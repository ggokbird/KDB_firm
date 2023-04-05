# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 22:02:47 2023

@author: Dongjae
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 07:50:32 2023

@author: Dongjae
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 21:56:20 2023

@author: Dongjae
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
# %% (0) Working Directory
import os 
import re
from urllib import request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import pandas as pd 
from tqdm import tqdm

try : 
    os.chdir("C://Users//Dongjae//Desktop//KRX") # Change Directory

except : 
    print("Directory not found")

# %% (0)-(1) chrome driver 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

import chromedriver_autoinstaller
import os
import time
from selenium.webdriver.chrome.options import Options
import subprocess

# Check if chrome driver is installed or not
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'

if os.path.exists(driver_path):
    print(f"chrom driver is insatlled: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)

# Get driver and open url
driver = webdriver.Chrome(driver_path)
driver.get("https://google.com")

# %% (0)-(2) chrome driver 
"""
 # LINK : https://github.com/ultrafunkamsterdam/undetected-chromedriver/issues/743
 # LINK : https://pythondocs.net/selenium/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81-%EB%B4%87-%ED%83%90%EC%A7%80-%EC%9A%B0%ED%9A%8C/
"""
    
subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동    
# subprocess.Popen(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', '--remote-debugging-port=1337 --headless'])

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    dr = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    dr = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
dr.implicitly_wait(5)

# %% (1)-(1) Session : Not working → login input 用
"""
○ Validating XPath Selectors in the browser (chrome Dev Tools)
$x("//html");
 ex) $x("//#contents > div.login-wrap > div > form > div:nth-child(1) > div > div > input")
document.querySelectorAll("<YOUR_CSS_SELECTOR>")
 ex) document.querySelectorAll("//#contents > div.login-wrap > div > form > div:nth-child(1) > div > div > input")
"""
app_id = 'goguma@krx.co.kr'
app_pw = "wkrwjs12!@"


dr.set_window_size(1200, 2400)  # 웹창 크기 지정
dr.get('https://dataservice.koscom.co.kr/login?returnUrl=/krx/approval-list')  
dr.maximize_window()
dr.implicitly_wait(10)  # 창이 뜰때까지 기다림

def ilogin():
    # 요소 지정
    try : 
        id_box = dr.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')   # ID입력창
        password_box = dr.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[2]/div/div/input') # password 입력창
        login_button = dr.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[3]/button')  # 로그인 버튼
    
        # 동작 실행하기
        act = ActionChains(dr) # 동작 실행 코드 지정
    
        id = app_id    # 아이디 입력받기
        password = app_pw    # 비밀번호 입력받기
        act.send_keys_to_element(id_box, '{}'.format(id)).send_keys_to_element(password_box, '{}'.format(password)).click(login_button).perform()    
        time.sleep(3)
        
    except NoSuchElementException as e : 
        """
         - if already login-ed
        """
        dr.get('https://dataservice.koscom.co.kr/krx/approval-list')  
        dr.maximize_window()
        dr.implicitly_wait(10)  # 창이 뜰때까지 기다림
        
    
# 테스트 코드
ilogin()

# %% (1)-(2) Check iframes 
# What iframes exist : Not working 
# iframes = dr.find_element(By.CSS_SELECTOR, 'iframe')
# for iframe in iframes:
#     print(iframe.get_attribute('name'))

# %% (2) Table iter 
# %% (2)-(1) For iter
# ○ [파이썬] 웹에서 자료실 파일 다운로드하는 크롤러 만들기 : https://calmlife.tistory.com/5
"""
 - Case 1 : One Table
     <사전확인>
    - ver1. ex)
   ☞ 
   
   - ver2.-표1 ex) https://dataservice.koscom.co.kr/krx/100562/approval-detail (알파프라임)
   ☞ //*[@id="contents"]/div[5]/div[2]/div[1]/table/tbody/tr[1]/td[1] (OK)
    - ver2.-표2 ex) https://dataservice.koscom.co.kr/krx/100562/approval-detail (알파프라임)
    ☞ //*[@id="contents"]/div[5]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1] (error)
   
     <해지> 
     - ver1. ex) 
    ☞ 
    
     - ver2. ex) https://dataservice.koscom.co.kr/krx/100574/approval-detail  
    ☞ //*[@id="contents"]/div[5]/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[1] (Error) ▶ (a)
    
 - Case 2 : Two Table 
 - Case 3 : No Table ex) https://dataservice.koscom.co.kr/krx/100568/approval-detail
 - Case 4 : Error such like (a)
     
 -주석 有 (Case 1+2) ex) https://dataservice.koscom.co.kr/krx/100562/approval-detail
    <1번째>
    ☞ (하나만 있는 경우) //*[@id="contents"]/div[5]/div[2]/div[1]/div
    ☞ //*[@id="contents"]/div[5]/div[2]/div[1]/div[1]
    ☞ //*[@id="contents"]/div[5]/div[2]/div[1]/div[2]
    ☞ (새끼) //*[@id="contents"]/div[5]/div[2]/p[2]/span
    #contents > div.post-view.basic > div.cnts > p:nth-child(3) > span
    
    <2번째>
    ☞ //*[@id="contents"]/div[5]/div[2]/div[1]/div[4]
    //*[@id="contents"]/div[5]/div[2]/div[1]/div[2]
    
    
"""
from itertools import product

num = 100579


def Table_iter(num) :
    case_4 = []
    url = "https://dataservice.koscom.co.kr/krx/" + str(num) + "/approval-detail" # 100579 will be converted to parameter
    dr.get(url)
    dr.maximize_window()
    
    ######################### subject ######################### 
    time.sleep(5) # For Loading 
    wts_sub = dr.find_element(By.XPATH, '//*[@id="contents"]/div[5]/div[1]/span') # title
    wts_sub = wts_sub.text[15:][:len(wts_sub.text)-8] 
    
    #=========================================================================
    ######################### content ↓ ######################### 
    
    ######################### Case 1 ######################### 
    #=========================================================================
    Max_rows = 20
    Rg = range(1, Max_rows)  
    Rg_col = range(1, 7) # fixed
    
    full_list = [] # will be used to make DF 
    for i, j in product(Rg, Rg_col) :
        try : 
            wts = dr.find_element(By.XPATH, '//*[@id="contents"]/div[5]/div[2]/div[1]/table/tbody/tr[' + str(i) + ']/td[' + str(j) +']') 
            if wts.text[0:2] == "구분" :
                print("Shit!!! Case4")
                case_4.append(wts_sub)
                break
                            
            full_list.append(wts.text)
        except NoSuchElementException as e:
            print("Not Enough Time Or End of the table")
            break
    
    # 주석 前 합계 줄에 " " 1개 추가 
    try : 
        full_list.append(" ")
    except : 
        pass
    
    #=========================================================================
    # ---------------------- 주석(Case 1) ---------------------- 
    #=========================================================================
    Max_rows_note = 8
    Rg_note = range(1, Max_rows_note)
    
    """
    # 주석 하나만 있을 경우에도 필요치 X (`23.2.7 17:46)
    try : 
        wts = dr.find_element(By.XPATH, '//*[@id="contents"]/div[5]/div[2]/div[1]/div') 
        print(wts.text)
        full_list.append("주석")
        full_list.append(wts.text)
        full_list.extend(["-" for i in range(1, 5)])
    except NoSuchElementException as e:
        print("Multiple notes")
    """
    
    for i in Rg_note :
        try : 
            wts = dr.find_element(By.XPATH, '//*[@id="contents"]/div[5]/div[2]/div[1]/div[' + str(i) + ']')                                    
            if wts.text[0:2] == "구분" :
                print("Shit!!! Case4")
                case_4.append(wts_sub)
                break
                                
            full_list.append("주석")
            full_list.append(wts.text)
            full_list.extend(["-" for i in range(1, 5)]) # # of No data ← 4

        except NoSuchElementException as e:
            print("Only one note OR No more notes")
            break    
    
    for i in Rg_note :
        try : 
            wts = dr.find_element(By.XPATH, '//*[@id="contents"]/div[5]/div[2]/p[' + str(i) + ']/span')           
            if wts.text[0:2] == "구분" :
                print("Shit!!! Case4")
                case_4.append(wts_sub)
                break
            
            full_list.append("주석")                    
            full_list.append(wts.text)
            full_list.extend([" " for i in range(1, 5)]) # # of No data ← 4

        except NoSuchElementException as e:
            print("Only one note OR No more notes")
            break    
    
    #=========================================================================
    #=========================================================================
    ######################### Case 2 ######################### 
    #=========================================================================
    #=========================================================================
    for i, j in product(Rg, Rg_col) :
        try : 
            wts = dr.find_element(By.XPATH, '//*[@id="contents"]/div[5]/div[2]/div[1]/div[3]/table/tbody/tr[' + str(i) + ']/td[' + str(j) + ']') 
            if wts.text[0:2] == "구분" :
                print("Shit!!! Case4")
                case_4.append(wts_sub)
                break
                                
            full_list.append(wts.text)
        except NoSuchElementException as e:
            print("Not Enough Time \ Or End of the table")
            break

    # 주석 前 합계 줄에 " " 1개 추가 
    try : 
        full_list.append(" ")
    except : 
        pass
        
    # ---------------------- 주석(Case 2) ---------------------- 
    # should be edited (multiple notes) - wts link 
    for i in Rg_note :
        try : 
            wts = dr.find_element(By.XPATH, '//*[@id="contents"]/div[5]/div[2]/div[' + str(i) + ']/div[4]')                            
            if wts.text[0:2] == "구분" :
                print("Shit!!! Case4")
                case_4.append(wts_sub)
                break
                                
            full_list.append("주석")
            full_list.append(wts.text)
            full_list.extend(["-" for i in range(1, 5)]) # # of No data ← 4

        except NoSuchElementException as e:
            print("Only one note OR No more notes")
            break    
            
    #=========================================================================
    #=========================================================================
    ######################### DataFrame 作 ######################### 
    #=========================================================================
    #=========================================================================
    """
     - list → 6개 단위로 df 作
    """
    try :
        # at the last of the df → # of firms
        full_list_temp = ["-" for i in range(1, 6)]
        full_list_temp.extend(full_list)
        full_list = full_list_temp.copy()
        full_list.insert(0, wts_sub)
        
        # full_list.append(wts_sub) 
        # full_list.extend(["-" for i in range(1, 6)])
        
        n = 6 # # of columns 
        full_list_c = [full_list[i * n:(i+1) * n] for i in range(len(full_list) + n-1 // n)]
        
        full_list_c_last = [i for i in full_list_c if i != []] # error (공란 있을 시)
        # full_list_c_last_except = full_list_c_last[0:len(full_list_c_last) - 1] # omited(`23.2.8 01:56)
        full_list_c_last_except = full_list_c_last
        
        # print(full_list_c_last_except)
        
        # Making DF 
        columns = ["구분", "상품명", "화폐단위", "이용료(월)", "제공방식",
                    "계약 효력일"]
        # columns = ["col_1", "col_2", "col_3", "col_4", "col_5",
        #             "col_6"]
        
        df = pd.DataFrame(full_list_c_last_except)
        
        # change columns index 
        col = df.columns.to_numpy()
        # col = col[[5, 0, 1, 2, 3, 4]]
        df = df[col]
        
        df.columns = columns
        # print(full_list_c_last_except)
        print(wts_sub)
        df.to_csv(wts_sub + "_" + str(num) + ".csv", encoding = "euc-kr")
    
        

    ######################### Case 3 ######################### 
    except ValueError as e:
        Case_3_list = []
        Rg = range(1, Max_rows) 
        for i in Rg :    
            try : 
                wts = dr.find_element(By.XPATH, '//*[@id="contents"]/div[5]/div[2]/div[' + str(i) + ']/span') 
                Case_3_list.append(wts.text)
                df = pd.DataFrame(Case_3_list)
                df.to_csv(wts_sub + "_" + str(num) + ".csv", encoding = "euc-kr")
            except : 
                pass

    print(num)
    return(case_4)
        
# %% Edit
start = 100562 # 100562, 100574
end = 100562
case_4_result = [] # Case 4 → 예외 처리
for i in range(start, end+1) :
    TI = Table_iter(i)   
    case_4_result.append(TI)

# %% Iter_result
start = 100171 # 100562, 100574 
# end = 100596
end = 100172
case_4_result = [] # Case 4 → 예외 처리
case_4_result_i = []
result_error = []

for i in range(start, end+1) :
    try : 
        TI = Table_iter(i)           
        case_4_result.append(TI)
        if TI != [] :
            case_4_result_i.append(i)
    except NoSuchElementException as e :
        result_error.append(i)
        
    
    
# %% (3) download attachment
from selenium import webdriver
import time
import pyautogui as pag
import pyperclip as py
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
 - It can be useful :
     chrome_options.add_experimental_option("prefs",{'download.prompt_for_download': True})

 - Case 1 : ∃ 계약서류, 추가 첨부파일
    - ver1. ex) https://dataservice.koscom.co.kr/krx/100617/approval-detail
   * 주문서 : //*[@id="contents"]/div[3]/dl[3]/dd[1]/a/span[2] 
    ☞ print_dialog_first
    
   * 요약본 : //*[@id="contents"]/div[3]/dl[3]/dd[2]/a/span[2]
    ☞ print_dialog_first
    
   * 이용조건 : //*[@id="contents"]/div[3]/dl[4]/dd[1]/a/span[2]
   ☞ just click
   
   * 계약조건 : //*[@id="contents"]/div[3]/dl[4]/dd[2]/a/span[2]
   ☞ just click
   
   * 추가첨부_1 : //*[@id="contents"]/div[5]/dl[1]/dd/ul/li[1]/a/span[2]
   ☞ just click
   
   * 추가첨부_2 : //*[@id="contents"]/div[5]/dl[1]/dd/ul/li[2]/a/span[2]
   ☞ just click
   
"""
######################### Setting : should be excecuted #########################
def print_dialog_first(title, sub_title, driver):
    time.sleep(2)
    pag.press('enter') # "Print" Button     
    time.sleep(2)
    
    # Type subject 
    py.copy(title + "_" + sub_title) # copy to clipboard (Korean not supported in pag.typewrite)
    pag.hotkey('ctrl', 'v') 
    pag.press('enter') # "Print" Button     
    
    time.sleep(2) # For Loading 
    # ==========# It is "NO" for duplicated files(For safety, twice)==========
    keyboard.send("esc") 
    time.sleep(2) # For Loading 
    keyboard.send("Enter")
    time.sleep(1) # For Loading 
    
    keyboard.send("esc") 
    time.sleep(2) # For Loading 
    keyboard.send("Enter")
    time.sleep(1) # For Loading 
    
    # ====================# It is for click the "X"====================
    # dr.switch_to.window(dr.currnet_window_handle)
    webdriver.ActionChains(dr).send_keys(Keys.ESCAPE).perform()
    keyboard.send("esc") 
    time.sleep(2) # For Loading 
    keyboard.send("Enter")
    time.sleep(1) # For Loading 
    
    dr.switch_to.window(dr.currnet_window_handle)
    keyboard.send("esc") 
    time.sleep(2) # For Loading 
    keyboard.send("Enter")
    time.sleep(1) # For Loading 

def just_save_dialog_first(title, sub_title, driver):
    """
     - IF ∃ 2 or more files → More "enter" is needed (up to 4 files)
    """
    time.sleep(2)
    pag.press('enter') # "Print" Button     
    time.sleep(2)
    pag.press('enter') # "Print" Button     
    time.sleep(2)
    pag.press('enter') # "Print" Button     
    time.sleep(2)
    pag.press('enter') # "Print" Button     
    time.sleep(2)
    
    # # Type subject 
    # py.copy(title + "_" + sub_title) # copy to clipboard (Korean not supported in pag.typewrite)
    # pag.hotkey('ctrl', 'v') 
    # pag.press('enter') # "Print" Button     
    
    time.sleep(2) # For Loading 
    
    # ==========# It is "NO" for duplicated files(For safety, twice)==========
    # keyboard.send("esc") 
    # time.sleep(2) # For Loading 
    # keyboard.send("Enter")
    # time.sleep(2) # For Loading 
        
    # keyboard.send("esc") 
    # time.sleep(2) # For Loading 
    # keyboard.send("Enter")
    # time.sleep(2) # For Loading 


url = "https://dataservice.koscom.co.kr/krx/100617/approval-detail"
dr.get(url)
dr.maximize_window()
time.sleep(5)

######################### title & date #########################
"""
# title ← Same as wts_sub
"""

title = dr.find_element(By.XPATH, '//*[@id="contents"]/div[5]/div[1]/span') # title
title = title.text[15:][:len(title.text)-8] 

date = dr.find_element(By.XPATH, '//*[@id="contents"]/div[3]/dl[2]/dd[2]') # date
date = date.text

######################### attachment & def #########################
""" Example code
attach_1 = dr.find_element(By.XPATH, '//*[@id="contents"]/div[3]/dl[3]/dd[1]/a/span[2]') # 주문서
attach_1.click()

time.sleep(5) # For Loading 
print_dialog_first(title = title, sub_title = "주문서" + "(" + date + ")")
"""

######################### Iteration #########################
sub_name_dict = {
    "주문서" : '//*[@id="contents"]/div[3]/dl[3]/dd[1]/a/span[2]', 
    "요약본" : '//*[@id="contents"]/div[3]/dl[3]/dd[2]/a/span[2]',
    "이용조건" : '//*[@id="contents"]/div[3]/dl[4]/dd[1]/a/span[2]', 
    "계약조건" : '//*[@id="contents"]/div[3]/dl[4]/dd[2]/a/span[2]', 
    "추가첨부_1" : '//*[@id="contents"]/div[5]/dl[1]/dd/ul/li[1]/a/span[2]', 
    "추가첨부_2" : '//*[@id="contents"]/div[5]/dl[1]/dd/ul/li[2]/a/span[2]'
    }
"""
 - `23.3.2 : 문제 發 - esc 문제는 해결되었으나, 현재 중복 다운로드 등 문제 상존 
"""
for i, (sub_title, xpath) in enumerate(sub_name_dict.items()) : 
    if i <= 1 : 
        try : 
            time.sleep(5) # For Loading 
            attach = dr.find_element(By.XPATH, xpath) # 주문서, 요약본 ... 
            
            time.sleep(2) # For Loading 
            keyboard.send("esc") # pag.press('Esc') is not working / and sometimes keyboard.send not work 
            
            # time.sleep(2) # For Loading 
            # keyboard.send("esc") # pag.press('Esc') is not working
            
            attach.click()
            
            time.sleep(5) # For Loading 
            print_dialog_first(title = title, sub_title = sub_title + "(" + date + ")", driver = dr)
            # pag.press(pag.KEYBOARD_KEYS["esc"])
            # pag.press(pag.KEYBOARD_KEYS["esc"])
            # pag.press('esc') 
        except : 
            pass
        
    else : 
        try : 
            time.sleep(5) # For Loading 
            attach = dr.find_element(By.XPATH, xpath) # 이용조건, 계약조건 ... 
            attach.click()
            just_save_dialog_first(title = title, sub_title = sub_title + "(" + date + ")", driver = dr)
        except : 
            pass

# %% 
# li_1 = dr.find_elements(By.LINK_TEXT, "다운로드")

title_content = dr.find_element_by_xpath("//h3[@class='body']")
title_content.find_elements(By.LINK_TEXT, "다운로드")
print(title_content)
