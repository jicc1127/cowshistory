# -*- coding: utf-8 -*-
#コマンドラインから、引数を渡す
#　PS> python ps_fpyymd_csvtocowshistory_csv_args.py Ext Path bckPath
# 	'\.csv', '.\\', '.\\csvorg' 
import sys
import chghistory

Ext = sys.argv[1]
Path = sys.argv[2]
bckPath = sys.argv[3]

chghistory.fpyymd_csvtoCowsHistory_csv(Ext, Path, bckPath)

print(" Dir" + Path + " の ymd.csvファイルをymdH.csvファイルに変更しました。")
 