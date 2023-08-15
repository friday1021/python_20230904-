# クラス: BudgetBook

## 説明:
家計簿の記録と管理を行うクラスです。

## メソッド名: select_record

### パラメータ:

- self: BudgetBook - インスタンス自体
- selected_budgetbook: str - 選択された家計簿の名前
- record_type: str - 選択された操作の種類（'income' 収入 / 'payment' 支出）

### 戻り値:

int - 選択された収入または支出の主キー（ID）。選択されなかった場合はNone。

### 説明:

一覧から収入または支出を選択するためのメソッドです。

### 処理内容:

- クエリ例を参考に、対象の家計簿の選択された方のテーブルから、収入または支出のデータを取得するクエリを作成し、変数`query`にセットします。
  - クエリ内で家計簿の名前とともに、収入または支出の種類に応じたテーブルとの関連を取得するためのサブクエリを使用します。
- 変数`values`に`(selected_budgetbook,)`をセットします。
- [`fetch_all`](../../../db/sql.py/SQLManagerクラス/fetch_all.html)メソッドに変数`query`と`values`を渡してクエリを実行し、戻り値を変数`records`に格納します。
- 変数`records`にデータがない場合（空の場合）、選択された家計簿の指定された種類のデータは存在しないことを通知してNoneを返却します。
- 変数`records`にデータがある場合、一覧表示を行い、選択された項目の主キー（ID）を取得するための入力を受け付けます。
- 選択された項目が有効範囲内になるまで、繰り返して入力を受け付けます。
- 選択された項目の主キー（ID）を取り出して返却します。選択されなかった場合はNoneを返します。

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
# 対象の家計簿の選択された方のテーブルからデータを取得
if record_type == 'income':
    query = "SELECT id, amount, created_at FROM incomes WHERE budgetbooks_id = (SELECT id FROM budgetbooks WHERE book_name = ?);"
else:
    query = "SELECT id, amount, created_at FROM payments WHERE budgetbooks_id = (SELECT id FROM budgetbooks WHERE book_name = ?);"
values = (selected_budgetbook,)
```