# クラス: DisplayManager

## メソッド名: get_budgetbook_menu

### パラメータ:
- self: DisplayManager - インスタンス自体

### 戻り値:
- letter: list - 家計簿メニューの一覧文字列のリスト

### 説明:
家計簿メニューの一覧文字列を取得するためのメソッドです。

### 処理内容:
- 家計簿メニューの一覧文字列をリストとして定義して返します。

### 使用例:
```python
display_manager = DisplayManager()
budgetbook_menu = display_manager.get_budgetbook_menu()
print(budgetbook_menu)
# -出力例-
# ['表示', '記録', '収入/支出の削除', 'この家計簿を削除', '戻る']
