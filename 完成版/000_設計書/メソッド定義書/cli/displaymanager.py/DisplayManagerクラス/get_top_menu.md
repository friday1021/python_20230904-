# クラス: DisplayManager

## メソッド名: get_top_menu

### パラメータ:
- self: DisplayManager - インスタンス自体

### 戻り値:
- letter: list - トップメニューの一覧文字列のリスト

### 説明:
トップメニューの一覧文字列を取得するためのメソッドです。

### 処理内容:
- トップメニューの一覧文字列をリストとして定義して返します。

### 使用例:
```python
display_manager = DisplayManager()
top_menu = display_manager.get_top_menu()
print(top_menu)  
# -出力例-
# ['家計簿']
