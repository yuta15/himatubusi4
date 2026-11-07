from contextlib import redirect_stdout
from dataclasses import replace
from io import StringIO
import unittest

from . import ApplyService, Field, Provider, Request, ResourceSpec, Result
from .examples import example_requests
from .validation import text


class ApplyServiceTests(unittest.TestCase):
    def test_all_resources_match_existing_output_and_results(self):
        from apply_service import ApplyService as OriginalService
        from apply_service import BuilderProvider, Provider as OriginalProvider, Request as OriginalRequest

        original = OriginalService(BuilderProvider())
        service = ApplyService()
        requests = example_requests()
        self.assertEqual(len(requests), 11)
        for request in requests:
            with self.subTest(resource=request.resource_type):
                before = request.parameters.copy()
                expected = StringIO()
                with redirect_stdout(expected):
                    result = original.apply(OriginalRequest(
                        OriginalProvider(request.provider.value), request.resource_type, request.parameters,
                    ))
                actual = StringIO()
                with redirect_stdout(actual):
                    new_result = service.apply(replace(request, resource_type=request.resource_type.lower()))
                self.assertEqual(actual.getvalue(), expected.getvalue())
                self.assertEqual((new_result.result, new_result.message), (result.result, result.message))
                self.assertEqual(request.parameters, before)

    def test_missing_and_invalid_fields_do_not_produce_output(self):
        output = []
        service = ApplyService(output=output.append)
        optional = {"versioning": False, "enabled": True, "multi_region": True, "private_cluster": False}
        for request in example_requests():
            for key, value in request.parameters.items():
                with self.subTest(resource=request.resource_type, field=key):
                    missing = dict(request.parameters)
                    del missing[key]
                    if key in optional:
                        self.assertTrue(service.apply(replace(request, parameters=missing)).result)
                        self.assertIn(f": {optional[key]}", output.pop())
                    else:
                        with self.assertRaisesRegex(ValueError, key):
                            service.apply(replace(request, parameters=missing))
                    invalid = [None]
                    if isinstance(value, str):
                        invalid += ["", "  ", 1]
                    elif type(value) is int:
                        invalid += [True, "1", 1.5]
                    else:
                        invalid += [1, "false"]
                    for bad_value in invalid:
                        with self.assertRaisesRegex(ValueError, key):
                            service.apply(replace(request, parameters={**request.parameters, key: bad_value}))
        self.assertEqual(output, [])

    def test_resource_constraints_and_boundaries(self):
        cases = [
            ("S3", "bucket_name", ("ab", "a" * 64), ("abc", "a" * 63)),
            ("APP_GATEWAY", "port", (0, 65536), (1, 65535)),
            ("APP_GATEWAY", "target_url", ("ftp://example.com",), ("http://example.com",)),
            ("CLOUD_FRONT", "origin_domain", ("https://example.com", "example.com/path", "a b"), ("example.com",)),
            ("STORAGE_ACCOUNT", "account_name", ("ABc", "ab", "a" * 25, "あいう"), ("abc", "a" * 24)),
            ("STORAGE_ACCOUNT", "replication", ("invalid",), ("LRS", "GRS")),
            ("VIRTUAL_MACHINE", "disk_size_gb", (0, 1025), (1, 1024)),
            ("AZURE_FUNCTIONS", "runtime", ("invalid",), ("python", "node", "dotnet")),
            ("APP_SERVICE", "runtime", ("invalid",), ("python", "node", "dotnet")),
            ("COSMOS_DB", "throughput", (399, 401, 10001), (400, 10000)),
            ("GKE", "node_count", (0, 101), (1, 100)),
        ]
        service = ApplyService(output=lambda _: None)
        requests = {request.resource_type: request for request in example_requests()}
        for kind, key, invalid, valid in cases:
            for value in (*invalid, *valid):
                with self.subTest(resource=kind, field=key, value=value):
                    request = requests[kind]
                    request = replace(request, parameters={**request.parameters, key: value})
                    if value in invalid:
                        with self.assertRaisesRegex(ValueError, key):
                            service.apply(request)
                    else:
                        self.assertTrue(service.apply(request).result)

    def test_unsupported_resource_and_provider_combination(self):
        service = ApplyService()
        request = example_requests()[0]
        for invalid in (replace(request, resource_type="UNKNOWN"), replace(request, provider=Provider.AZURE)):
            with self.subTest(request=invalid), self.assertRaisesRegex(ValueError, "Unsupported resource"):
                service.apply(invalid)
        with self.assertRaises(ValueError):
            ApplyService(resources={}).apply(request)

    def test_custom_execution_receives_validated_values(self):
        calls, output = [], []

        def execute(values):
            calls.append(values)
            return Result(True, f"Custom execution: {values['name']}")

        spec = ResourceSpec({"name": Field(text)}, execute)
        registry = {(Provider.AWS, "S3"): spec}
        service = ApplyService(registry, output=output.append)
        registry.clear()
        with self.assertRaises(ValueError):
            service.apply(Request(Provider.AWS, "S3", {"name": " "}))
        self.assertEqual(calls, [])
        self.assertEqual(output, [])
        result = service.apply(Request(Provider.AWS, "S3", {"name": "  example  "}))
        self.assertEqual(result.message, "Custom execution: example")
        self.assertEqual(dict(calls[0]), {"name": "example"})
        self.assertEqual(output, ["[AWS/S3]\n  name : example"])
        with self.assertRaises(TypeError):
            calls[0]["name"] = "changed"

    def test_execution_failure_propagates_without_success_output(self):
        output = []

        def fail(values):
            raise RuntimeError("execution failed")

        service = ApplyService({(Provider.AWS, "S3"): ResourceSpec({}, fail)}, output=output.append)
        with self.assertRaisesRegex(RuntimeError, "execution failed"):
            service.apply(Request(Provider.AWS, "S3", {}))
        self.assertEqual(output, [])


if __name__ == "__main__":
    unittest.main()
