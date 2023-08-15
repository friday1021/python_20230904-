# クラス: SqlManager

## 説明:

データベースとの接続とクエリ実行を行うためのクラスです。

## メソッド名: fetch_one

### パラメータ:

- self: SqlManager - インスタンス自体
- query: str - 実行するSQLクエリ
- values: tuple - クエリ内のプレースホルダに対応する値 (デフォルト: None)

### 戻り値:

- result: tuple - クエリの実行結果の1行データ (カラムごとのタプル形式)

### 説明:

指定されたSQLクエリを実行し、結果の1行を取得するためのメソッドです。

### 処理内容:

- クエリを実行し、指定された値がある場合はプレースホルダに対応する値を使用してクエリを実行します。
- クエリの実行結果の1行データを取得して返します。取得できない場合はNoneを返します。

### 使用例:

```python
sql_manager = SqlManager('my_database.db')
query = "SELECT column1, column2 FROM table_name WHERE condition_column = ?;"
values = ('condition_value',)
result = sql_manager.fetch_one(query, values)
if result:
    print('クエリの実行結果:', result)
else:
    print('結果がありません。')
```

### 文法解説

`self.cursor.execute(query, values)` - プレースホルダに対応する値(values)を使用して実行

`self.cursor.execute(query)` - プレースホルダのない場合の実行

`self.connection.commit()` - クエリ実行結果をコミット（確定）
