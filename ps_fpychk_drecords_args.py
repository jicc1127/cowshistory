# -*- coding: utf-8 -*-
#コマンドラインから、引数を渡す
#　PS> python ps_fpychk_drecords_args.py wbN sheetN
#   'cowshistory.xlsx'  'ABFarm'  
import sys
import chghistory

wbN = sys.argv[1]
sheetN = sys.argv[2]

chghistory.fpychk_drecords(wbN, sheetN)

print(wbN +"/" + sheetN   +  " の 重複データを抜き出しました。")
 