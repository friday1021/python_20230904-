# クラス: DisplayManager

## メソッド名: get_border

### パラメータ:

- self: DisplayManager - インスタンス自体
- line_str: str - 罫線を描画するための文字列 (デフォルト: '-')
- width: int - 罫線の幅 (デフォルト: 80)
- end: str - 罫線の末尾に追加する文字列 (デフォルト: '')

### 戻り値:
- border: str - 罫線の文字列

### 説明:
罫線用文字列を生成して返すためのメソッドです。

## 処理内容:
- `line_str`パラメータで指定された文字列を幅`width`で繰り返して、罫線用文字列を生成します。
- 罫線用文字列の末尾に`end`パラメータで指定された文字列を追加して、最終的な罫線を作成します。

## 使用例:
```python
display_manager = DisplayManager()
border = display_manager.get_border('*', 60, '!')
print(border)
