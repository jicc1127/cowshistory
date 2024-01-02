# -*- coding: utf-8 -*-
#コマンドラインから、引数を渡す
#　PS> python ps_fpysep_outfrmin_args.py wbN sheetN coln ncol index name bdate
# wbN0 : cowshistory.xlsx, sheetN0 : ABFarm, wbN1 : AB_cowslist.xlsx, sheetN1 : cowslist, 
#colidno1 : 2 (column number fo idno1)
import sys
import chghistory

wbN = sys.argv[1]
sheetN = sys.argv[2]
coln = int(sys.argv[3])
ncol = int(sys.argv[4])
index = int(sys.argv[5] )
name = sys.argv[6]
bdate = sys.argv[7]

chghistory.fpysep_outfrmin( wbN, sheetN, coln, ncol, index, name, bdate )

print( wbN+ "/"  + sheetN + "の異動情報を基準日において 所属牛"+ sheetN+"in" "と 転出牛" + sheetN+"out"  + " に分けました")
 