# クラス: BudgetBook

## 説明:
家計簿の記録と管理を行うクラスです。

## メソッド名: delete_record

### パラメータ:

- self: BudgetBook - インスタンス自体
- record_type: str - 削除するデータの種類（'income' 収入 / 'payment' 支出）
- record_id: int - 削除するデータの主キー（ID）

### 戻り値: なし

### 説明:

収入または支出のデータを削除するためのメソッドです。

### 処理内容:

- 削除対象のデータの種類に応じて、適切なテーブルを特定するためのクエリを生成し、変数`query`にセットします。
- 変数`values`に`(record_id,)`をセットします。
- 生成されたクエリには、対象のデータの主キー（ID）を使用した条件が含まれます。
- [`execute_query`](../../../db/sql.py/SQLManagerクラス/execute_query.html)メソッドに変数`query`と`values`を渡してクエリを実行し、削除が成功した場合は成功メッセージを表示します。
- 削除が失敗した場合はエラーメッセージを表示します。

### データベース関連の文法解説:

```python
# 「budgetbooksテーブルから全ての列の値を取り出す。ただし抽出する行はbook_name列の値が?の行に絞り込む」という意味のクエリを作成する
query = "SELECT * FROM budgetbooks WHERE book_name = ?;"
# ('堀川の家計簿',)を変数valuesにセット
values = ('堀川の家計簿',)
# ?の部分を変数values:'堀川の家計簿'に置き換えてクエリを実行
result = self.budget.sql_manager.fetch_one(query, values)
```

#### クエリ例

```python
# 対象のテーブルを特定してクエリをセット
if record_type == 'income':
    query = "DELETE FROM incomes WHERE id = ?;"
else:
    query = "DELETE FROM payments WHERE id = ?;"
```