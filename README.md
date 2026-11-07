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
│   └── sqs/
├── azure/
│   ├── storage_account/
│   ├── virtual_machine/
│   ├── azure_functions/
│   ├── app_service/
│   ├── cosmos_db/
│   ├── key_vault/
│   ├── container_registry/
│   └── service_bus/
└── gc/
    ├── compute_engine/
    ├── gke/
    ├── cloud_storage/
    ├── pub_sub/
    └── cloud_run/
```

各リソースに同じ構成の `builder.py` と `applier.py` がある。

Python 3.14以上で `apply_service` 全20種類の実行例を確認できる。
`apply_service_by_ai` は従来の11種類に対応する。
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
| AWS | CLOUD_FRONT | origin_domain（スキーム・パスなし） | enabled=True |
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

検証ルールや数値範囲は構造を試すためのサンプル仕様で、実際のクラウドの全制約を再現するものではない。
`AWS / APP_GATEWAY` は既存の登録キーをそのまま使用したデモ用のゲートウェイ。
