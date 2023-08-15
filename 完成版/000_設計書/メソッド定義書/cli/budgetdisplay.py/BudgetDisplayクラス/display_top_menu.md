# クラス: BudgetDisplay

## 説明:
家計簿の情報を表示するためのクラスです。`DisplayManager`クラスと`MenuDisplay`クラスを継承しています。

## メソッド名: display_top_menu

### パラメータ:
- self: BudgetDisplay - インスタンス自体

### 戻り値:
- None

### 説明:
トップメニューを表示するためのメソッドです。

### 処理内容:
- トップメニューを表示するために、[`get_border`](../../displaymanager.py/DisplayManagerクラス/get_border.html)メソッドを使用して罫線を引いて表示を区切ります。
- [`get_top_menu`](../../displaymanager.py/DisplayManagerクラス/get_top_menu.html)メソッドで機能の一覧を取得して変数`menu_list`にセットします。
- [`display_menu`](../../displaymanager.py/MenuDisplayクラス/display_menu.html)メソッドに変数`menu_list`を渡し、メニュー画面を表示します。
- [`get_border`](../../displaymanager.py/DisplayManagerクラス/get_border.html)メソッドを使用して罫線を引いて表示を区切り、戻り値として None を返します。

### 使用例:
```python
display = BudgetDisplay()
display.display_top_menu()
