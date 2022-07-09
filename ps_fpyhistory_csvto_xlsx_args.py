# -*- coding: utf-8 -*-
#コマンドラインから、引数を渡す
#　PS> python ps_fpyhistory_csvto_xlsx_args.py Ext Path bckPath wbN sheetN
# 	'\.csv', '.\\', '.\\csvhistory'  'MH_CowsHistory.xlsx' 'MHFarm'
import sys
import chghistory

Ext = sys.argv[1]
Path = sys.argv[2]
bckPath = sys.argv[3]
wbN = sys.argv[4]
sheetN = sys.argv[5]

chghistory.fpyHistory_csvto_xlsx(Ext, Path, bckPath, wbN, sheetN)

print(" Dir" + Path + " の idno_yyyymmdd.csvファイルをCowsHistory.xlsxに入力しました。")
 