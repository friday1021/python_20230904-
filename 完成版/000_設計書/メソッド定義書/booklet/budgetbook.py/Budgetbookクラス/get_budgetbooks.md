# クラス: BudgetBook

## 説明:
家計簿の記録と管理を行うクラスです。

## メソッド名: get_budgetbooks
### パラメータ:
- self: BudgetBook - インスタンス自体
### 戻り値:
list[str] - 存在する家計簿の一覧（家計簿名のリスト）
### 説明:
データベースから存在する家計簿の一覧を取得して返します。
### 処理内容:
- データベースから全ての家計簿名を取得するクエリを作成し、変数`query`にセットします。
- [`fetch_all`](../../../db/sql.py/SQLManagerクラス/fetch_all.html)メソッドに変数`query`を渡してクエリを実行し、戻り値を変数`result`にセットします。
- 取得結果がある場合は、各行の家計簿名をリストに格納して返します。
- 取得結果がない場合は空のリストを返します。

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
"SELECT book_name FROM budgetbooks;"
```