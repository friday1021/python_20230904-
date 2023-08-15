import time
from booklet.budgetbook import BudgetBook
from cli.displaymanager import DisplayManager, MenuDisplay

class BudgetDisplay(DisplayManager, MenuDisplay):
    '''
    家計簿の情報を表示するためのクラス
    '''
    
    def __init__(self) -> None:
        # BudgetBookをインスタンス化
        self.budget = BudgetBook()


    def display_choose_option(self) -> int:
        '''
        機能選択
        '''

        while True:
            try:
                choice = int(input('選択 >>'))
            except ValueError as e:
                print('半角で入力してください。')
                time.sleep(0.5)
            else:
                return choice


    def display_budget_summary(self, budget_info) -> None:
        '''
        家計簿のサマリ表示
        '''
        
        # 項目ごとの値を取り出す
        selected_budgetbook = budget_info[1]
        created_at = budget_info[2]
        updated_at = budget_info[3]

        # ヘッダ表示
        print(f'{selected_budgetbook} の家計簿:')
        print('-' * 40)
        print(f'作成日時: {created_at}')
        print(f'更新日時: {updated_at}')

        # 資産を集計して表示
        total_income = self.budget.calculate_total_income(selected_budgetbook)
        total_payment = self.budget.calculate_total_payment(selected_budgetbook)
        current_assets = total_income - total_payment
        print(f'現在の資産: {current_assets}円')


    def display_budget(self, selected_budgetbook) -> None:
        '''
        家計簿の一覧を画面表示する
        '''
        
        # クエリをセットしてデータ取得
        query = "SELECT * FROM budgetbooks WHERE book_name = ?;"
        values = (selected_budgetbook,)
        result = self.budget.sql_manager.fetch_one(query, values)

        if result:
            # データが存在したらそれぞれを表示
            self.display_budget_summary(result) # ヘッダ
            self.display_income_details(values) # 収入
            self.display_payment_details(values) # 支出
        else:
            print('家計簿が存在しません。')


    def display_incomes(self, selected_budgetbook) -> None:
        '''
        収入を表示
        '''

        # クエリをセットしてデータ取得
        query = "SELECT amount, created_at FROM incomes WHERE budgetbooks_id = (SELECT id FROM budgetbooks WHERE book_name = ?);"
        values = (selected_budgetbook,)
        incomes = self.budget.sql_manager.fetch_all(query, values)
        
        if incomes:
            # データが存在したら全てを一覧表示
            print(f'{selected_budgetbook} の収入:')
            for income in incomes:
                amount, created_at = income
                print(f'金額: {amount}, 日付: {created_at}')
        else:
            print(f'{selected_budgetbook} の収入はありません。')


    def display_payments(self, selected_budgetbook) -> None:
        '''
        支出を表示
        '''

        # クエリをセットしてデータ取得
        query = "SELECT amount, created_at FROM payments WHERE budgetbooks_id = (SELECT id FROM budgetbooks WHERE book_name = ?);"
        values = (selected_budgetbook,)
        payments = self.budget.sql_manager.fetch_all(query, values)
        
        if payments:
            # データが存在したら全てを一覧表示
            print(f'{selected_budgetbook} の支出:')
            for payment in payments:
                amount, created_at = payment
                print(f'金額: {amount}, 日付: {created_at}')
        else:
            print(f'{selected_budgetbook} の支出はありません。')
            

    def display_income_details(self, selected_budgetbook) -> None:
        '''
        収入詳細を表示
        '''

        # ヘッダ表示
        print('\n収入:')
        print("-" * 80)
        print(f'{self.adjust_width_for_fullwidth("金額", 10)} | {self.adjust_width_for_fullwidth("収入源", 15)} | {self.adjust_width_for_fullwidth("ノート", 20)} | {self.adjust_width_for_fullwidth("日時", 20)}')
        print("-" * 80)

        # クエリを作成して実行モジュールに投げる
        income_details_query = "SELECT amount, source, notes, created_at FROM incomes WHERE budgetbooks_id = (SELECT id FROM budgetbooks WHERE book_name = ?);"
        incomes = self.budget.sql_manager.fetch_all(income_details_query, selected_budgetbook)

        # 取得結果を画面に表示
        for income in incomes:
            # None 値を空文字に置き換え
            amount, source, notes, created_at = income
            source = source if source else ''
            notes = notes if notes else ''
            # 整形して表示
            print(f'{amount:<10} | {self.adjust_width_for_fullwidth(source, 15)} | {self.adjust_width_for_fullwidth(notes, 20)} | {created_at:<20}')


    def display_payment_details(self, selected_budgetbook) -> None:
        '''
        支出詳細を表示
        '''

        # ヘッダ表示
        print('\n支出:')
        print("-" * 80)
        print(f'{self.adjust_width_for_fullwidth("金額", 10)} | {self.adjust_width_for_fullwidth("収入源", 15)} | {self.adjust_width_for_fullwidth("ノート", 20)} | {self.adjust_width_for_fullwidth("日時", 20)}')
        print("-" * 80)

        # クエリを作成して実行モジュールに投げる
        payment_details_query = "SELECT amount, category, notes, created_at FROM payments WHERE budgetbooks_id = (SELECT id FROM budgetbooks WHERE book_name = ?);"
        payments = self.budget.sql_manager.fetch_all(payment_details_query, selected_budgetbook)

        # 取得結果を画面に表示
        for payment in payments:
            # None 値を空文字に置き換え
            amount, category, notes, created_at = payment
            category = category if category else ''
            notes = notes if notes else ''
            # 整形して表示
            print(f'{amount:<10} | {self.adjust_width_for_fullwidth(category, 15)} | {self.adjust_width_for_fullwidth(notes, 20)} | {created_at:<20}')

    
    def display_budgetbook_menu(self, selected_budgetbook) -> None:
        '''
        家計簿の操作可能内容を表示
        '''
        
        # 家計簿に何をするか選択
        while True:
            try:
                print(self.get_border())  # 罫線を描画
                print('機能を選択してください↓')

                # 家計簿メニューオプションのリストを表示
                budgetbook_menu = self.get_budgetbook_menu()
                self.display_menu(budgetbook_menu)

                print(self.get_border())  # 罫線を描画
                choice_budgetbook_menu = self.display_choose_option()

                if 1 <= choice_budgetbook_menu <= len(budgetbook_menu):
                    # 選択した機能を取得
                    menu_option = budgetbook_menu[choice_budgetbook_menu - 1]

                    # 機能ごとのメソッドを呼ぶ
                    if menu_option == '表示':
                        self.display_budget(selected_budgetbook)
                    elif menu_option == '記録':
                        self.budget.record_budget(selected_budgetbook)
                    elif menu_option == 'この家計簿を削除':
                        if self.budget.delete_budget(selected_budgetbook) == True:
                            break
                    elif menu_option == '収入/支出の削除':
                        self.budget.handle_income_or_payment_deletion(selected_budgetbook)
                    else:
                        break  # 前のメニューに戻る
                else:
                    print('無効な選択です。')
            except ValueError as e:
                print('半角で入力してください。', e)
                time.sleep(0.5)
            finally:
                input('続行するにはEnterキーを押してください >>')


    def display_top_menu(self) -> None:
        '''
        トップメニューを表示
        '''        

        print(self.get_border()) # 罫線を引く
        print('機能を選択してください↓')

        # 機能の一覧を取得して表示
        menu_list = self.get_top_menu()
        self.display_menu(menu_list)

        print(self.get_border()) # 罫線を引く
        return None
            

    def display_create_budgetbook(self) -> None:
        '''
        新しい家計簿の情報を決め、クエリ実行メソッドに投げる
        '''
        while True:
            # 家計簿の名前を決める
            new_book_name = input('新しい家計簿の名前を入力してください: ')
            if new_book_name:
                if self.budget.create_budgetbook(new_book_name):  # 新しい家計簿を作成
                    print(f'新しい家計簿「{new_book_name}」を作成しました。')
                    break
                else:
                    print('家計簿の作成に失敗しました。もう一度試してください。')
            else:
                print('無効な名前です。もう一度入力してください。')


    def display_budgetbook_list(self) -> tuple:
        '''
        存在する家計簿の一覧を表示
        家計簿がない時は新しい家計簿を作成
        '''

        budgetbooks = self.budget.get_budgetbooks()  # 家計簿の一覧を取得

        if budgetbooks:
            # 新しい家計簿を作成する選択肢を表示
            print('存在する家計簿一覧:')

            # メニュー表示
            time.sleep(0.5)
            self.display_menu(budgetbooks)
            time.sleep(0.5)

            # 0は新規作成
            print('0: 新しい家計簿を作成')
            print('999: 終了')

            # ユーザーの選択を取得
            choice = input('選択してください (番号): ')

            try:
                choice = int(choice)
                if 1 <= choice <= len(budgetbooks):
                    # 家計簿を選択した場合の処理
                    return (budgetbooks, choice)
                elif choice == 0:
                    # 家計簿作成用メソッドを呼び出す
                    self.display_create_budgetbook()
            except ValueError:
                print('無効な入力です。正しい番号を入力してください。')
        else:
            # 家計簿がひとつもなかった場合
            qcreate = input('存在する家計簿はありません。新しい家計簿を作成しますか？(y/n)')
            if qcreate != 'y':
                choice = 999
                return (budgetbooks, choice)

            while True:
                # 名前を決める
                new_book_name = input('新しい家計簿の名前を入力してください: ')
                if new_book_name:
                    if self.budget.create_budgetbook(new_book_name):  # 新しい家計簿を作成
                        print(f'新しい家計簿「{new_book_name}」を作成しました。')
                        budgetbooks = self.budget.get_budgetbooks()  # 家計簿の一覧を取得
                        choice = 1
                        return (budgetbooks, choice)
                    else:
                        print('家計簿の作成に失敗しました。もう一度試してください。')
                else:
                    print('無効な名前です。もう一度入力してください。')
        return (budgetbooks, choice)
