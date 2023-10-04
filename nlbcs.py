# -*- coding: utf-8 -*-
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
import numpy as np 
#fpyopen_url
"""
fpyopen_url:
    open a url and return a webdriver
    v1.1   例外処理を追加
    2023/6/3
    @author: jicc
    
"""
def fpyopen_url(url):
    """
    open a url and return a webdriver

    Parameters
    ----------
    url : str
        url to open  
        ex:"https://www.id.nlbc.go.jp/CattleSearch/search/agreement"

    Returns
    -------
    driver : webdriver.chrome.webdriver.WebDriver
    WebDriver object of selenium.webdriver.chrome.webdriver module

    """
    #from selenium import webdriver
    from selenium.common.exceptions import SessionNotCreatedException
    
    try:
        driver = webdriver.Chrome()
        
    except SessionNotCreatedException:
        print("chromedriverのversionがあっていません。")
    
    try:    
        driver.get(url)
        return driver

    except UnboundLocalError:
        print("urlを取得できません")

#fpydriver_quit
"""
fpydriver_quit:
    quit the browser
    v1.0
    2022/6/29
    @author: jicc
    
"""
def fpydriver_quit(driver):
    """
    quit the browser

    Parameters
    ----------
    driver : webdriver.chrome.webdriver.WebDriver
        WebDriver object of selenium.webdriver.chrome.webdriver module

    Returns
    -------
    None.

    """
    #from selenium import webdriver
      
    driver.quit()

#fpydriver_close
"""
fpydriver_close:
    close a page of the browser
    v1.0
    2022/6/29
    @author: jicc
    
"""
def fpydriver_close(driver):
    """
    close a page of the browser

    Parameters
    ----------
    driver : webdriver.chrome.webdriver.WebDriver
        WebDriver object of selenium.webdriver.chrome.webdriver module

    Returns
    -------
    None.

    """
    #from selenium import webdriver
      
    driver.close()

#fpyname_click   
"""
fpyname_click
    click the attribute of a name
    v1.0
    2022/6/29
    @author: jicc

"""
def fpyname_click(driver, name):
    """
    click the attribute of a name

    Parameters
    ----------
    driver : webdriver.chrome.webdriver.WebDriver
    WebDriver object of selenium.webdriver.chrome.webdriver module
    name : str
        an attribute 
        ex."method:goSearch"

    Returns
    -------
    None.

    """
    
    element = driver.find_element_by_name(name)
    element.click()    
    
#fpyidno_search    
"""
fpyidno_search:
    search an individual and it's transfer information
    v1.0
    2022/6/30
    @author: jicc
    
"""
def fpyidno_search(driver, idno):
    '''
    search an individual and it's transfer information

    Parameters
    ----------
    driver : webdriver.chrome.webdriver.WebDriver
    WebDriver object of selenium.webdriver.chrome.webdriver module
    idno : str
        individual identification number (10figures)
        ex. "0861094620", '1577804244'
    Returns
    -------
    None.

    '''
    #import time
    #from selenium.common.exceptions import NoSuchElementException
    #try:
    idno_elem = driver.find_element_by_name("txtIDNO")
    idno_elem.send_keys(idno) #0861094620　1577804244
    #idno_elem.submit()..this is impossible! 
    search_elem = driver.find_element_by_name("method:doSearch")
    search_elem.click()
    #except NoSuchElementException:
    #    print("Error: " + idno + " not found")
    #    time.sleep(3)
    
#fpynowDate_s00
"""
fpynowDate_s00:
    get the data of nowDate "2022年06月30日 10時現在"
    and return str nowDate "yyyymmdd" for filename
    v1.0
    2022/7/4
    @author: jicc
    
"""
def fpynowDate_s00(driver):
    """
    get the data of nowDate "2022年06月30日 10時現在"
    and return str nowDate "yyyy/mm/dd"

    Parameters
    ----------
    driver : webdriver.chrome.webdriver.WebDriver
    WebDriver object of selenium.webdriver.chrome.webdriver module

    Returns
    -------
    nowDate : str
        the date of a search
        ex. "yyyymmdd"

    """
    import re
    nowDate = driver.find_element_by_class_name("nowDate")
    nowDate = nowDate.text
    #print(nowDate)
    nowDate_reg = re.compile(r'(\d\d\d\d)年(\d\d)月(\d\d)')
    mo = nowDate_reg.search(nowDate)
    year = mo.group(1)  #str
    month = mo.group(2) #str
    day = mo.group(3)   #str
    
    nowDate = year + month + day
    
       
    return nowDate
    
