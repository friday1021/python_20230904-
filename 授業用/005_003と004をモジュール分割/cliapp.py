from cli.displaymanager import MenuDisplay, DisplayManager
class CLIApp():
    '''
    コマンドラインインターフェースの実行クラス
    '''
    def __init__(self) -> None:
        '''
        初期処理
        1.あいさつ文を表示
        2.必要なクラスのインスタンス化
        '''
        self.menu = MenuDisplay()
        self.disp = DisplayManager()

        
    def run(self) -> None:
        '''
        アプリのエントリポイント
        '''
        # DisplayManagerクラスのget_top_menuメソッドを呼び出す
        # メニュ画面のリストを受け取る
        menu_list = self.disp.get_top_menu()

        print(self.disp.get_border()) # 罫線を引く

        print('機能を選択してください↓')
        
        # 機能の一覧を取得して表示
        self.menu.display_menu(menu_list)

        print(self.disp.get_border()) # 罫線を引く

        # 結果確認
        choice = int(input('選択 >>'))
        print(f'選択したのは{choice}です')

        # 家計簿を新規登録できるようにするためこのまま
        budget_list = [
                '家計簿1',
                '家計簿2',
                '家計簿3',
                ]

        # cliapp.run
        if choice == 1:
            # 新しい家計簿を作成する選択肢を表示
            print('家計簿一覧:')

            # メニュー表示
            self.menu.display_menu(budget_list)

            # 0は新規作成
            print('0: 新しい家計簿を作成')
            print('999: 終了')

            # ユーザーの選択を取得
            choice = int(input('選択してください (番号): '))

            if choice == 999:
                # 999なら終了
                input('終了します。')
            elif choice >= 1:
                # 家計簿が選択されたら家計簿の名前をメニュー画面に渡す
                pass
            else:
                print('無効な選択です。')

        return None

if __name__ == '__main__':
    app = CLIApp()
    app.run()
        