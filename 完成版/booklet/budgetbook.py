try:
    import sys
    from typing import Optional
except ImportError as e:
    print(e)
    sys.exit()

try:
    from db.sql import SqlManager
except ImportError as e:
    print(e)
    sys.exit()


class BudgetBook:
    '''
    家計簿の記録と管理を行うクラス
    '''

    def __init__(self) -> None:
        # データベースと接続
        db_name = "mydatabase.db"
        self.sql_manager = SqlManager(db_name)


    def adjust_width_for_fullwidth(self, s, desired_width) -> str:
        '''
        日本語等の全角文字をカウントして字幅を調整する
        '''
        # 全角文字の数をカウント
        count_fullwidth = sum([1 for c in s if '\u4e00' <= c <= '\u9fff' or '\u3040' <= c <= '\u30ff' or '\uff01' <= c <= '\uff5e'])

        # 全角文字の数に基づいて幅を調整
        adjusted_width = desired_width - count_fullwidth
        return f"{s:<{adjusted_width}}"


    def calculate_total_income(self, selected_budgetbook) -> int:
        '''
        収入の合計金額を集計する
        '''
        # データベースから収入を取得するクエリを作成
        income_query = "SELECT SUM(amount) FROM incomes WHERE budgetbooks_id = (SELECT id FROM budgetbooks WHERE book_name = ?);"
        total_income = self.sql_manager.fetch_one(income_query, (selected_budgetbook,))

        # 収入が1つでもあれば集計結果を返す（なければ0）
        return total_income[0] if total_income and total_income[0] else 0


    def calculate_total_payment(self, selected_budgetbook) -> int:
        '''
        支出の合計金額を集計する
        '''

        # データベースから支出を取得するクエリを作成
        payment_query = "SELECT SUM(amount) FROM payments WHERE budgetbooks_id = (SELECT id FROM budgetbooks WHERE book_name = ?);"
        total_payment = self.sql_manager.fetch_one(payment_query, (selected_budgetbook,))

        # 支出が1つでもあれば集計結果を返す（なければ0）
        return total_payment[0] if total_payment and total_payment[0] else 0


    def record_budget(self, selected_budgetbook) -> None:
        '''
        家計簿への記録
        '''

        # 収入か支出の金額を入力させる
        record_type = input('収入/支出を選択してください (income/payment): ')
        amount = int(input('金額を入力してください: '))
        
        # 共通で使用するカラム
        common_columns = "(budgetbooks_id, amount, created_at, updated_at"
        common_values = "((SELECT id FROM budgetbooks WHERE book_name = ?), ?, datetime('now', '+9 hours'), datetime('now', '+9 hours')"

        # 収入の場合の詳細入力
        if record_type == 'income':
            source = input('収入源を入力してください: ')
            notes = input('ノートを入力してください (任意): ')
            
            # SQLのカラムとバリュー部分を追加する
            query = f"INSERT INTO incomes {common_columns}, source, notes) VALUES {common_values}, ?, ?);"
            values = (selected_budgetbook, amount, source, notes)

        # 支出の場合の詳細入力
        elif record_type == 'payment':
            category = input('カテゴリーを入力してください: ')
            notes = input('ノートを入力してください (任意): ')

            # SQLのカラムとバリュー部分を追加する
            query = f"INSERT INTO payments {common_columns}, category, notes) VALUES {common_values}, ?, ?);"
            values = (selected_budgetbook, amount, category, notes)
            
        else:
            print('無効な選択です。')
            return

        # クエリを投げて結果を表示
        if self.sql_manager.execute_query(query, values):
            print('記録が完了しました。')
        else:
            print('記録に失敗しました。')

    # 
    def delete_budget(self, selected_budgetbook) -> bool:
        '''
        家計簿の削除
        '''

        # 確認メッセージ表示
        confirm = input(f'{selected_budgetbook} を削除しますか？ (y/n): ')
        
        if confirm.lower() == 'y':
            # yなら削除用クエリを生成して投げる
            query = "DELETE FROM budgetbooks WHERE book_name = ?;"
            values = (selected_budgetbook,)

            if self.sql_manager.execute_query(query, values):
                # 成功時
                print(f'{selected_budgetbook} を削除しました。')
                return True
            else:
                # 失敗時
                print('削除に失敗しました。')
        return False


    def handle_income_or_payment_deletion(self, selected_budgetbook) -> None:
        '''
        削除対象の操作
        '''
        
        # 削除がする対象を確認
        record_type = input('削除する収入または支出を選択してください (income/payment): ')
        record_id = self.select_record(selected_budgetbook, record_type)
        
        if record_id:
            # データが1つでもあれば削除要求
            self.delete_record(record_type, record_id)
    

    def get_budgetbooks(self) -> list:
        '''
        存在する家計簿の一覧を取得
        '''

        # クエリをセット
        query = "SELECT book_name FROM budgetbooks;"
        result = self.sql_manager.fetch_all(query)

        if result:
            # 家計簿のリストを生成して返す
            return [row[0] for row in result]
        else:
            # 家計簿がないならからリストを返す
            return []


    def create_budgetbook(self, book_name) -> bool:
        '''
        新しい家計簿を作成
        '''

        # クエリをセット
        query = "INSERT INTO budgetbooks (book_name, created_at, updated_at) VALUES (?, datetime('now'), datetime('now'));"
        values = (book_name,)

        # クエリを投げて結果を返却
        return self.sql_manager.execute_query(query, values)


    def select_record(self, selected_budgetbook, record_type) -> Optional[int]:
        '''
        一覧から収入または支出を選択
        '''

        # 対象の家計簿の選択された方のテーブルからデータを取得
        if record_type == 'income':
            query = "SELECT id, amount, created_at FROM incomes WHERE budgetbooks_id = (SELECT id FROM budgetbooks WHERE book_name = ?);"
        else:
            query = "SELECT id, amount, created_at FROM payments WHERE budgetbooks_id = (SELECT id FROM budgetbooks WHERE book_name = ?);"
        values = (selected_budgetbook,)
        
        # クエリを投げて結果を受け取る
        records = self.sql_manager.fetch_all(query, values)

        # 登録がない場合中断
        if not records:
            print(f'{selected_budgetbook} の{record_type}はありません。')
            return None

        # 一覧表示
        for index, (record_id, amount, created_at) in enumerate(records, start=1):
            print(f'{index}. 金額: {amount}, 日付: {created_at}')

        # 正しく選ばれるまで繰り返す
        while True:
            try:
                choice = int(input('削除する項目を選択してください: '))
                
                if 1 <= choice <= len(records):
                    # 選択された項目の主キー（ID）を取り出して返す
                    return records[choice - 1][0]
                else:
                    print('無効な選択です。')
            except ValueError:
                print('半角で入力してください。')


    def delete_record(self, record_type, record_id) -> None:
        '''
        収入または支出の削除
        '''

        # 対象のテーブルを特定してクエリをセット
        if record_type == 'income':
            query = "DELETE FROM incomes WHERE id = ?;"
        else:
            query = "DELETE FROM payments WHERE id = ?;"
        values = (record_id,)
        
        # クエリを実行
        if self.sql_manager.execute_query(query, values):
            print(f'{record_type}を削除しました。')
        else:
            print('削除に失敗しました。')