#fpynowDate_s01
"""
fpynowDate_s01:
    get the data of nowDate "2022年06月30日 10時現在"
    and return str nowDate "yyyy/mm/dd"
    v1.0
    2022/6/30
    @author: jicc
    
"""
def fpynowDate_s01(driver):
    """
    get the data of nowDate "2022年06月30日 10時現在"
    and return str nowDate "yyyy/mm/dd"

    Parameters
    ----------
    driver : webdriver.chrome.webdriver.WebDriver
    WebDriver object of selenium.webdriver.chrome.webdriver module

    Returns
    -------
    nowDate : str
        the date of a search
        ex. "yyyy/mm/dd"

    """
    import re
    nowDate = driver.find_element_by_class_name("nowDate")
    nowDate = nowDate.text
    #print(nowDate)
    nowDate_reg = re.compile(r'(\d\d\d\d)年(\d\d)月(\d\d)')
    mo = nowDate_reg.search(nowDate)
    year = mo.group(1)  #str
    month = mo.group(2) #str
    day = mo.group(3)   #str
    
    nowDate = year + '/' + month + '/' + day
    
       
    return nowDate 

#fpyidno_search_results
"""
fpyidno_search_results:
    get a list of individual number search results
    v1.0
    2022/6/30
    @author: jicc
    
"""
def fpyidno_search_results(driver):
    """
    get a list of individual number search results

    Parameters
    ----------
    driver : webdriver.chrome.webdriver.WebDriver
    WebDriver object of selenium.webdriver.chrome.webdriver module

    Returns
    -------
    list
    individual number search results

    """
    #return all WebElement objects' list of CSSclass name "resultTable"
    idno_search_results = driver.find_elements_by_class_name("resultTable")
    #print("idno_searck_results")
    #print(idno_search_results)
    l = len(idno_search_results)
    isresults = [] #要素の内部テキストのリスト作成　text:method
    for i in range(0, l):
        isresults.append(idno_search_results[i].text)
    
    return isresults
    #['個体識別番号', '出生の年月日', '雌雄の別', '母牛の個体識別番号', '種別',
    #'1657613438', '2022.04.05', 'メス', '1362646332', '黒毛和種', ' ',
    #'異動内容', '異動年月日', '飼養施設所在地', '氏名または名称', '都道府県', '市区町村',
    #'1', '出生', '2022.04.05', '兵庫県', 'AB市', 'AB牧場']

#fpyind_inf
"""
fpyind_inf:
    get a list of individual information
    v1.01
    2022/7/6
    @author: jicc
    
"""
def fpyind_inf(isresults):
    """
    get a list of individual information
    birthday 'yyyy.mm.dd' -> datetime  add date part  #1
    2022/7/6 v1.01
    Parameters
    ----------
    isresults : list
        individual number search results

    Returns
    -------
    lists' list
    individual information

    """
    import chghistory
    
    ind_inf = []
    
    #if isresults != []:
    ind_inf.append(isresults[0:5])  #columns' name
    ind_inf.append(isresults[5:10]) #individual information
    
    date = ind_inf[1][1] #1
    ind_inf[1][1] = chghistory.fpydate_dottoslash( date ) #1
    #else:
    #    ind_inf = ["idNo = ????"]
    
    return ind_inf

