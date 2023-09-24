# -*- coding: utf-8 -*-
#コマンドラインから、引数を渡す
#　PS> python ps_fpyfpymkd_path_args.py path
#    .\\csvhistory, .\\bck etc.
import sys
import chghistory

path = sys.argv[1]

chghistory.fpymkd_path( path )

print("ディレクトリ" + path + "を作成しました。")
 