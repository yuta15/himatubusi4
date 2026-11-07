Strategyによる、クラウド・リソースごとの処理の差し替えを検証するサンプル。

`ApplyService → BuilderProvider → Builder → Applier` の順に処理する。
Builderが入力を検証し、検証済みの値を持つApplierを生成する。
Applierは処理内容をprintし、成功のResultを返す。SDKや外部APIは使用しない。
出力は親クラス `Applier._print()` で統一し、各Applierは表示する項目を渡す。

```text
[AWS/S3]
  bucket_name : example-bucket
  region      : ap-northeast-1
  versioning  : True
```

具象クラスは `apply_service/<クラウド>/<リソース>/` に配置し、
`builder.py` と `applier.py` に分けている。
クラウドディレクトリは `aws`、`azure`、`gc`。

```text
apply_service/
├── aws/
│   ├── s3/
│   │   ├── builder.py
│   │   └── applier.py
│   ├── app_gateway/
│   ├── cloud_front/
│   ├── cloud_trail/
│   ├── ec2/
│   ├── sns/
│   ├── sqs/
│   ├── ecr/
│   ├── secrets_manager/
│   └── cloudwatch_logs/
├── azure/
│   ├── storage_account/
│   ├── virtual_machine/
│   ├── azure_functions/
│   ├── app_service/
│   ├── cosmos_db/
│   ├── key_vault/
│   ├── container_registry/
│   ├── service_bus/
│   ├── managed_identity/
│   ├── log_analytics/
│   └── event_hubs/
└── gc/
    ├── compute_engine/
    ├── gke/
    ├── cloud_storage/
    ├── pub_sub/
    ├── cloud_run/
    ├── artifact_registry/
    ├── secret_manager/
    └── bigquery_dataset/
```

各リソースに同じ構成の `builder.py` と `applier.py` がある。

Python 3.14以上で `apply_service` 全29種類の実行例を確認できる。
`apply_service_by_ai` も同じ29種類に対応する。CloudFrontは `apply_service` のみ新しいパラメータ仕様を使用し、AI版は従来の `origin_domain` を使用する。
引数なしでは既存実装とAI版を順に実行する。実装ごとの実行も可能。

```sh
python3.14 main.py
python3.14 main.py --implementation original
python3.14 main.py --implementation ai
```

`Request.parameters` はリソースごとに異なる。必須文字列は空白のみも拒否し、前後の空白を除去する。
検証失敗と未対応のリソースはValueErrorになり、呼び出し元まで伝播する。

| Provider | リソース | 必須パラメータ | 任意パラメータ（既定値） |
|---|---|---|---|
| AWS | S3 | bucket_name（3〜63文字）, region | versioning=False |
| AWS | APP_GATEWAY | name, target_url（http/https）, port（1〜65535） | — |
| AWS | CLOUD_FRONT | distribution_name, origins（1件以上）, default_origin_id | enabled=True |
| AWS | CLOUD_TRAIL | trail_name, bucket_name | multi_region=True |
| AWS | EC2 | name, region, instance_type | — |
| AWS | SNS | topic_name, region | fifo=False |
| AWS | SQS | queue_name, region, visibility_timeout（秒、0〜43200） | — |
| AZURE | STORAGE_ACCOUNT | account_name（英小文字・数字3〜24文字）, location, replication（LRS/GRS） | — |
| AZURE | VIRTUAL_MACHINE | name, size, disk_size_gb（1〜1024） | — |
| AZURE | AZURE_FUNCTIONS | name, runtime（python/node/dotnet）, storage_account | — |
| AZURE | APP_SERVICE | name, plan_name, runtime（python/node/dotnet） | — |
| AZURE | COSMOS_DB | account_name, database_name, throughput（400〜10000、100刻み） | — |
| AZURE | KEY_VAULT | vault_name, location | soft_delete=True |
| AZURE | CONTAINER_REGISTRY | registry_name, location, sku（Basic/Standard/Premium） | — |
| AZURE | SERVICE_BUS | namespace_name, location, sku（Basic/Standard/Premium） | — |
| GOOGLE_CLOUD | COMPUTE_ENGINE | name, zone, machine_type | — |
| GOOGLE_CLOUD | GKE | cluster_name, location, node_count（1〜100） | private_cluster=False |
| GOOGLE_CLOUD | CLOUD_STORAGE | bucket_name, location | versioning=False |
| GOOGLE_CLOUD | PUB_SUB | topic_name, project_id | — |
| GOOGLE_CLOUD | CLOUD_RUN | service_name, region, image | allow_unauthenticated=False |

`apply_service` のCloudFrontでは、各オリジンに必須文字列の `id` と `domain`、任意の `path` を指定する。
`id` は重複不可、`domain` は空文字列・URLスキーム・パスを許可しない。
`path` を指定する場合は `/` から始まる文字列とする。`default_origin_id` は `origins` に存在するIDを指定する。

検証ルールや数値範囲は構造を試すためのサンプル仕様で、実際のクラウドの全制約を再現するものではない。
`AWS / APP_GATEWAY` は既存の登録キーをそのまま使用したデモ用のゲートウェイ。

両実装の追加リソースも、検証・print・Result返却までのデモとして動作する。
Secrets Manager / Secret Managerでは秘密値の登録は扱わない。以下の数値範囲や選択肢もデモ仕様。

| Provider | リソース | 必須パラメータ | 任意パラメータ（既定値） |
|---|---|---|---|
| AWS | ECR | repository_name, region | scan_on_push=True |
| AWS | SECRETS_MANAGER | secret_name, region | — |
| AWS | CLOUDWATCH_LOGS | log_group_name, region | retention_days=30（1〜365） |
| AZURE | MANAGED_IDENTITY | identity_name, location | — |
| AZURE | LOG_ANALYTICS | workspace_name, location | retention_days=30（30〜730） |
| AZURE | EVENT_HUBS | namespace_name, location | sku="Standard"（Basic/Standard/Premium） |
| GOOGLE_CLOUD | ARTIFACT_REGISTRY | repository_name, project_id, location | format="DOCKER"（DOCKER/MAVEN/NPM） |
| GOOGLE_CLOUD | SECRET_MANAGER | secret_id, project_id | — |
| GOOGLE_CLOUD | BIGQUERY_DATASET | dataset_id, project_id | location="asia-northeast1" |
