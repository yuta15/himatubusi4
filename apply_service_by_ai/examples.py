from .models import Provider, Request


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
        Request(Provider.AWS, "EC2", {
            "name": "example-ec2", "region": "ap-northeast-1", "instance_type": "t3.micro",
        }),
        Request(Provider.AWS, "SNS", {
            "topic_name": "example-topic", "region": "ap-northeast-1",
        }),
        Request(Provider.AWS, "SQS", {
            "queue_name": "example-queue", "region": "ap-northeast-1", "visibility_timeout": 30,
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
        Request(Provider.AZURE, "KEY_VAULT", {
            "vault_name": "example-vault", "location": "japaneast",
        }),
        Request(Provider.AZURE, "CONTAINER_REGISTRY", {
            "registry_name": "exampleregistry", "location": "japaneast", "sku": "Basic",
        }),
        Request(Provider.AZURE, "SERVICE_BUS", {
            "namespace_name": "example-bus", "location": "japaneast", "sku": "Standard",
        }),
        Request(Provider.GOOGLE_CLOUD, "COMPUTE_ENGINE", {
            "name": "example-instance", "zone": "asia-northeast1-a", "machine_type": "e2-micro",
        }),
        Request(Provider.GOOGLE_CLOUD, "GKE", {
            "cluster_name": "example-cluster", "location": "asia-northeast1-a",
            "node_count": 3, "private_cluster": True,
        }),
        Request(Provider.GOOGLE_CLOUD, "CLOUD_STORAGE", {
            "bucket_name": "example-gc-bucket", "location": "ASIA-NORTHEAST1",
        }),
        Request(Provider.GOOGLE_CLOUD, "PUB_SUB", {
            "topic_name": "example-topic", "project_id": "example-project",
        }),
        Request(Provider.GOOGLE_CLOUD, "CLOUD_RUN", {
            "service_name": "example-service", "region": "asia-northeast1",
            "image": "asia-northeast1-docker.pkg.dev/example-project/example-repo/app:latest",
        }),
    ]
