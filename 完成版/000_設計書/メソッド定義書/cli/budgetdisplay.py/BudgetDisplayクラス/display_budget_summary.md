# クラス: BudgetDisplay

## 説明:
家計簿の情報を表示するためのクラスです。`DisplayManager`クラスと`MenuDisplay`クラスを継承しています。

## メソッド名: display_budget_summary

### パラメータ:
- self: BudgetDisplay - インスタンス自体
- budget_info: list - 家計簿情報のリスト（[テーブルbudgetbooksの1列目,テーブルbudgetbooksの2列目...]）

### 戻り値:None

### 説明:
家計簿のサマリ情報を表示するためのメソッドです。

### 処理内容:
- 家計簿情報のリストから、選択された家計簿名、作成日時、更新日時を取り出します。
- 選択された家計簿名と日時情報を含むヘッダを表示します。
- [`calculate_total_income`](../../../booklet/budgetbook.py/Budgetbookクラス/calculate_total_income.html)メソッドを呼び出し、返却された家計簿の収入合計を変数`total_income`へセットします。
- [`calculate_total_payment`](../../../booklet/budgetbook.py/Budgetbookクラス/calculate_total_payment.html)メソッドを呼び出し、返却された家計簿の収入合計を変数`total_payment`へセットします。
- `total_income` - `total_payment`で現在の資産を計算し、表示します。

### 使用例:
```python
display = BudgetDisplay()
budget_info = ["家計簿名", "家計簿の情報", "作成日時", "更新日時"]
display.display_budget_summary(budget_info)
