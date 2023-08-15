# クラス名: CLIApp

## メソッド名: run
### パラメータ:
- self: CLIApp - インスタンス自体

### 戻り値: なし

### 説明:
CLIアプリケーションを実行するためのメソッドです。

### 処理内容:
- [`display_top_menu`](../../cli/budgetdisplay.py/BudgetDisplayクラス/display_top_menu.html)メソッドを呼び出して機能一覧を表示します。
- [`display_choose_option`](../../cli/budgetdisplay.py/BudgetDisplayクラス/display_choose_option.html)メソッドを呼び出して機能を選択させます。
- 選択した機能に応じて処理を行います。具体的な処理は以下の通りです。
  - 選択が1の場合:
    - [`display_budgetbook_list`](../../cli/budgetdisplay.py/BudgetDisplayクラス/display_budgetbook_list.html)メソッドを呼び出して家計簿を選択させ、返却された値を変数`budgetbooks`と`choice_budgetbook`に保持します。
    - 変数`choice_budgetbook`が999の場合、終了します。
    - 変数`choice_budgetbook`が1以上の場合、選択された家計簿の名前を取得して表示します。
  - `choice_budgetbook`が0の場合:
    - 新しい家計簿を作成します。
  - その他の選択:
    - 無効な選択ですと表示します。

### 使用例:
```python
app = CLIApp()
app.run()
```
## 変数定義書

### 変数名: 変数の説明
- **型**: 変数のデータ型
- **初期値**: 変数の初期値（ある場合）
- **使用方法**: 変数がどのように使用されるかの説明
