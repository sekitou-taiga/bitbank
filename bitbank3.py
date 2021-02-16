#全約定履歴の取得

#python_bitbankccとdatetimeのパッケージをインポート
import python_bitbankcc
import datetime 

# public API classのオブジェクトを取得
pub = python_bitbankcc.public()

# 全約定履歴を取得
value = pub.get_transactions( 'btc_jpy' )

#約定履歴の一例
trans_ex = value['transactions'][0]
print('取引ID:' + str(trans_ex['transaction_id']))
print('売買情報:' + trans_ex['side'])
print('約定価格:' + trans_ex['price'])
print('数量:' + trans_ex['amount'])
print('約定日時:' + str(datetime.datetime.fromtimestamp(trans_ex['executed_at']/1000)))