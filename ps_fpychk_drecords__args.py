# -*- coding: utf-8 -*-
#コマンドラインから、引数を渡す
#　PS> python ps_fpychk_drecords_args.py wbN sheetN searchdate
#   'cowshistory.xlsx'  'ABFarm'  
import sys
import chghistory

wbN = sys.argv[1]
sheetN = sys.argv[2]
searchdate = sys.argv[3]
chghistory.fpychk_drecords_(wbN, sheetN, searchdate)

print(wbN +"/" + sheetN   +  " の 重複データを抜き出しました。")
 