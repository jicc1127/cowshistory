# -*- coding: utf-8 -*-
#コマンドラインから、引数を渡す
#　PS> python ps_fpydel_d_idno_args.py wbN sheetN
#   'cowshistory.xlsx'  'ABFarm'  
import sys
import chghistory

wbN = sys.argv[1]
sheetN = sys.argv[2]

chghistory.fpydel_d_idNo(wbN, sheetN)

print(wbN +"/" + sheetN   +  " の 重複idNoを削除しました。")
 