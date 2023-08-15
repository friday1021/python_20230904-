# クラス: BudgetDisplay

## 説明:
家計簿の情報を表示するためのクラスです。`DisplayManager`クラスと`MenuDisplay`クラスを継承しています。

## メソッド名: display_budgetbook_list

### パラメータ:
- self: BudgetDisplay - インスタンス自体

### 戻り値:
- budgetbooks: list - 家計簿の一覧
- choice: int - 選択されたオプション

### 説明:
存在する家計簿の一覧を表示または新しい家計簿を作成するためのメソッドです。

### 処理内容:
- [`get_budgetbooks`](../../../booklet/budgetbook.py/Budgetbookクラス/get_budgetbooks.html)メソッドを呼び出して家計簿の一覧を取得し、返却されたリストを変数`budgetbooks`にセットします。
- 取得した家計簿の一覧が存在する（空でない）場合、[`display_menu`](../../displaymanager.py/MenuDisplayクラス/display_menu.html)メソッドに変数`budgetbooks`を渡し、ユーザーの選択を待ちます。
  - 家計簿を選択した場合、変数`budgetbooks`と`choice`を返します。
  - 0が選択された場合、[`display_create_budgetbook`](./display_create_budgetbook.html)メソッドを呼び出し新しい家計簿を作成を依頼します。
- 家計簿の一覧が存在しない場合、新しい家計簿を作成するかどうかの確認を行います。
  - 作成しない場合、変数`choice`に`999`をセットし変数`budgetbooks`とともに返却します。
  - 作成する場合、新しい家計簿の名前を入力させ、変数`new_book_name`にセットします。
    - [`create_budgetbook`](../../../booklet/budgetbook.py/Budgetbookクラス/create_budgetbook.html)メソッドに変数`new_book_name`を渡し新しい家計簿を作成します。
    - 作成に成功した場合、[`get_budgetbooks`](../../../booklet/budgetbook.py/Budgetbookクラス/get_budgetbooks.html)メソッドを呼び出し変数`budgetbooks`を更新します。
    - 変数`choice`に`1`をセットし作成した変数`budgetbooks`と`choice`を返却します。

### 使用例:
```python
display = BudgetDisplay()
budgetbooks, choice = display.display_budgetbook_list()