#fpytrs_inf
"""
fpytrs_inf:
    get a list of transfer information
    v1.02
    2022/7/12
    add a column "searching date" *)
    v2.0
    2023/9/24
    @author: jicc
    
"""
def fpytrs_inf(isresults, ind_inf, nowDate_):
    """
    get a list of transfer information
    transfer date 'yyyy.mm.dd' -> datetime : add date part  #2
    2022/7/6 v1.01
    Parameters
    ----------
    isresults : list
        idNo(individual number) search results
    ind_inf : list
        individual information
    nowDate_ : str
        searching date yyyy/mm/dd

    Returns
    -------
    lists' list
    individual transfer information

    """
    import chghistory
    #transfer information 異動情報
    trs_inf = [] #return to default
    trs_inf_clmns_ = ['No']  #colum names

    trs_inf_clmns_ = trs_inf_clmns_ + isresults[11:15] 
    trs_inf_clmns = ind_inf[0] + trs_inf_clmns_ 
    trs_inf_clmns.append( "検索年月日" )
    #add a column "検索年月日"
    #ind_inf[0] = ['個体識別番号', '出生の年月日', '雌雄の別', '母牛の個体識別番号', '種別']
    #isresults[11:15] = ['異動内容', '異動年月日', '飼養施設所在地', '氏名または名称']
    #print('trs_inf_clmns')
    #print(trs_inf_clmns)
    #trs_inf_clmns = ['個体識別番号', '出生の年月日', '雌雄の別', '母牛の個体識別番号', '種別',
    #'No', '異動内容', '異動年月日', '飼養施設所在地', '氏名または名称', '検索年月日']
    
    trs_inf.append(trs_inf_clmns)  #trs_inf = [[trs_inf_clmns]]
    #column名の行 trs_inf[0] をセット、以下に異動情報のリストを追加する。
    print(trs_inf)
    isresults = isresults[17:] 
    #'個体識別番号'から'市区町村'まで削除し、異動情報だけのリストとする。
    #print('isresults')
    #print(isresults)
    
    #transfer information individual data, no columns'list and data's list only 
    #個体の異動情報だけのリスト, column名の行のリストなし data's list only
    trs_inf_inddt = [] #return to default
    
    li = len(isresults) #異動情報リストの要素数
    #print(li)
    li = li / 6 # 1異動情報 6要素で割る。異動回数('No')の算出
    #print(li)
    li = int(li) #float to int
    #print(li)

    for i in range(0, li):
        #transfer information of No. i,　6elements
        #No. i+1 の異動情報　6要素
        #リスト['i+1', '出生', '2014.06.13', '??県', '??市', '??牧場'] を追加する。
        trs_inf_inddt_tmp = isresults[0:6]
        #add a column searching date
        #検索年月日を加える
        trs_inf_inddt_tmp.append( nowDate_ )        #*)
        #add a trs_inf to the list trs_inf_inddt
        #異動情報リストを追加する
        trs_inf_inddt.append(trs_inf_inddt_tmp)
        #追加したdataを list isresults から削除する
        del isresults[0:6]
        
    print('trs_inf_inddt')
    print(trs_inf_inddt)

    for j in range(0, li):
        
        date = trs_inf_inddt[j][2]  #2
        trs_inf_inddt[j][2] = chghistory.fpydate_dottoslash( date ) #2
        #lists' list trs_inf_inddt の第j要素(list)の第3要素(異動年月日)を
		#transfer date 'yyyy.mm.dd' -> 'yyyy/mm/dd
        
        #join two elements [3] and [4] to element[3](address)
        # 2要素 '都道府県', '市区町村'を結合して、'飼養施設所在地'に統合する。
        address = trs_inf_inddt[j][3] + ' ' + trs_inf_inddt[j][4]
        del trs_inf_inddt[j][4]
        trs_inf_inddt[j][3] = address
        
        #replace '\u3000全角空白' to ' ' v1.02 2022/7/12
        tmp = trs_inf_inddt[j][4].replace( '\u3000', ' ')
        trs_inf_inddt[j][4] = tmp
        #この作業が必要か不明2023/9/7
        
    	#□tmpに if trs_inf_inddt[j][4] == None:
    	#					trs_inf_inddt[j][4] = ''
    	#				else:
    	#					tmp = trs_inf_inddt[j][4].replace( '\u3000', ' ')
    	#					trs_inf_inddt[j][4] = tmp
    	# の処置はいらないか?　
    	# trs_inf_inddt[j][4]にNull値があった場合、
    	#AttributeError: 'NoneType' object has no attribute 'replace' が発生するかも？
    	#2022/8/3
    #print(trs_inf_inddt)
    
    #trs_inf_inddtの各要素に、個体情報を紐づける
    #ind_infを紐づけ
    ind_trs_dt = []
    ind_trs_dt = ind_inf[1] #個体情報をセット
    
    #各異動情報の前に、個体情報ind_trs_dt を付ける。
    for k in range(0, li):
    
        ind_trs_dtk = ind_trs_dt + trs_inf_inddt[k]
        trs_inf.append(ind_trs_dtk)
    #個体異動情報の lists' list trs_inf の完成 
    
    return trs_inf

