# クラス: BudgetDisplay

## 説明:
家計簿の情報を表示するためのクラスです。`DisplayManager`クラスと`MenuDisplay`クラスを継承しています。

## メソッド名: display_choose_option

### パラメータ:
- self: BudgetDisplay - インスタンス自体

### 戻り値:
- choice: int - 選択された機能の番号

### 説明:
機能を選択するためのメソッドです。ユーザーに選択肢を表示し、入力を受け付けます。

### 処理内容:
- 無限ループ内で、ユーザーの選択を受け付けるために入力を待ちます。
- 入力された値を整数に変換し、選択肢の番号として変数`choice`にセットします。
- もし入力が整数でない場合、ValueError例外が発生します。この場合、エラーメッセージを表示し、0.5秒待機します。
- 整数が正しく入力された場合、変数`choice`を戻り値として返します。

### 使用例:
```python
display = BudgetDisplay()
selected_option = display.display_choose_option()
print("選択された機能の番号:", selected_option)
