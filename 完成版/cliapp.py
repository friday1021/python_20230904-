try:
    import sys
except ImportError as e:
    print(e)
    sys.exit()

try:
    from general.bot import Bot
    from cli.budgetdisplay import BudgetDisplay
except ImportError as e:
    print(e)
    print('ユーザ定義モジュールの読み込みに失敗しました。')
    sys.exit()

class CLIApp():
    '''
    コマンドラインインターフェースを提供するクラス
    '''
    def __init__(self) -> None:
        # アプリ起動時の挨拶を表示
        print(Bot().greeting())
        self.disp = BudgetDisplay()
        

    def run(self) -> None:

        # トップメニューから機能を選択
        self.disp.display_top_menu()
        choice = self.disp.display_choose_option()

        if choice == 1:
            while True:
                # 家計簿の一覧を表示し、選択させる
                budgetbooks, choice_budgetbook = self.disp.display_budgetbook_list()
                if choice_budgetbook == 999:
                    # 999なら終了
                    input('終了します。')
                    break
                try:
                    if choice_budgetbook >= 1 and choice_budgetbook <= len(budgetbooks):
                        # 家計簿が選択されたら家計簿の名前をメニュー画面に渡す
                        selected_budgetbook = budgetbooks[choice_budgetbook - 1]
                        self.disp.display_budgetbook_menu(selected_budgetbook)  # 選択された家計簿のメニューを表示
                    elif choice_budgetbook == 0:
                        # 新規作成後は何もしない
                        pass
                    else:
                        print('無効な選択です。')
                except TypeError as e:
                    print(e)


if __name__ == '__main__':
    app = CLIApp()
    app.run()
        