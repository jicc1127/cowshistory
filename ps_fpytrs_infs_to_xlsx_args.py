# -*- coding: utf-8 -*-
#コマンドラインから、引数を渡す
#　PS> python ps_fpytrs_infs_to_xlsx_args.py wbN0 sheetN0 wbN1 sheetN1 colidno1
# wbN0 : cowshistory.xlsx, sheetN0 : ABFarm, wbN1 : AB_cowslist.xlsx, sheetN1 : cowslist, 
#colidno1 : 2 (column number fo idno1)
import sys
import chghistory

wbN0 = sys.argv[1]
sheetN0 = sys.argv[2]
wbN1 = sys.argv[3]
sheetN1 = sys.argv[4]
colidno1 = int( sys.argv[5] )

chghistory.fpytrs_infs_to_xlsx(wbN0, sheetN0, wbN1, sheetN1, colidno1)

print( wbN1+ "/"  + sheetN1 + "の個体リストの個体異動情報を検索し" +  wbN1 + "/" + sheetN1  + " に入力しました。")
 