from .aws import (
    AppGatewayBuilder,
    CloudFrontBuilder,
    CloudTrailBuilder,
    Ec2Builder,
    S3Builder,
    SnsBuilder,
    SqsBuilder,
)
from .azure import (
    AppServiceBuilder,
    AzureFunctionsBuilder,
    ContainerRegistryBuilder,
    CosmosDbBuilder,
    KeyVaultBuilder,
    ServiceBusBuilder,
    StorageAccountBuilder,
    VirtualMachineBuilder,
)
from .base import Builder
from .common import Provider
from .gc import CloudRunBuilder, CloudStorageBuilder, ComputeEngineBuilder, GkeBuilder, PubSubBuilder


class BuilderProvider:
    def __init__(self):
        self._provider: dict[tuple[Provider, str], Builder] = {
            (Provider.AWS, "S3"): S3Builder(),
            (Provider.AWS, "APP_GATEWAY"): AppGatewayBuilder(),
            (Provider.AWS, "CLOUD_FRONT"): CloudFrontBuilder(),
            (Provider.AWS, "CLOUD_TRAIL"): CloudTrailBuilder(),
            (Provider.AWS, "EC2"): Ec2Builder(),
            (Provider.AWS, "SNS"): SnsBuilder(),
            (Provider.AWS, "SQS"): SqsBuilder(),
            (Provider.AZURE, "STORAGE_ACCOUNT"): StorageAccountBuilder(),
            (Provider.AZURE, "VIRTUAL_MACHINE"): VirtualMachineBuilder(),
            (Provider.AZURE, "AZURE_FUNCTIONS"): AzureFunctionsBuilder(),
            (Provider.AZURE, "APP_SERVICE"): AppServiceBuilder(),
            (Provider.AZURE, "COSMOS_DB"): CosmosDbBuilder(),
            (Provider.AZURE, "KEY_VAULT"): KeyVaultBuilder(),
            (Provider.AZURE, "CONTAINER_REGISTRY"): ContainerRegistryBuilder(),
            (Provider.AZURE, "SERVICE_BUS"): ServiceBusBuilder(),
            (Provider.GOOGLE_CLOUD, "COMPUTE_ENGINE"): ComputeEngineBuilder(),
            (Provider.GOOGLE_CLOUD, "GKE"): GkeBuilder(),
            (Provider.GOOGLE_CLOUD, "CLOUD_STORAGE"): CloudStorageBuilder(),
            (Provider.GOOGLE_CLOUD, "PUB_SUB"): PubSubBuilder(),
            (Provider.GOOGLE_CLOUD, "CLOUD_RUN"): CloudRunBuilder(),
        }

    def provide(self, provider: Provider, resource_type: str) -> Builder:
        try:
            return self._provider[(provider, resource_type.upper())]
        except KeyError:
            raise ValueError(f"Unsupported resource: {provider}/{resource_type}") from None
