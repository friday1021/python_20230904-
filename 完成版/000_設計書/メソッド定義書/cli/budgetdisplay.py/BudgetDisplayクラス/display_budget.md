# クラス: BudgetDisplay

## 説明:
家計簿の情報を表示するためのクラスです。`DisplayManager`クラスと`MenuDisplay`クラスを継承しています。

## メソッド名: display_budget

### パラメータ:
- self: BudgetDisplay - インスタンス自体
- selected_budgetbook: str - 表示する家計簿名

### 戻り値:
なし

### 説明:
家計簿の一覧を画面表示するためのメソッドです。

### 処理内容:
- クエリをセットしてデータベースから指定された家計簿名のデータを取得します。
- 取得したデータが存在する場合、以下の情報を画面に表示します：
  - [`display_budget_summary`](../../../cli/budgetdisplay.py/BudgetDisplayクラス/display_budget_summary.html)メソッドを呼び出してヘッダ情報を表示。
  - [`display_income_details`](../../../cli/budgetdisplay.py/BudgetDisplayクラス/display_income_details.html)メソッドを呼び出して収入の詳細情報を表示。
  - [`display_payment_details`](../../../cli/budgetdisplay.py/BudgetDisplayクラス/display_payment_details.html)メソッドを呼び出して支出の詳細情報を表示。
- 取得したデータが存在しない場合、'家計簿が存在しません。'と表示します。

### 使用例:

```python
display = BudgetDisplay()
selected_budgetbook = "家計簿名"
display.display_budget(selected_budgetbook)
```

### 文法解説:

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
"SELECT * FROM budgetbooks WHERE book_name = ?;"
```