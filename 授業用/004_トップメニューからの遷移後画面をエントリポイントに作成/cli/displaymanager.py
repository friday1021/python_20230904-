class DisplayManager:
    '''
    画面表示用の情報を管理するクラス
    '''

    def get_border(self, line_str='-', width=80, end='') -> str:
        '''
        罫線用文字列を返却
        '''
        pass


    def get_top_menu(self) -> str:
        '''
        トップメニュー一覧用の文字列を返却
        '''
        pass


    def get_accounts_menu(self) -> str:
        '''
        アカウント管理一覧用の文字列を返却
        '''
        pass


    def get_budgetbook_menu(self) -> str:
        '''
        家計簿メニューの一覧を返却
        '''
        pass


    def adjust_width_for_fullwidth(self, s, desired_width) -> str:
        '''
        全角の使用による表示崩れ対応
        全角分文字サイズを調整し返却
        '''
        pass


class MenuDisplay:
    '''
    メニュー表示用クラス
    '''

    def display_menu(self, menu_list) -> None:
        '''
        メニューのリストを受け取って画面表示
        '''
        pass
