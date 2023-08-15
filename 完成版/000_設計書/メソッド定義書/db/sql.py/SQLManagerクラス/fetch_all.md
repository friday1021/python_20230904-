# クラス: SqlManager

## 説明:

データベースとの接続とクエリ実行を行うためのクラスです。

## メソッド名: fetch_all

### パラメータ:

- self: SqlManager - インスタンス自体
- query: str - 実行するSQLクエリ
- values: tuple - クエリ内のプレースホルダに対応する値 (デフォルト: None)

### 戻り値:

- result: list - クエリの実行結果の全行データのリスト (各行がカラムごとのタプル形式)

### 説明:

指定されたSQLクエリを実行し、結果の全行を取得するためのメソッドです。

### 処理内容:

- クエリを実行し、指定された値がある場合はプレースホルダに対応する値を使用してクエリを実行します。
- クエリの実行結果の全行データをリストとして取得して返します。取得できない場合はNoneを返します。

### 使用例:
```python
sql_manager = SqlManager('my_database.db')
query = "SELECT column1, column2 FROM table_name WHERE condition_column = ?;"
values = ('condition_value',)
results = sql_manager.fetch_all(query, values)
if results:
    for result in results:
        print('クエリの実行結果:', result)
else:
    print('結果がありません。')
```

### 文法解説

`self.cursor.execute(query, values)` - プレースホルダに対応する値(values)を使用して実行

`self.cursor.execute(query)` - プレースホルダのない場合の実行

`self.connection.commit()` - クエリ実行結果をコミット（確定）
