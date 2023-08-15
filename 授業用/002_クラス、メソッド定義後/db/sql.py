from typing import Optional
class SqlManager:
    '''
    データベースとの接続、実行を行う
    '''
    def __init__(self, db_name) -> None:
        '''
        初期処理
        '''
        pass

            
    def create_tables(self) -> None:
        '''
        テーブル作成クエリを発行し、実行メソッドに投げる
        '''
        pass

    
    def execute_query(self, query, values=None) -> bool:
        '''
        受け取ったクエリを実行する
        '''
        pass

    
    def fetch_one(self, query, values=None) -> Optional[tuple]:
        '''
        クエリを実行し、結果の1行を返却する
        エラーの場合はNoneを返却する
        '''
        pass

    
    def fetch_all(self, query, values=None) -> Optional[list]:
        '''
        クエリを実行し、結果の全行を返却する
        エラーの場合はNoneを返却する
        '''
        pass

