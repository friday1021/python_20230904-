# クラス: BudgetDisplay

## 説明:
家計簿の情報を表示するためのクラスです。`DisplayManager`クラスと`MenuDisplay`クラスを継承しています。

## メソッド名: display_budgetbook_menu

### パラメータ:
- self: BudgetDisplay - インスタンス自体
- selected_budgetbook: str - 選択された家計簿名

### 戻り値:
なし

### 説明:
家計簿の操作可能な内容を表示するためのメソッドです。

### 処理内容:
- 無限ループ内で、下記の処理を行います。
  - [`get_budgetbook_menu`](../../displaymanager.py/DisplayManagerクラス/get_budgetbook_menu.html)メソッドを呼び出し、戻り値を変数`budgetbook_menu`にセットします。
  - [`display_menu`](../../displaymanager.py/MenuDisplayクラス/display_menu.html)メソッドに変数`budgetbook_menu`を渡し、メニューを表示します。
  - [`display_choose_option`](./display_choose_option.html)メソッドを呼び出し、戻り値を変数`choice_budgetbook_menu`にセットします。
  - ユーザーの選択を受け取り、選択が有効な場合、選択した機能に応じて各メソッドを呼び出します。
    - 選択が「表示」の場合[`display_budget`](./display_budget.html)メソッドに変数`selected_budgetbook`を渡し、表示を依頼します。
    - 選択が「記録」の場合、[`record_budget`](../../../booklet/budgetbook.py/Budgetbookクラス/record_budget.html)に変数`selected_budgetbook`を渡し、記録処理を依頼します。
    - 選択が「この家計簿を削除」の場合、[`delete_budget`](../../../booklet/budgetbook.py/Budgetbookクラス/delete_budget.html)メソッドに変数`selected_budgetbook`を渡し、戻り値が`True`なら無限ループを抜けます。
    - 選択が「収入/支出の削除」の場合、[`handle_income_or_payment_deletion`](../../../booklet/budgetbook.py/Budgetbookクラス/handle_income_or_payment_deletion.html)メソッドに変数`selected_budgetbook`を渡し、処理を依頼します。
    - 選択が「戻る」の場合、無限ループを抜けます。
- 選択が無効な場合、'無効な選択です。'と表示します。

### 使用例:
```python
display = BudgetDisplay()
selected_budgetbook = "家計簿名"
display.display_budgetbook_menu(selected_budgetbook)
