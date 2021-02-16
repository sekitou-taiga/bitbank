#新規注文を行う

#python_bitbankccとdatetimeのパッケージをインポート
import python_bitbankcc
import datetime

#APIキー，シークレットの設定
API_KEY = '5f2d8797-5d8f-4ccb-ac3a-d2bd05d4e5ea'
API_SECRET = '216c999292e8ee068359f440cb58d5e8c895450356203cd2946f1882491a7394'

#privte API classのオブジェクトを取得
prv = python_bitbankcc.private(API_KEY, API_SECRET)

#新規注文を行う：'ペア', '価格', '注文枚数', '売or買', '指値or成行'
value = prv.order( 'bcc_jpy', '200000', '0.07', 'sell', 'limit' )

#新規注文内容
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

#注文のキャンセル(ここでは，上記の注文を即時にキャンセルしている)
prv.cancel_order( value['pair'], str(value['order_id']) )　#'ペア', '注文ID'