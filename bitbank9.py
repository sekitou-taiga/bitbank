#約定履歴を取得する

#python_bitbankccのパッケージをインポート
import python_bitbankcc
import datetime

#APIキー，シークレットの設定
API_KEY = '5f2d8797-5d8f-4ccb-ac3a-d2bd05d4e5ea'
API_SECRET = '216c999292e8ee068359f440cb58d5e8c895450356203cd2946f1882491a7394'

#privte API classのオブジェクトを取得
prv = python_bitbankcc.private(API_KEY, API_SECRET)

#約定履歴を取得する：　'ペア', '取得する約定数'
value = prv.get_trade_history('btc_jpy', '10')


print('取引ID：' + str(value['trade_id']))
print('通貨ペア：' + value['pair'])
print('売買情報：' + value['side'])
print('注文タイプ：' + value['type'])
print('注文時の数量：' + value['start_amount'])
print('未約定の数量：' + value['remaining_amount'])
print('約定済の数量：' + value['executed_amount'])
print('注文価格：' + value['price'])
print('平均約定価格：' + value['average_price'])
print('注文状態：' + value['status'])
print('注文日時：' + str(datetime.datetime.fromtimestamp(value['ordered_at']/1000)))
print('約定日時：' + str(datetime.datetime.fromtimestamp(value['executed_at']/1000)))