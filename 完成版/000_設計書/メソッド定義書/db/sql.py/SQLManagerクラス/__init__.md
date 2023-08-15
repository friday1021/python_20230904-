## クラス: SqlManager

### 説明:
データベースとの接続とクエリ実行を行うためのクラスです。

### メソッド:
### メソッド名: \_\_init\_\_
#### パラメータ:
- self: SqlManager - インスタンス自体
- db_name: str - データベースのファイル名

#### 戻り値: なし

#### 説明:
データベースへの接続を確立し、初期処理として外部キー制約を有効化した上でテーブルを作成します。
外部キー制約が有効化された状態で、データベース内にテーブルを作成するためのメソッドです。

```python
class SqlManager:
    '''
    データベースとの接続、実行を行う
    '''

    def __init__(self, db_name) -> None:
        '''
        初期処理としてデータベースと接続を行う
        '''
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('PRAGMA foreign_keys = ON;')
        self.cursor = self.connection.cursor()
        self.create_tables()
