# クラス: SqlManager

## 説明:

データベースとの接続とクエリ実行を行うためのクラスです。

## メソッド名: execute_query

### パラメータ:

- self: SqlManager - インスタンス自体
- query: str - 実行するSQLクエリ
- values: tuple - クエリ内のプレースホルダに対応する値 (デフォルト: None)

### 戻り値:

- bool: クエリの実行が成功したかどうかを示すブール値

### 説明:

指定されたSQLクエリを実行するためのメソッドです。

### 処理内容:

- クエリを実行し、指定された値がある場合はプレースホルダに対応する値を使用してクエリを実行します。
- クエリの実行結果をコミットしてデータベースに反映します。
- クエリの実行が成功した場合はTrueを返し、失敗した場合はエラーメッセージを表示してFalseを返します。

### 使用例:

```python
sql_manager = SqlManager('my_database.db')
query = "INSERT INTO table_name (column1, column2) VALUES (?, ?);"
values = ('value1', 'value2')
success = sql_manager.execute_query(query, values)
if success:
    print('クエリの実行が成功しました。')
else:
    print('クエリの実行に失敗しました。')
```

### 文法解説

`self.cursor.execute(query, values)` - プレースホルダに対応する値(values)を使用して実行

`self.cursor.execute(query)` - プレースホルダのない場合の実行

`self.connection.commit()` - クエリ実行結果をコミット（確定）
