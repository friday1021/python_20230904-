# クラス: BudgetDisplay

## 説明:
家計簿の情報を表示するためのクラスです。`DisplayManager`クラスと`MenuDisplay`クラスを継承しています。

## メソッド名: display_payments

### パラメータ:
- self: BudgetDisplay - インスタンス自体
- selected_budgetbook: str - 表示する家計簿名

### 戻り値:
なし

### 説明:
支出を表示するためのメソッドです。

### 処理内容:
- データベースから指定された家計簿名の支出データを取得するクエリを作成し、変数`query`にセットします。
- 変数`values`に`(selected_budgetbook,)`をセットします。
- [`fetch_all`](../../../db/sql.py/SQLManagerクラス/fetch_all.html)メソッドに変数`query`と変数`values`を渡してクエリを実行し、戻り値を変数`payments`にセットします。
- 変数`payments`が存在する（空でない）場合、各支出情報を一覧表示します。
- 取得した支出データが存在しない場合、'家計簿名 の支出はありません。'と表示します。

### 使用例:
```python
display = BudgetDisplay()
selected_budgetbook = "家計簿名"
display.display_payments(selected_budgetbook)
```

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
"SELECT amount, created_at FROM payments WHERE budgetbooks_id = (SELECT id FROM budgetbooks WHERE book_name = ?);"
```