#fpysave_to_csv
"""
fpysave_to_csv:
    save lists' list trs_inf to the csv file
    v1.0
    2022/7/2
    @author: jicc
    
"""
def fpysave_to_csv(filename, trs_inf):
    """
    save lists' list trs_inf to the csv file

    Parameters
    ----------
    filename : str
        filename
    trs_inf : list
        transfer information

    Returns
    -------
    None.

    """
    
    #import numpy as np 
    
    filename = filename + '.csv'
    #save to csvfile
    np.savetxt(filename, trs_inf, delimiter =",", fmt ='% s')

#fpytrsinf_to_H_csv
"""
fpytrsinf_to_H_csv:
    search and save individual transfer information to History csvfile
    #個体情報を検索し、idno_yyyymmdd.csv fileに保存する
    2022/7/6
    v1.0
    @author: jicc
    
"""
def fpytrsinf_to_H_csv(driver, idno):
    """
    search and save individual transfer information to History csvfile

    Parameters
    ----------
    driver : webdriver.chrome.webdriver.WebDriver
    WebDriver object of selenium.webdriver.chrome.webdriver module
    idno : str
        ex. "0123456789"
    
    Returns
    -------
    None.
    
    """
    
    #import nlbcs
    
    fpyidno_search(driver, idno )
    #open the page of idno's transfer information
    nowDate = fpynowDate_s00(driver)
    #get a nowDate with "yyyymmdd" for a filename
    file_name = idno + '_' + nowDate
    #0123456789_yyyymmdd
    print("nowDate")
    print(nowDate)
    
    nowDate_ = fpynowDate_s01(driver)
    #get a nowDate_ with "yyyy/mm/dd" for a fillindate
    print("nowDate_")
    print(nowDate_)
    
    isresults = fpyidno_search_results(driver)
    #get a list of idNo(individual number) search results
    #print("isresults")
    #print(isresults)
    ind_inf = fpyind_inf(isresults)
    #get a list of individual information
    #print("ind_inf")
    #print(ind_inf)
    trs_inf = fpytrs_inf(isresults, ind_inf, nowDate_ )
    #get a list of transfer information
    #print("trs_inf")
    #print(trs_inf)
    print(trs_inf[1][0] + '_' + nowDate + '.csv')
    fpysave_to_csv(file_name, trs_inf)
    #lists' list trs_inf to the csv file 0123456789_yyyymmdd.csv

