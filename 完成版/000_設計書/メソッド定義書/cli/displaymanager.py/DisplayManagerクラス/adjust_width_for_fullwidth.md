# クラス: DisplayManager

## メソッド名: adjust_width_for_fullwidth

### パラメータ:
- self: DisplayManager - インスタンス自体
- s: str - 調整する文字列
- desired_width: int - 望む表示幅

### 戻り値:
- adjusted_string: str - 調整された幅に合わせた文字列

### 説明:
全角文字を考慮した文字列の表示幅を調整するためのメソッドです。

### 処理内容:
- 引数として渡された文字列`s`内の全角文字の数を数え、その数を用いて表示幅を算出します。
- 望む表示幅`desired_width`から全角文字の数を差し引いた調整後の幅を計算します。
- 調整後の幅に合わせて文字列`s`を左寄せして調整し、調整された文字列を返します。

### 使用例:
```python
display_manager = DisplayManager()
adjusted_string = display_manager.adjust_width_for_fullwidth("日本語abc", 15)
print(adjusted_string)  # '日本語abc    '
