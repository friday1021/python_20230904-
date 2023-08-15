class DisplayManager:
    '''
    画面表示用の情報を管理するクラス
    '''

    def get_border(self, line_str='-', width=80, end='') -> str:
        '''
        罫線用文字列を返却
        '''
        return line_str * width + end


    def get_top_menu(self) -> str:
        '''
        トップメニュー一覧用の文字列を返却
        '''
        letter = [
                  '家計簿',
                  ]
        return letter


    def get_accounts_menu(self) -> str:
        '''
        アカウント管理一覧用の文字列を返却
        '''
        letter = ['新規登録',
                  'ログイン',
                  'ログアウト',
                  ]
        return letter


    def get_budgetbook_menu(self) -> str:
        '''
        家計簿メニューの一覧を返却
        '''
        letter = ['表示',
                  '記録',
                  '収入/支出の削除',
                  'この家計簿を削除',
                  '戻る',
                  ]
        return letter


    def adjust_width_for_fullwidth(self, s, desired_width) -> str:
        '''
        全角の使用による表示崩れ対応
        全角分文字サイズを調整し返却
        '''

        # 全角文字の数を数えてサイズを算出
        count_fullwidth = sum([1 for c in s if '\u4e00' <= c <= '\u9fff' or '\u3040' <= c <= '\u30ff' or '\uff01' <= c <= '\uff5e'])
        adjusted_width = desired_width - count_fullwidth

        # 表示用幅を返却
        return f"{s:<{adjusted_width}}"


class MenuDisplay:
    '''
    メニュー表示用クラス
    '''

    def display_menu(self, menu_list) -> None:
        '''
        メニューのリストを受け取って画面表示
        '''
        for index, item in enumerate(menu_list, start=1):
            print(f'{index}. {item}')
