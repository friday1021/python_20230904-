# クラス: BudgetBook

## 説明:
家計簿の記録と管理を行うクラスです。

## メソッド名: \_\_init\_\_
### パラメータ:
- self: BudgetBook - インスタンス自体
### 戻り値:
なし
### 説明:
BudgetBookクラスのコンストラクタです。データベースへの接続を確立します。
### 処理内容:
- データベース名を "mydatabase.db" として設定します。
- SqlManagerクラスのインスタンスを作成し、sql_manager属性に格納します。

#### 使用例:
```python
budget = BudgetBook()
