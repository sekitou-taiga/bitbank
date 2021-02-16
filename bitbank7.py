#アクティブな注文情報を取得

#python_bitbankccとdatetimeのパッケージをインポート
import python_bitbankcc
import datetime

#APIキー，シークレットの設定
API_KEY = '5f2d8797-5d8f-4ccb-ac3a-d2bd05d4e5ea'
API_SECRET = '216c999292e8ee068359f440cb58d5e8c895450356203cd2946f1882491a7394'

#privte API classのオブジェクトを取得
prv = python_bitbankcc.private(API_KEY, API_SECRET)

#アクティブな注文一覧の取得
value = prv.get_active_orders( 'btc_jpy' )

#注文一覧の一例
order_ex = value['orders'][0]
print('取引ID：' + str(order_ex['order_id']))
print('通貨ペア：' + order_ex['pair'])
print('売買情報：' + order_ex['side'])
print('注文タイプ：' + order_ex['type'])
print('注文時の数量：' + order_ex['start_amount'])
print('未約定の数量：' + order_ex['remaining_amount'])
print('約定済の数量：' + order_ex['executed_amount'])
print('注文価格：' + order_ex['price'])
print('平均約定価格：' + order_ex['average_price'])
print('注文状態：' + order_ex['status'])
print('注文日時：' + str(datetime.datetime.fromtimestamp(order_ex['ordered_at']/1000)))