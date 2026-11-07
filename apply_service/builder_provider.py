from .aws import AppGatewayBuilder, CloudFrontBuilder, CloudTrailBuilder, S3Builder
from .azure import (
    AppServiceBuilder,
    AzureFunctionsBuilder,
    CosmosDbBuilder,
    StorageAccountBuilder,
    VirtualMachineBuilder,
)
from .base import Builder
from .common import Provider
from .gc import ComputeEngineBuilder, GkeBuilder


class BuilderProvider:
    def __init__(self):
        self._provider: dict[tuple[Provider, str], Builder] = {
            (Provider.AWS, "S3"): S3Builder(),
            (Provider.AWS, "APP_GATEWAY"): AppGatewayBuilder(),
            (Provider.AWS, "CLOUD_FRONT"): CloudFrontBuilder(),
            (Provider.AWS, "CLOUD_TRAIL"): CloudTrailBuilder(),
            (Provider.AZURE, "STORAGE_ACCOUNT"): StorageAccountBuilder(),
            (Provider.AZURE, "VIRTUAL_MACHINE"): VirtualMachineBuilder(),
            (Provider.AZURE, "AZURE_FUNCTIONS"): AzureFunctionsBuilder(),
            (Provider.AZURE, "APP_SERVICE"): AppServiceBuilder(),
            (Provider.AZURE, "COSMOS_DB"): CosmosDbBuilder(),
            (Provider.GOOGLE_CLOUD, "COMPUTE_ENGINE"): ComputeEngineBuilder(),
            (Provider.GOOGLE_CLOUD, "GKE"): GkeBuilder(),
        }

    def provide(self, provider: Provider, resource_type: str) -> Builder:
        try:
            return self._provider[(provider, resource_type.upper())]
        except KeyError:
            raise ValueError(f"Unsupported resource: {provider}/{resource_type}") from None
