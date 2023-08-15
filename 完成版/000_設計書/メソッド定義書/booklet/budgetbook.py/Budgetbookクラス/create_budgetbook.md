# クラス: BudgetBook

## 説明:
家計簿の記録と管理を行うクラスです。

## メソッド名: create_budgetbook

### パラメータ:

- self: BudgetBook - インスタンス自体
- book_name: str - 作成する家計簿の名前

### 戻り値:

bool - 家計簿の作成が成功したかどうか（True: 成功, False: 失敗）

### 説明:

新しい家計簿をデータベースに作成します。

### 処理内容:

- クエリを作成し、変数`query`にセットして、新しい家計簿をデータベースに作成します。
- 変数`values`に`(book_name,)`をセットします。
- 家計簿の名前と作成日時、更新日時をクエリにセットします。
- [`execute_query`](../../../db/sql.py/SQLManagerクラス/execute_query.html)メソッドへ変数`query`と変数`values`を投げて実行結果を返却します。作成に成功した場合はTrueを、失敗した場合はFalseを返します。

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
"INSERT INTO budgetbooks (book_name, created_at, updated_at) VALUES (?, datetime('now'), datetime('now'));"
```