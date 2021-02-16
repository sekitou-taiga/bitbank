#アセット情報の取得

#python_bitbankccのパッケージをインポート
import python_bitbankcc

#APIキー，シークレットの設定
API_KEY = '5f2d8797-5d8f-4ccb-ac3a-d2bd05d4e5ea'
API_SECRET = '216c999292e8ee068359f440cb58d5e8c895450356203cd2946f1882491a7394'

#privte API classのオブジェクトを取得
prv = python_bitbankcc.private(API_KEY, API_SECRET)

#アセット一覧の取得
value = prv.get_asset()

#アセット情報の一例
asset_ex = value['assets'][1]
print('通貨名：' + asset_ex['asset'])
print('保有量：' + asset_ex['onhand_amount'])
print('ロックされている量：' + asset_ex['locked_amount'])
print('利用可能な量：' + asset_ex['free_amount'])
print('引き出し手数料：' + asset_ex['withdrawal_fee'])