#fpyindtrsinf_to_csv
"""
fpyindtrsinf_to_csv: 
    individual transfer information to csv file
    #牛の個体情報を検索し、csvファイルに保存する
    v1.01
    2022/7/5
    column 2 を　parameter col に変更 *)
    v1.02
    2023/9/9
    @author: jicc
    
"""
def fpyindtrsinf_to_csv(wbN, sheetN, col):
    """
    individual transfer information to csv file
    add try~except v1.01 2022/7/5
    Parameters
    ----------
    wbN : str
        Excelfile name    ex. "cowlist.xlsx"
    sheetN : str
        sheet name        ex. "cowlist"
    col : int
        column number of idNo in a Excel sheet's list
    Returns
    -------
    None.

    """
    #import nlbcs
    import chghistory
    import time
    from selenium.common.exceptions import NoSuchElementException

    wb = chghistory.fpyopenxl(wbN, sheetN)
    sheet = wb[1]
    max_row = sheet.max_row

    driver = fpyopen_url("https://www.id.nlbc.go.jp/CattleSearch/search/agreement")
    fpyname_click(driver, "method:goSearch") 
    for row_num in range(2, max_row + 1):
        #idno 個体識別番号を　2行目2列から順番に取得する
        idno = chghistory.fpygetCell_value(sheet, row_num, col)
        # column 2 を　parameter col に変更 *) 2023/9/9 
        try:
            fpytrsinf_to_H_csv(driver, idno)
            #search and save individual transfer informations 
            #to a History csvfile 0123456789_yyyymmdd.csv
			#個体異動情報を検索し、csvfile 0123456789_yyyymmdd.csv に保存する。
        except NoSuchElementException:
            print("Error: " + idno + " not found")
        time.sleep(2)

    fpydriver_quit(driver)

#fpytrsinf_to_list
"""
fpytrsinf_to_list:
     search and return individual transfer information to list
    v1.01
    2022/7/22
    @author: jicc
    
"""
def fpytrsinf_to_list(driver,idno):
    """
    search and return individual transfer information to list

    Parameters
    ----------
    driver : webdriver.chrome.webdriver.WebDriver
    WebDriver object of selenium.webdriver.chrome.webdriver module
    idno : str
        ex. "0123456789"
    
    Returns
    -------
    trs_inf : list
    
    individual transfer information
    
    """
    #import nlbcs
    #import time
    fpyidno_search(driver, idno )
    #open the page of idno's transfer information
    nowDate = fpynowDate_s00(driver) #*
    print(nowDate) #*
    print(idno) #*
    #get nowDate if nowDate == None -> idNo not found...NoSuchElementException
    #* v1.01 2022/7/22
    isresults = fpyidno_search_results(driver)
    #get a list of individual number search results
    #print(isresults)
    ind_inf = fpyind_inf(isresults)
    #get a list of individual information
    #print(ind_inf)
    trs_inf = fpytrs_inf(isresults, ind_inf)
    #get a list of transfer information
    #print(trs_inf)
    return trs_inf

