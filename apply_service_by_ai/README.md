# Apply service: 入力定義とリソース別の実行関数

既存の `apply_service` と同じ全29リソースを扱う別実装。
入力の検証、処理内容のprint、Resultの返却までを実装している。

対応リソースはAWSがS3・APP_GATEWAY・CLOUD_FRONT・CLOUD_TRAIL・EC2・SNS・SQS、
AzureがSTORAGE_ACCOUNT・VIRTUAL_MACHINE・AZURE_FUNCTIONS・APP_SERVICE・COSMOS_DB・KEY_VAULT・CONTAINER_REGISTRY・SERVICE_BUS、
Google CloudがCOMPUTE_ENGINE・GKE・CLOUD_STORAGE・PUB_SUB・CLOUD_RUN。
さらにAWSにECR・SECRETS_MANAGER・CLOUDWATCH_LOGS、
AzureにMANAGED_IDENTITY・LOG_ANALYTICS・EVENT_HUBS、
Google CloudにARTIFACT_REGISTRY・SECRET_MANAGER・BIGQUERY_DATASETを追加している。
各リソースのパラメータと既定値は[ルートREADME](../README.md)の一覧を参照。

```sh
python3.14 main.py --implementation ai
```

```python
from apply_service_by_ai import ApplyService, Provider, Request

service = ApplyService()
result = service.apply(Request(
    Provider.AWS,
    "S3",
    {"bucket_name": "example-bucket", "region": "ap-northeast-1"},
))
```

## 構成

`ApplyService` がリソース定義を選択し、検証済みの値を専用の実行関数に渡す。
リソース定義は入力項目と実行関数の組で、各リソースのファイルにまとめている。
各クラウドの `__init__.py` が定義を `RESOURCES` として集約する。

```text
apply_service_by_ai/
├── resources/
│   ├── aws/
│   │   ├── s3.py
│   │   ├── app_gateway.py
│   │   ├── cloud_front.py
│   │   ├── cloud_trail.py
│   │   ├── ec2.py
│   │   ├── sns.py
│   │   ├── sqs.py
│   │   ├── ecr.py
│   │   ├── secrets_manager.py
│   │   └── cloudwatch_logs.py
│   ├── azure/
│   │   ├── storage_account.py
│   │   ├── virtual_machine.py
│   │   ├── azure_functions.py
│   │   ├── app_service.py
│   │   ├── cosmos_db.py
│   │   ├── key_vault.py
│   │   ├── container_registry.py
│   │   ├── service_bus.py
│   │   ├── managed_identity.py
│   │   ├── log_analytics.py
│   │   └── event_hubs.py
│   └── google_cloud/
│       ├── compute_engine.py
│       ├── gke.py
│       ├── cloud_storage.py
│       ├── pub_sub.py
│       ├── cloud_run.py
│       ├── artifact_registry.py
│       ├── secret_manager.py
│       └── bigquery_dataset.py
├── service.py
├── models.py
├── resource.py
├── validation.py
├── output.py
├── examples.py
└── __init__.py
```

```python
SPEC = ResourceSpec(
    fields={
        "bucket_name": Field(string_length(3, 63)),
        "region": Field(text),
        "versioning": Field(boolean, default=False),
    },
    execute=create_s3,
)
```

各実行関数にはリソース固有の処理を書く。
現在はAPI呼び出しを置く箇所で引数をprintし、Resultを返している。
SDKを使う場合は、その関数内のprintをAPI呼び出しに置き換える。
共通の表示形式は `output.py` の `format_resource()` を利用する。

- `resources/<クラウド>/<リソース>.py`: リソース定義と専用の実行関数。
- `resource.py`・`validation.py`: 必須項目、型、範囲、既定値などの共通検証。
- `service.py`: リソースの選択、検証、実行。
- `models.py`: Provider、Request、Result。

クライアント層、認証、SDK連携、リソースIDの生成は追加していない。
Resultは既存実装と同じ `result` と `message` の2項目。
サービス自身はprintせず、実行関数が出力を担当する。

`ApplyService(resources=...)` でリソース定義や実行関数を差し替えられる。
検証済みの値は読み取り専用Mappingとして実行関数に渡す。
項目間の制約は `ResourceSpec.validate_values` で、各項目の検証後、実行関数を呼ぶ前に検証する。
CloudFrontは `distribution_name`、1件以上の `origins`、`default_origin_id` が必須で、
`enabled` の既定値は `True`。各オリジンは `id`、`domain`、任意の `path` を持つ。
`id` の重複、空のdomain、URLスキームやパスを含むdomainは拒否する。
`path` は `/` で始まる文字列、`default_origin_id` は `origins` に存在するIDとする。
検証失敗・未登録リソースはValueError、実行関数の例外は呼び出し元に伝播する。

全29リソースで、入力ルール、既定値、出力、Resultの内容が既存実装と同じ。
Secrets Manager / Secret Managerはシークレット本体の作成を想定し、秘密値の登録は扱わない。
検証ルールはデモ仕様で、実クラウドの全制約は再現していない。
`AWS / APP_GATEWAY` という既存の登録キーもそのまま使う。
