from .resource import Field, ResourceSpec, simulated
from .validation import boolean, hostname, http_url, integer, string_length, text


RESOURCES = {
    "S3": ResourceSpec(
        fields={
            "bucket_name": Field(string_length(3, 63)),
            "region": Field(text),
            "versioning": Field(boolean, default=False),
        },
        execute=simulated("Simulated S3 bucket creation: {bucket_name}"),
    ),
    # 既存の登録名を維持したデモ用のゲートウェイ。
    "APP_GATEWAY": ResourceSpec(
        fields={"name": Field(text), "target_url": Field(http_url), "port": Field(integer(1, 65535))},
        execute=simulated("Simulated gateway creation: {name}"),
    ),
    "CLOUD_FRONT": ResourceSpec(
        fields={"origin_domain": Field(hostname), "enabled": Field(boolean, default=True)},
        execute=simulated("Simulated CloudFront distribution creation: {origin_domain}"),
    ),
    "CLOUD_TRAIL": ResourceSpec(
        fields={
            "trail_name": Field(text),
            "bucket_name": Field(text),
            "multi_region": Field(boolean, default=True),
        },
        execute=simulated("Simulated CloudTrail trail creation: {trail_name}"),
    ),
}
