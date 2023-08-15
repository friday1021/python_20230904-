import sqlite3
from typing import Optional
class SqlManager:
    '''
    データベースとの接続、実行を行う
    '''
    def __init__(self, db_name) -> None:
        '''
        初期処理
        '''
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('PRAGMA foreign_keys = ON;')
        self.cursor = self.connection.cursor()
        self.create_tables()
            
    def create_tables(self) -> None:
        '''
        テーブル作成クエリを発行し、実行メソッドに投げる
        '''

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
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY,
            budgetbooks_id INTEGER,
            amount INTEGER,
            category TEXT,
            notes TEXT,
            created_at DATETIME,
            updated_at DATETIME,
            FOREIGN KEY (budgetbooks_id) REFERENCES budgetbooks (id) ON DELETE CASCADE
        );
        '''

        self.cursor.execute(create_budgetbooks_table)
        self.cursor.execute(create_incomes_table)
        self.cursor.execute(create_payments_table)
        self.connection.commit()
    
    def execute_query(self, query, values=None) -> bool:
        '''
        受け取ったクエリを実行する
        '''
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def fetch_one(self, query, values=None) -> Optional[tuple]:
        '''
        クエリを実行し、結果の1行を返却する
        エラーの場合はNoneを返却する
        '''
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print("Error fetching one:", e)
            return None
    
    def fetch_all(self, query, values=None) -> Optional[list]:
        '''
        クエリを実行し、結果の全行を返却する
        エラーの場合はNoneを返却する
        '''
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print("Error fetching all:", e)
            return None
