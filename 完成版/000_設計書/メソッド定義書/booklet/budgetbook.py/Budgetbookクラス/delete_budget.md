# クラス: BudgetBook

## 説明:
家計簿の記録と管理を行うクラスです。

## メソッド名: delete_budget

### パラメータ:

- self: BudgetBook - インスタンス自体
- selected_budgetbook: str - 選択された家計簿名

### 戻り値:

bool - 削除が成功した場合はTrue、失敗した場合はFalse

### 説明:

指定された家計簿を削除します。削除の確認をユーザーに求めます。

### 処理内容:

- 削除確認メッセージを表示し、ユーザーからの入力を受け取ります。
- 入力が "y" の場合:
  - 削除用のSQLクエリを生成し、変数`query`にセットします。
  - 変数`values`に`(selected_budgetbook,)`をセットします。
  - [`execute_query`](../../../db/sql.py/SQLManagerクラス/execute_query.html)メソッドに変数`query`と`values`を渡してクエリを実行します。
  - 削除が成功した場合は成功メッセージを表示し、Trueを返します。
  - 削除が失敗した場合は失敗メッセージを表示し、Falseを返します。
- 入力が "y" 以外の場合はFalseを返します。


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
"DELETE FROM budgetbooks WHERE book_name = ?;"
```