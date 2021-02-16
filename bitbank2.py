#板情報の取得

#python_bitbankccのパッケージをインポート
import python_bitbankcc 

# public API classのオブジェクトを取得
pub = python_bitbankcc.public()

# 板情報を取得
value = pub.get_depth( 'xrp_jpy' )

#売り板
print('売り板 [価格, 数量]:' + ','.join(map(str,value['asks'])))
#買い板
print('買い板 [価格, 数量]:' + ','.join(map(str,value['bids'])))
