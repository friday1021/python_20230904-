try:
    import sys
    from typing import Optional
except ImportError as e:
    print(e)
    sys.exit()


class BudgetBook:
    '''
    家計簿の記録と管理を行うクラス
    '''

    def __init__(self) -> None:
        '''
        初期処理
        '''
        pass


    def adjust_width_for_fullwidth(self, s, desired_width) -> str:
        '''
        日本語等の全角文字をカウントして字幅を調整する
        '''
        pass


    def calculate_total_income(self, selected_budgetbook) -> int:
        '''
        収入の合計金額を集計する
        '''
        pass


    def calculate_total_payment(self, selected_budgetbook) -> int:
        '''
        支出の合計金額を集計する
        '''
        pass


    def record_budget(self, selected_budgetbook) -> None:
        '''
        家計簿への記録
        '''
        pass

    # 
    def delete_budget(self, selected_budgetbook) -> bool:
        '''
        家計簿の削除
        '''
        pass


    def handle_income_or_payment_deletion(self, selected_budgetbook) -> None:
        '''
        削除対象の操作
        '''
        pass
    

    def get_budgetbooks(self) -> list:
        '''
        存在する家計簿の一覧を取得
        '''
        pass


    def create_budgetbook(self, book_name) -> bool:
        '''
        新しい家計簿を作成
        '''
        pass


    def select_record(self, selected_budgetbook, record_type) -> Optional[int]:
        '''
        一覧から収入または支出を選択
        '''
        pass


    def delete_record(self, record_type, record_id) -> None:
        '''
        収入または支出の削除
        '''
        pass