#fpytrsinf_to_xlsx
"""
fpytrsinf_to_xlsx:
     search and save individual transfer information to Excelfile
    v1.02
    2022/7/26
    #1) 3,9,12列の年月日をdatetimeに変換　を追加
    #2) LineNo 入力を追加
    v1.03
    2023/10/4
    @author: jicc
    
"""
def fpytrsinf_to_xlsx(driver,idno, sheet):
    """
    search and save individual transfer information to Excelfile

    Parameters
    ----------
    driver : webdriver.chrome.webdriver.WebDriver
    WebDriver object of selenium.webdriver.chrome.webdriver module
    idno : str
        ex. "0123456789"
    sheet : worksheet.worksheet.Worksheet
         worksheet object
    
    Returns
    -------
    sheet : worksheet.worksheet.Worksheet
         worksheet object
         after this, we need to save this Excelfile
         ex. wb.save("cowshistory.xlsx")
   
    """
    import nlbcs
    import chghistory
    
    nlbcs.fpyidno_search(driver, idno )
    #open the page of idno's transfer information
    nowDate = nlbcs.fpynowDate_s00(driver) #not necessary? 不要? 2023/10/4
    print("nowDate")
    print(nowDate) #*
    print(idno) #*
    
    nowDate_ = nlbcs.fpynowDate_s01(driver)
    #get a nowDate_ with "yyyy/mm/dd" for a fillindate
    print("nowDate_")
    print(nowDate_)
    
    isresults = nlbcs.fpyidno_search_results(driver)
    #get a list of individual number search results
    #print(isresults)
    ind_inf = nlbcs.fpyind_inf(isresults)
    #get a list of individual information
    #print(ind_inf)
    trs_inf = nlbcs.fpytrs_inf(isresults, ind_inf, nowDate_)
    #get a list of transfer information
    #print(trs_inf)
    
    l = len(trs_inf)    #trs_inf[1]~trs_inf[l-1]まで入力(trs_inf[0]:title) 
    l0 = len(trs_inf[0]) #number of elements
    max_row = sheet.max_row
    i = max_row + 1
    for j in range(1, l):   #trs_inf[1]~trs_inf[l-1]
        for k in range(0, l0):  #trs_inf[j][0]~trs_inf[j][l0-1]
                chghistory.fpyinputCell_value(sheet, i, 1, i-1) #2)
                #LineNo
                chghistory.fpyinputCell_value(sheet, i, k+2, trs_inf[j][k])
                #column k+1:LineNo(None)
        i = i + 1
    
    #sheet 3列 '出生の年月日' 'yyyy/mm/dd' -> datetimeに変換  #1)
    chghistory.fpyxlstrymdtodatetime_s( sheet, 3 )
    print('sheet 3列 \'出生の年月日\' \'yyyy/mm/dd\' -> datetimeに変換')
    
    #sheet 9列 '異動年月日' 'yyyy/mm/dd' -> datetimeに変換  #1)
    chghistory.fpyxlstrymdtodatetime_s( sheet, 9 )
    print('sheet 9列 \'異動年月日\' \'yyyy/mm/dd\' -> datetimeに変換')
    
    #sheet 12列 '検索年月日' 'yyyy/mm/dd' -> datetimeに変換 #1)
    chghistory.fpyxlstrymdtodatetime_s( sheet, 12 )
    print('sheet 12列 \'検索年月日\' \'yyyy/mm/dd\' -> datetimeに変換')
    
    
    return sheet

#reference    
def nlbcsReference():
    
    print('-----nlbcsReference ---------------------------------------------------------v1.01------')
    print('**fpyopen_url(url)')
    print('open a url and return a webdriver')
    print('.............................................................................................')
    print('**fpydriver_quit(driver)')
    print('quit the browser')
    print('.............................................................................................')
    print('**fpydriver_close(driver)')
    print('close a page of the browser')
    print('.............................................................................................')
    print('**fpyname_click(driver, name)')
    print('click the attribute of a name')
    print('.............................................................................................')
    print('**fpyidno_search(driver, idno)')
    print('search an individual and it\'s transfer information')
    print('.............................................................................................')
    print('**fpynowDate_s00(driver)')
    print('get the data of nowDate \"2022年06月30日 10時現在\"')
    print('and return str nowDate \"yyyymmdd\" for filename')
    print('.............................................................................................')
    print('**fpynowDate_s01(driver)')
    print('get the data of nowDate \"2022年06月30日 10時現在\"')
    print('and return str nowDate \"yyyy/mm/dd\"')
    print('.............................................................................................')
    print('**fpyidno_search_results(driver))')
    print('get a list of individual number search results')
    print('.............................................................................................')
    print('**fpyind_inf(isresults)')
    print('get a list of individual information')
    print('.............................................................................................')
    print('**fpytrs_inf(isresults, ind_inf)')
    print('get a list of transfer information')
    print('.............................................................................................')
    print('**fpysave_to_csv(filename, trs_inf)')
    print('save lists\' list trs_inf to the csv file')
    print('.............................................................................................')
    print('**fpytrsinf_to_H_csv(driver,idno)')
    print('search and save individual transfer information to History csvfile')
    print('.............................................................................................')
    print('**fpyindtrsinf_to_csv(wbN, sheetN)')
    print('individual transfer information to csv file')
    print('.............................................................................................')
    print('**fpytrsinf_to_list(driver,idno)')
    print('search and return individual transfer information to list')
    print('.............................................................................................')
    print('**fpytrsinf_to_xlsx(driver,idno, sheet)')
    print('search and save individual transfer information to Excelfile')
    print('--------------------------------------------------------------------2022/7/25 by jicc---------')