# -*- coding: utf-8 -*-
#コマンドラインから、引数を渡す
#　PS> python ps_fpyspdfindirtocsv_args.py Ext Path bckPath
# 	'\.pdf', '.\\', '.\\pdforg' 
import sys
import chghistory

Ext = sys.argv[1]
Path = sys.argv[2]
bckPath = sys.argv[3]

chghistory.fpySpdf_in_Dir_to_csv(Ext, Path, bckPath)

print(" Dir" + Path + " の pdfファイルをcsvファイルに変更しました。")
 