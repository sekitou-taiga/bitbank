#ロウソク足データの取得

#python_bitbankccとdatetimeのパッケージをインポート
import python_bitbankcc
import datetime

# public API classのオブジェクトを取得
pub = python_bitbankcc.public()

# ロウソク足データを取得
value = pub.get_candlestick( 'xrp_jpy',  '1hour', '20180504' )

#ローソク足情報の一例(2018/5/4 午前9時の1時間足)
candle = value['candlestick'][0]
print('candle type:' + candle['type'])
print('始値：' + candle['ohlcv'][0][0])
print('高値：' + candle['ohlcv'][0][1])
print('安値：' + candle['ohlcv'][0][2])
print('終値：' + candle['ohlcv'][0][3])
print('出来高：' + candle['ohlcv'][0][4])
print('対象時刻：' + str(datetime.datetime.fromtimestamp(candle['ohlcv'][0][5]/1000)))