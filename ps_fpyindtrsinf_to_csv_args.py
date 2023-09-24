# -*- coding: utf-8 -*-
#コマンドラインから、引数を渡す
#　PS> python ps_fpyindtrsinf_to_csv_args.py wbN sheetN col
#   'cowlist.xlsx'  'cowlist'  
import sys
import nlbcs

wbN = sys.argv[1]
sheetN = sys.argv[2]
col = int(sys.argv[3])
nlbcs.fpyindtrsinf_to_csv(wbN, sheetN, col)

print( 'individual transfer information to csv file 0123456789_yyyymmdd.csv')
 