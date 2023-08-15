# クラス: BudgetDisplay

## 説明:
家計簿の情報を表示するためのクラスです。`DisplayManager`クラスと`MenuDisplay`クラスを継承しています。

### メソッド:
### メソッド名: \_\_init\_\_
#### パラメータ:
- self: BudgetDisplay - インスタンス自体

#### 戻り値: なし

#### 説明:
- BudgetDisplayクラスのインスタンスを初期化します。
- BudgetBookクラスのインスタンスを生成して、インスタンス変数`budget`として保持し、家計簿の情報を取得できるようにします。

```python
class BudgetDisplay(DisplayManager, MenuDisplay):
    '''
    家計簿の情報を表示するためのクラス
    '''
    
    def __init__(self) -> None:
        # BudgetBookをインスタンス化
        self.budget = BudgetBook()
