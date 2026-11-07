import argparse

from apply_service import ApplyService, BuilderProvider, Provider, Request
from apply_service_by_ai import ApplyService as AiApplyService
from apply_service_by_ai.examples import example_requests as ai_example_requests


def example_requests() -> list[Request]:
    return [
        Request(Provider.AWS, "S3", {
            "bucket_name": "example-bucket", "region": "ap-northeast-1", "versioning": True,
        }),
        Request(Provider.AWS, "APP_GATEWAY", {
            "name": "example-gateway", "target_url": "https://example.com", "port": 443,
        }),
        Request(Provider.AWS, "CLOUD_FRONT", {
            "origin_domain": "example.com", "enabled": True,
        }),
        Request(Provider.AWS, "CLOUD_TRAIL", {
            "trail_name": "example-trail", "bucket_name": "audit-bucket", "multi_region": True,
        }),
        Request(Provider.AZURE, "STORAGE_ACCOUNT", {
            "account_name": "examplestorage", "location": "japaneast", "replication": "LRS",
        }),
        Request(Provider.AZURE, "VIRTUAL_MACHINE", {
            "name": "example-vm", "size": "Standard_B1s", "disk_size_gb": 32,
        }),
        Request(Provider.AZURE, "AZURE_FUNCTIONS", {
            "name": "example-function", "runtime": "python", "storage_account": "examplestorage",
        }),
        Request(Provider.AZURE, "APP_SERVICE", {
            "name": "example-app", "plan_name": "example-plan", "runtime": "node",
        }),
        Request(Provider.AZURE, "COSMOS_DB", {
            "account_name": "example-cosmos", "database_name": "example-db", "throughput": 400,
        }),
        Request(Provider.GOOGLE_CLOUD, "COMPUTE_ENGINE", {
            "name": "example-instance", "zone": "asia-northeast1-a", "machine_type": "e2-micro",
        }),
        Request(Provider.GOOGLE_CLOUD, "GKE", {
            "cluster_name": "example-cluster", "location": "asia-northeast1-a",
            "node_count": 3, "private_cluster": True,
        }),
    ]


def run_original() -> None:
    print("=== apply_service ===")
    service = ApplyService(BuilderProvider())
    for request in example_requests():
        print(service.apply(request))
        print("-" * 60)


def run_ai() -> None:
    print("=== apply_service_by_ai ===")
    service = AiApplyService()
    for request in ai_example_requests():
        print(service.apply(request))
        print("-" * 60)


def main() -> None:
    parser = argparse.ArgumentParser(description="既存実装とAI版のクラウドリソース適用デモ")
    parser.add_argument(
        "--implementation",
        choices=("original", "ai", "both"),
        default="both",
        help="実行する実装（既定: both）",
    )
    args = parser.parse_args()
    if args.implementation in ("original", "both"):
        run_original()
    if args.implementation in ("ai", "both"):
        run_ai()


if __name__ == "__main__":
    main()
