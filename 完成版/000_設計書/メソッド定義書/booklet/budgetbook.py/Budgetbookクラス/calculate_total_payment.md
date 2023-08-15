# クラス: BudgetBook

## 説明:
家計簿の記録と管理を行うクラスです。

## メソッド名: calculate_total_payment

### パラメータ:

- selected_budgetbook: str - 選択された家計簿名

### 戻り値:

int - 支出の合計金額

### 説明:

指定された家計簿の支出の合計金額をデータベースから集計します。

### 処理内容:

- 収入を取得するためのSQLクエリを作成し、変数`payment_query`にセットします。
- [`fetch_one`](../../../db/sql.py/SQLManagerクラス/fetch_one.html)メソッドに変数`payment_query`と`selected_budgetbook`を渡してクエリを実行し、戻り値の支出合計金額を変数`total_payment`にセットします。
- 収入が存在すれば変数`total_payment`を返し、存在しなければ0を返します。

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
'SELECT SUM(amount) FROM payments WHERE budgetbooks_id = (SELECT id FROM budgetbooks WHERE book_name = ?);'
```