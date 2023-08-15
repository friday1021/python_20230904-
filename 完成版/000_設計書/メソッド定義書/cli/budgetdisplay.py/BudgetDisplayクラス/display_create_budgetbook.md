# クラス: BudgetDisplay

## 説明:
家計簿の情報を表示するためのクラスです。`DisplayManager`クラスと`MenuDisplay`クラスを継承しています。

## メソッド名: display_create_budgetbook

### パラメータ:
- self: BudgetDisplay - インスタンス自体

### 戻り値:
なし

### 説明:
新しい家計簿の情報を決定し、クエリ実行メソッドに投げるためのメソッドです。

### 処理内容:
- 無限ループ内で、新しい家計簿の名前をユーザーに入力させ、変数`new_book_name`にセットします。
- 入力された名前が有効な場合、新しい家計簿を作成します。
  - [`create_budgetbook`](../../../booklet/budgetbook.py/Budgetbookクラス/create_budgetbook.html)メソッドに変数`new_book_name`を渡して新しい家計簿を作成し、成功した場合はメッセージを表示してループを終了します。
  - 作成に失敗した場合はエラーメッセージを表示します。
- 入力された名前が無効な場合、'無効な名前です。もう一度入力してください。'と表示します。

### 使用例:
```python
display = BudgetDisplay()
display.display_create_budgetbook()
