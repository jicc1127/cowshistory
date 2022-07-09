# -*- coding: utf-8 -*-
#コマンドラインから、引数を渡す
#　PS> python ps_fpyxlstrymdtodatetime_args.py wbN sheetN　col
#   'KT_CowsHistory.xlsx' KTFarm'  3列　と　9列
import sys
import chghistory

wbN = sys.argv[1]
sheetN = sys.argv[2]
col= int(sys.argv[3])
chghistory.fpyxlstrymdtodatetime(wbN, sheetN, col)

print(wbN +"/" + sheetN + " " + str(col)  +  "列 の 日付データをdatetime に変換しました。")
 