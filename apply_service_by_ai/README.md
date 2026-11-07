# Apply service: 定義と関数による実装

既存の `apply_service` と独立した別実装。全11リソースの入力ルール・既定値・
printの形式・Resultの内容を維持し、SDKや外部APIを使わずに動く。

```sh
python3.14 -m apply_service_by_ai
python3.14 -B -m unittest apply_service_by_ai.test_service -v
```

```python
from apply_service_by_ai import ApplyService, Provider, Request

service = ApplyService()
result = service.apply(Request(
    provider=Provider.AWS,
    resource_type="S3",
    parameters={"bucket_name": "example-bucket", "region": "ap-northeast-1"},
))
```

## 設計

`ApplyService` が「選択 → 検証・正規化 → 実行 → 共通出力」を担当する。
各クラウドのファイルには `ResourceSpec` を登録する。Specは項目の定義と実行関数の組。
データを表す `Request`・`Result`・`Field`・`ResourceSpec` にdataclassを使い、
処理を進めるサービスは通常のクラスにした。

現状の模擬実行は「検証したパラメータを表示してResultを返す」ため、
リソースごとのBuilder/Applierクラスを作る必要がない。
必須値、選択肢、範囲、既定値を宣言し、同じ仕組みで検証する。
クラウド固有の検証関数は必要な項目だけに適用する。

```python
"S3": ResourceSpec(
    fields={
        "bucket_name": Field(string_length(3, 63)),
        "region": Field(text),
        "versioning": Field(boolean, default=False),
    },
    execute=simulated("Simulated S3 bucket creation: {bucket_name}"),
)
```

## 差し替え

`ResourceSpec.execute` は検証済みの読み取り専用Mappingを受け取り、Resultを返す関数。
専用処理が必要なリソースは、この関数だけを差し替えられる。
引数間の検証が必要なら、実行関数の冒頭で行ってから外部への操作に進める。
認証が必要になったら、認証用オブジェクトを受け取る関数や通常のクラスのメソッドを登録できる。
現段階では認証処理は実装していない。

`ApplyService(resources=...)` で登録内容全体を差し替えられる。
`output=...` に文字列を受け取る関数を渡すと、表示先も差し替えられる。
たとえば `ApplyService(output=messages.append)` なら標準出力の代わりにリストへ保存する。

検証失敗・未登録リソースはValueError、実行中の例外は呼び出し元へ伝播する。
入力の余分な項目は既存実装と同様に無視する。出力には検証した項目だけを使う。
検証ルールはデモ仕様で、実クラウドの全制約は再現していない。
既存の `AWS / APP_GATEWAY` という登録名も維持している。

この方式はMappingベースなので、専用クラスの属性に比べ、実行関数内の項目名を静的型検査で
確認しにくい。実処理や引数間の制約が複雑になったリソースでは、検証済みの設定を型付きの
オブジェクトへ変換する設計が候補になる。全リソースを先回りして複雑にしない方針とした。
