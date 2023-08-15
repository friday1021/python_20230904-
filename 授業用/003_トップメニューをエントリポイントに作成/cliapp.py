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
        pass

        
    def run(self) -> None:
        '''
        アプリのエントリポイント
        '''
        # displaymanager.DisplayManager.get_top_menu
        letter = [
                  '家計簿',
                  ]

        # displaymanager.DisplayManager.get_border
        print('-' * 80) # 罫線を引く

        print('機能を選択してください↓')
        
        # displaymanager.MenuDisplay.display_menu
        # 機能の一覧を取得して表示
        for index, item in enumerate(letter, start=1):
            print(f'{index}. {item}')

        # displaymanager.DisplayManager.get_border
        print('-' * 80) # 罫線を引く

        # 結果確認
        choise = input('選択 >>')
        print(f'選択したのは{choise}です')

        return None

if __name__ == '__main__':
    app = CLIApp()
    app.run()
        