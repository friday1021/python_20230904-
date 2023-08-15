## クラス: SqlManager

### 説明:
データベースとの接続とクエリ実行を行うためのクラスです。

## メソッド名: create_tables

### パラメータ:
- self: SqlManager - インスタンス自体

### 戻り値:
なし

### 説明:
テーブルを作成するためのメソッドです。`budgetbooks`テーブル、`incomes`テーブル、および`payments`テーブルを作成します。

### 処理内容:
- `budgetbooks`テーブルの定義クエリを作成して変数`create_budgetbooks_table`にセットします。
- `self.cursor.execute(create_budgetbooks_table)`でクエリを実行します。
- `incomes`テーブルの定義クエリを作成して変数`create_incomes_table`にセットします。外部キー制約として`budgetbooks_id`が`budgetbooks`テーブルの`id`を参照しており、`ON DELETE CASCADE`で削除時の動作を指定しています。
- `self.cursor.execute(create_incomes_table)`でクエリを実行します。
- `payments`テーブルの定義クエリを作成して変数`create_payments_table`にセットします。外部キー制約として`budgetbooks_id`が`budgetbooks`テーブルの`id`を参照しており、`ON DELETE CASCADE`で削除時の動作を指定しています。
- `self.cursor.execute(create_payments_table)`でクエリを実行します。
- 実行したクエリの結果をコミットしてデータベースに反映します。
  - `self.connection.commit()`でコミットします。

### 使用例:
```python
sql_manager = SqlManager('my_database.db')
sql_manager.create_tables()
```

#### クエリ例

```python
# budgetbooksテーブルの定義
create_budgetbooks_table = '''
CREATE TABLE IF NOT EXISTS budgetbooks (
    id INTEGER PRIMARY KEY,
    book_name TEXT,
    created_at DATETIME,
    updated_at DATETIME
);
'''

# incomesテーブルの定義
create_incomes_table = '''
CREATE TABLE IF NOT EXISTS incomes (
    id INTEGER PRIMARY KEY,
    budgetbooks_id INTEGER,
    amount INTEGER,
    source TEXT,
    notes TEXT,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (budgetbooks_id) REFERENCES budgetbooks (id) ON DELETE CASCADE
);
'''

# paymentsテーブルの定義
create_payments_table = '''
    自分で作成
);
'''
```