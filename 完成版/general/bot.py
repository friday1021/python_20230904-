try:
    import sys
    import datetime
except ImportError as e:
    print(e)
    sys.exit()
class Bot:
    
    def __init__(self) -> None:
        '''
        初期処理
        '''
        self.newtime = datetime.datetime.now()
    
    def greeting(self) -> str:
        '''
        時間帯ごとの挨拶の文字列を返却する
        '''
        now = datetime.datetime.now()
        hour = now.hour
        if hour >= 18:
            # 夜の挨拶
            letter = 'こんばんは！'
        elif hour >= 11:
            letter = 'こんにちは！'
        elif hour >= 5:
            letter = 'おはようございます！'
        else:
            letter = 'こんばんは！'
        letter += '\n現在の時刻は' + now.strftime('%Y/%m/%d %H:%M:%S') + 'です！'
        return letter