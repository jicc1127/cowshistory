# -*- coding: utf-8 -*-
#コマンドラインから、引数を渡す
#　PS> python ps_fpynewtrs_infs_to_xlsx_args.py wbN0 sheetN0 colidno0 wbN1 sheetN1 colidno1
# wbN0 : cowshistory.xlsx, sheetN0 : ABFarm, colidno0 : 2 (column number fo idno0), 
# wbN1 : AB_cowslist.xlsx, sheetN1 : cowslist, colidno1 : 2 (column number fo idno1)
import sys
import chghistory

wbN0 = sys.argv[1]
sheetN0 = sys.argv[2]
colidno0 = int( sys.argv[3] )
wbN1 = sys.argv[4]
sheetN1 = sys.argv[5]
colidno1 = int( sys.argv[6] )

chghistory.fpynewtrs_infs_to_xlsx(wbN0, sheetN0, colidno0, wbN1, sheetN1, colidno1)

print( wbN1+ "/"  + sheetN1 + "の個体リストの個体異動情報を検索し、新しい情報を" +  wbN0+ "/" + sheetN0  + " に追加入力しました。")
 