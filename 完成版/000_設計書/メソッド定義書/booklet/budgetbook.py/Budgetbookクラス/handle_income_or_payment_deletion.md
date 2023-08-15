# クラス: BudgetBook

## 説明:
家計簿の記録と管理を行うクラスです。

## メソッド名: handle_income_or_payment_deletion
### パラメータ:
- self: BudgetBook - インスタンス自体
- selected_budgetbook: str - 選択された家計簿名
### 戻り値:
なし
### 説明:
収入または支出の削除対象を操作します。削除する対象をユーザーに確認し、削除の実行を行います。
### 処理内容:
- 削除対象を`income`または`payment`から選択させ、いずれかの文字列を変数`record_type`にセットします。
- [`select_record`](./select_record.html)メソッドに変数`selected_budgetbook`と`record_type`を渡して選択された削除対象のレコードのIDを取得します。
- レコードIDが存在する場合、[`delete_record`](./delete_record.html)メソッドに変数`record_type`と`record_id`を渡して削除対象のレコードを削除します。

