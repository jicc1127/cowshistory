# cowshistory
PS C:\Users\inoue\Dropbox\rep\cowshistory>  python ps_cowshistory_webscrsys_args.py

-----CowsHistory_webscrsys---------------------------------------------------------v2.01-------

牛の個体情報検索サービス 個体識別番号の検索から個体の異動情報を検索し、
Excelファイルにリスト化するシステム

#fpytrs_infs_to_xlsx(wbN0, sheetN0, wbN1, sheetN1, colidno1)
個体リスト AB_cowslist/cowslistのidnoから個体異動情報を検索する
個体情報リスト cowshistory.xlsx/ABFarmに新規または追加入力する
PS> ps_fpytrs_infs_to_xlsx_args.py wbN0 sheetN0 wbN1 sheetN1 colidno1
wbN0 : cowshistory.xlsx, sheetN0 : ABFarm,
wbN1 : AB_cowslist.xlsx, sheetN1 : cowslist, colidno1 : 2 (column number of idno1)

#fpychk_drecords(wbN, sheetN, searchdate)
Excel個体情報リスト cowshistory/ABFarmの重複データをを削除する
PS> ps_fpychk_drecords_args.py wbN sheetN searchdate
wbN: ..\AB_cowshistory.xlsx, sheetN:ABFarm, searchdate:'yyyy/mm/dd'

#fpysep_outfrmin( wbN, sheetN, coln, ncol, index, name, bdate )
PS> python ps_fpysep_outfrmin_args.py wbN sheetN coln ncol index name bdate
wbN : ..\AB_cowshistory.xlsx, sheetN : ABFarm, coln : 2, ncol : 12,
index : 10, name :  AB Farm, bdate : yyyy/mm/dd
separate move-out cows from move-in
異動情報のExcelfile: AB_cowshistory.xlsx の　sheet　ABFarmの情報を
基準日における所属牛（転入牛move-in)と退出牛(転出牛move-out)の情報に分け、
2枚のsheet ABFarmin, ABFarmout を作成する

---------------------------------------------------------------2024/1/13 by jicc---------

- AB_cowshistory.x;sx/ABFarm : ABFarm の cowshistory(異動情報)

sheet ABFarm
| LineNo | 個体識別番号 | 出生の年月日 | 雌雄の別 | 母牛の個体識別番号 | 種別 |
| No | 異動内容 | 異動年月日 | 住所 | 氏名または名称 | 検索年月日 |

- AB_cowslist.xlsx/cowslist : ABFarmのcowslist

sheet cowslist のcolumnを以下のように設定する :
| cowslist_id | cowidNo | eartagNo | DHITNo | name | breed | birthday | sex |
| sire_code | sire_name | damidNo | dameartagNo | in_date | in_reason | from | out_date |
| out_reason | to | note | base_date |
or
| cowslist_id | 個体識別番号 | 耳標 | 検定番号 | 名前 | 品種 | 生年月日 | 性別 |
| 種雄牛コード | 種雄牛名 | 母牛個体識別番号 | 母牛耳標 | 導入年月日 | 導入理由 | 導入元 | 転出年月日 |
| 転出理由 | 転出先 | note | 基準日 |
