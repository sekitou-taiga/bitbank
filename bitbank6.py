#注文IDを指定して注文情報を取得

#python_bitbankccとdatetimeのパッケージをインポート
import python_bitbankcc
import datetime

#APIキー，シークレットの設定
API_KEY = '5f2d8797-5d8f-4ccb-ac3a-d2bd05d4e5ea'
API_SECRET = '216c999292e8ee068359f440cb58d5e8c895450356203cd2946f1882491a7394'

#privte API classのオブジェクトを取得
prv = python_bitbankcc.private(API_KEY, API_SECRET)

#注文情報の取得
value = prv.get_order( 'btc_jpy', '11702854576' )#'ペア', '注文ID'

#注文情報の一例
print('取引ID：' + str(value['order_id']))
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


