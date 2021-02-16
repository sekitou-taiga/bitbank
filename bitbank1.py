#ティッカー情報の取得

#python_bitbankccのパッケージをインポート
import python_bitbankcc 

# public API classのオブジェクトを取得
pub = python_bitbankcc.public()

# ティッカー情報を取得
value = pub.get_ticker( 'btc_jpy' )

#現在の売り注文の最安値
print('sell:' + value['sell'])
#現在の買い注文の最安値
print('buy:' + value['buy'])
#過去24時間の最高値取引価格
print('high:' + value['high'])
#過去24時間の最安値取引価格
print('low:' + value['low'])
#最新取引価格
print('last:' + value['last'])
#過去24時間の出来高
print('vol:' + value['vol'])

"""
通貨ペア
    btc_jpy, xrp_jpy, xrp_btc, ltc_jpy, ltc_btc, eth_jpy, eth_btc, mona_jpy, mona_btc, bcc_jpy, bcc_btc, xlm_jpy, xlm_btc, qtum_jpy, qtum_btc
"""