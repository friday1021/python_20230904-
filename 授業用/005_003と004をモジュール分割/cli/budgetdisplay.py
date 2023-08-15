try:
    import time, sys
except ImportError as e:
    print(e)
    sys.exit()

class BudgetDisplay():
    '''
    家計簿の情報を表示するためのクラス
    '''
    
    def __init__(self) -> None:
        '''
        初期処理
        '''
        pass


    def display_choose_option(self) -> str:
        '''
        機能選択
        '''
        pass


    def display_budget_summary(self, budget_info) -> None:
        '''
        家計簿のサマリ表示
        '''
        pass
    

    def display_budget(self, selected_budgetbook) -> None:
        '''
        家計簿の一覧を画面表示する
        '''
        pass


    def display_incomes(self, selected_budgetbook) -> None:
        '''
        収入を表示
        '''
        pass


    def display_payments(self, selected_budgetbook) -> None:
        '''
        支出を表示
        '''
        pass
            

    def display_income_details(self, selected_budgetbook) -> None:
        '''
        収入詳細を表示
        '''
        pass


    def display_payment_details(self, selected_budgetbook) -> None:
        '''
        支出詳細を表示
        '''
        pass

    
    def display_budgetbook_menu(self, selected_budgetbook) -> None:
        '''
        家計簿の操作可能内容を表示
        '''
        pass


    def display_top_menu(self) -> None:
        '''
        トップメニューを表示
        '''
        pass
            

    def display_create_budgetbook(self) -> None:
        '''
        新しい家計簿の情報を決め、クエリ実行メソッドに投げる
        '''
        pass


    def display_budgetbook_list(self) -> tuple:
        '''
        存在する家計簿の一覧を表示
        家計簿がない時は新しい家計簿を作成
        '''
        pass