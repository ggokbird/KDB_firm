
# %% (0) Working Directory
import os
import zipfile
import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import SessionNotCreatedException
from bs4 import BeautifulSoup
import pandas as pd
import time
from time import sleep

start_date = '20230101'
end_date = '20230331'
filePath = 'C:\\Users\\KRX\\Desktop\\201021'

def createAndSetWorkingDir(directory):
    # chrome_version = "118.0.5993.70"
    chrome_version = "119.0.6045.105"
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)
    print(f"Current working directory is now set to: {os.getcwd()}")

createAndSetWorkingDir(filePath)

def download_chromedriver(chrome_version):
    zip_path = os.path.join(filePath, "chromedriver.zip")
    extract_folder = os.path.join(filePath, "chromedriver-win32")

    url = f"https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{chrome_version}/win32/chromedriver-win32.zip"
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception(f"Failed to download ChromeDriver for version {chrome_version}. Status code: {response.status_code}")

    with open(zip_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print("Starting to unzip the chromedriver...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    print("Unzipping completed.")

    chromedriver_exe_path = os.path.join(extract_folder, "chromedriver.exe")

    # Change the working directory to the extracted folder
    os.chdir(extract_folder)
    print(f"Working directory changed to: {os.getcwd()}")

    if os.path.exists(chromedriver_exe_path):
        return chromedriver_exe_path
    else:
        raise FileNotFoundError(f"'chromedriver.exe' was not found in the extracted directory: {extract_folder}")

try:
    # chrome_v = "118.0.5993.70"
    chrome_v = "119.0.6045.105"
    print(f"Expected Chrome version: {chrome_v}")
    chromedriver_path = download_chromedriver(chrome_v)
    print(f"Downloaded ChromeDriver path: {chromedriver_path}")
    
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.google.com")
    driver.quit()

except SessionNotCreatedException as e:
    print(f"Error encountered: {str(e)}")
    match = re.search(r"Chrome version (\d+\.\d+\.\d+)", str(e))
    if match:
        chrome_version_detected = match.group(1)
        print(f"Detected Chrome version from error: {chrome_version_detected}")
        try:
            chromedriver_path = download_chromedriver(chrome_version_detected)
            print(f"Downloaded ChromeDriver path for detected version: {chromedriver_path}")
            
            options = webdriver.ChromeOptions()
            options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            service = Service(executable_path=chromedriver_path)
            driver = webdriver.Chrome(service=service, options=options)
            driver.get("https://www.google.com")
            driver.quit()
        except Exception as ex:
            print(f"Error while trying to download ChromeDriver for detected version: {ex}")

# %% (1)-(1) Session : Not working → login input 用
"""
○ Validating XPath Selectors in the browser (chrome Dev Tools)
$x("//html");
 ex) $x("//#contents > div.login-wrap > div > form > div:nth-child(1) > div > div > input")
document.querySelectorAll("<YOUR_CSS_SELECTOR>")
 ex) document.querySelectorAll("//#contents > div.login-wrap > div > form > div:nth-child(1) > div > div > input")
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

app_id = 'goguma@krx.co.kr'
app_pw = "wkrwjs12!@"

dr = webdriver.Chrome()
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

# %% 231101 표가 2개 있는 경우는 잘 Working 하나 표 1개에는 제대로 작동하지 않는 코드 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

def login(driver, app_id, app_pw):
    try:
        id_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')
        password_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[2]/div/div/input')
        login_button = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[3]/button')
        
        act = ActionChains(driver)
        act.send_keys_to_element(id_box, app_id).send_keys_to_element(password_box, app_pw).click(login_button).perform()
        time.sleep(3)
    except NoSuchElementException:
        driver.get('https://dataservice.koscom.co.kr/krx/approval-list')
        driver.maximize_window()
        driver.implicitly_wait(10)

def table_iter(num, driver):
    base_url = f"https://dataservice.koscom.co.kr/krx/{num}/approval-detail"
    driver.get(base_url)

    # div 내부에 직접적으로 table이 위치하는 경우 (표가 1개 있는 경우)
    table_container_single = driver.find_elements(By.CSS_SELECTOR, 'div[style*="font-size: 18px"]')
    
    # div 내부에 다른 div를 포함하는 경우 (표가 2개 있는 경우)
    table_container_double = driver.find_elements(By.CSS_SELECTOR, 'div[style*="font-size: 18px"] div[style*="font-size: 18px"]')
    
    if table_container_single:
        table_containers = table_container_single
    else:
        table_containers = table_container_double

    result = []
    for container in table_containers:
        tables = container.find_elements(By.TAG_NAME, 'table')
        for table in tables:
            rows = table.find_elements(By.CSS_SELECTOR, 'tr')
            for row in rows:
                result.append(row.text)

        # Capture the note below the table
        notes = container.find_elements(By.CSS_SELECTOR, 'div[style*="margin-top:10px"]')
        for note in notes:
            result.append(note.text)

    return result


def convert_to_dataframes(data_list):
    headers = ["구분", "상품명", "화폐단위", "이용료(월)", "제공방식", "계약 효력일"]
    
    tables_data = []
    current_table = []
    
    for data in data_list:
        # 헤더를 만나면 새로운 테이블 시작
        if data.startswith('구분'):
            if current_table:  # 이전 테이블 데이터가 있으면 저장
                tables_data.append(current_table)
                current_table = []
            # 헤더 줄은 스킵
            continue
        else:
            # 특별한 split 로직으로 "계약 효력일" 처리
            split_data = data.rsplit(' ', 1)
            first_parts = split_data[0].rsplit(' ', len(headers)-2)
            current_table.append(first_parts + [split_data[1]])
    
    # 마지막 테이블 데이터 저장
    if current_table:
        tables_data.append(current_table)
    
    # 데이터프레임으로 변환
    dataframes = []
    for table in tables_data:
        # DataFrame 생성
        df = pd.DataFrame(table, columns=headers)
        dataframes.append(df)

    return dataframes

app_id = 'goguma@krx.co.kr'
app_pw = "wkrwjs12!@"

driver = webdriver.Chrome()
driver.set_window_size(1200, 2400)
driver.get('https://dataservice.koscom.co.kr/login?returnUrl=/krx/approval-list')
driver.maximize_window()
driver.implicitly_wait(10)

# 로그인
login(driver, app_id, app_pw)

# 원하는 데이터 가져오기
num = 100562 # 표 2개 
# num = 100561 # 표 1개 
data_result = table_iter(num, driver)

# 데이터를 DataFrame으로 변환
dataframes = convert_to_dataframes(data_result)
for df in dataframes:
    print(df)

# %% 231101 표가 2개 + 표 1개에는 제대로 작동
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

def login(driver, app_id, app_pw):
    try:
        id_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')
        password_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[2]/div/div/input')
        login_button = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[3]/button')
        
        act = ActionChains(driver)
        act.send_keys_to_element(id_box, app_id).send_keys_to_element(password_box, app_pw).click(login_button).perform()
        time.sleep(3)
    except NoSuchElementException:
        driver.get('https://dataservice.koscom.co.kr/krx/approval-list')
        driver.maximize_window()
        driver.implicitly_wait(10)

def table_iter(num, driver):
    base_url = f"https://dataservice.koscom.co.kr/krx/{num}/approval-detail"
    driver.get(base_url)

    # 테이블의 모든 행(row)를 가져옴
    rows = driver.find_elements(By.CSS_SELECTOR, 'table > tbody > tr')

    result = []
    for row in rows:
        cells = row.find_elements(By.CSS_SELECTOR, 'td')
        result.append([cell.text for cell in cells])
            
    return result

def convert_to_dataframes(data_list):
    headers = ["구분", "상품명", "화폐단위", "이용료(월)", "제공방식", "계약 효력일"]
    df = pd.DataFrame(data_list, columns=headers)
    return [df]


app_id = 'goguma@krx.co.kr'
app_pw = "wkrwjs12!@"

driver = webdriver.Chrome()
driver.set_window_size(1200, 2400)
driver.get('https://dataservice.koscom.co.kr/login?returnUrl=/krx/approval-list')
driver.maximize_window()
driver.implicitly_wait(10)

# Login
login(driver, app_id, app_pw)

# Extract data
num = 100561 # Table count: 2
# num = 100561 # Table count: 1 
data_result = table_iter(num, driver)

# Convert the data to DataFrame
dataframes = convert_to_dataframes(data_result)
for df in dataframes:
    print(df)
    
# %% 231101 주석 추가
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

def login(driver, app_id, app_pw):
    try:
        id_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')
        password_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[2]/div/div/input')
        login_button = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[3]/button')
        
        act = ActionChains(driver)
        act.send_keys_to_element(id_box, app_id).send_keys_to_element(password_box, app_pw).click(login_button).perform()
        time.sleep(3)
    except NoSuchElementException:
        driver.get('https://dataservice.koscom.co.kr/krx/approval-list')
        driver.maximize_window()
        driver.implicitly_wait(10)

def table_iter(num, driver):
    base_url = f"https://dataservice.koscom.co.kr/krx/{num}/approval-detail"
    driver.get(base_url)

    # 페이지에서 모든 행을 기다림
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'table > tbody > tr'))
    )
    
    # 테이블의 모든 행(row)를 가져옴
    rows = driver.find_elements(By.CSS_SELECTOR, 'table > tbody > tr')
    result = []
    for row in rows:
        cells = row.find_elements(By.CSS_SELECTOR, 'td')
        result.append([cell.text for cell in cells])
    
    # 페이지에서 주석이 포함된 모든 div를 기다림
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@style, 'margin-top:') and contains(text(), '주')]"))
    )
    
    # 노트(주석)을 가져옴
    notes = driver.find_elements(By.XPATH, "//div[contains(@style, 'margin-top:') and contains(text(), '주')]")
    notes_text = [note.text for note in notes]

    return result, notes_text

def convert_to_dataframes(data_list, notes_list):
    headers = ["구분", "상품명", "화폐단위", "이용료(월)", "제공방식", "계약 효력일"]
    df = pd.DataFrame(data_list, columns=headers)
    notes_df = pd.DataFrame(notes_list, columns=["Notes"])
    return df, notes_df

app_id = 'goguma@krx.co.kr'
app_pw = "wkrwjs12!@"

driver = webdriver.Chrome()
driver.set_window_size(1200, 2400)
driver.get('https://dataservice.koscom.co.kr/login?returnUrl=/krx/approval-list')
driver.maximize_window()
driver.implicitly_wait(10)

# Login
login(driver, app_id, app_pw)

# Extract data
num = 100562 # Example number, it can be different
data_result, notes_result = table_iter(num, driver)

# Convert the data to DataFrame
data_df, notes_df = convert_to_dataframes(data_result, notes_result)

# Display the data
print(data_df)
print(notes_df)

# Make sure to quit the driver after your scraping job is done
# driver.quit()

# %% 231102 셀레니움을 이용한 웹사이트 로그인 및 다운로드 링크 클릭 로깅
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import pyautogui
import keyboard

def login(driver, app_id, app_pw):
    # 로그인 시도 전 로그 출력
    print("[INFO] 로그인을 시도합니다.")
    id_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')
    password_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[2]/div/div/input')
    login_button = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[3]/button')
    
    act = ActionChains(driver)
    act.send_keys_to_element(id_box, app_id).send_keys_to_element(password_box, app_pw).click(login_button).perform()
    time.sleep(3)

def table_iter(num, driver):
    # 상세 페이지 이동 전 로그 출력
    print(f"[INFO] 상세 페이지로 이동합니다: {num}")
    base_url = f"https://dataservice.koscom.co.kr/krx/{num}/approval-detail"
    driver.get(base_url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'table > tbody > tr'))
    )
    
    rows = driver.find_elements(By.CSS_SELECTOR, 'table > tbody > tr')
    result = []
    for row in rows:
        cells = row.find_elements(By.CSS_SELECTOR, 'td')
        result.append([cell.text for cell in cells])
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@style, 'margin-top:') and contains(text(), '주')]"))
    )
    
    notes = driver.find_elements(By.XPATH, "//div[contains(@style, 'margin-top:') and contains(text(), '주')]")
    notes_text = [note.text for note in notes]

    return result, notes_text

def convert_to_dataframes(data_list, notes_list):
    # 데이터프레임 변환 전 로그 출력
    print("[INFO] 데이터를 데이터프레임으로 변환합니다.")
    headers = ["구분", "상품명", "화폐단위", "이용료(월)", "제공방식", "계약 효력일"]
    df = pd.DataFrame(data_list, columns=headers)
    notes_df = pd.DataFrame(notes_list, columns=["Notes"])
    return df, notes_df

def handle_print_dialog():
    # 인쇄 대화 상자 처리 전 로그 출력
    print("[INFO] 인쇄 대화 상자를 처리합니다.")
    time.sleep(2)
    pyautogui.press('enter')  # "Print" Button
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v') 
    pyautogui.press('enter')  # "Print" Button
    time.sleep(2)
    keyboard.send("esc")
    time.sleep(2)
    keyboard.send("enter")
    time.sleep(1)
    keyboard.send("esc")

# capabilities = DesiredCapabilities.CHROME
# capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}

# driver = webdriver.Chrome(desired_capabilities=capabilities)
# driver = webdriver.Chrome()
# ChromeOptions 인스턴스 생성
chrome_options = webdriver.ChromeOptions()

# 로거 설정 추가
chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

# Chrome 드라이버 인스턴스 생성
driver = webdriver.Chrome(options=chrome_options)

app_id = 'goguma@krx.co.kr'
app_pw = "wkrwjs12!@"

driver.set_window_size(1200, 2400)
driver.get('https://dataservice.koscom.co.kr/login?returnUrl=/krx/approval-list')
driver.maximize_window()
driver.implicitly_wait(10)

login(driver, app_id, app_pw)

num = 100562  # Example number, adjust for actual use
data_result, notes_result = table_iter(num, driver)

data_df, notes_df = convert_to_dataframes(data_result, notes_result)

print(data_df)
print(notes_df)

print("[INFO] 다운로드 링크를 클릭합니다.")
download_links = driver.find_elements(By.CSS_SELECTOR, 'a.file-link[download]')
for index, link in enumerate(download_links):
    link_text = link.find_element(By.XPATH, ".//span[contains(@class, 'name')]").text
    try:
        if "이용조건" not in link_text:
            print(f"[INFO] 다운로드 링크 ({index}) 클릭.")
            driver.execute_script("arguments[0].click();", link)
            handle_print_dialog()  # 이용조건이 아닌 링크에 대해 인쇄 대화 상자 처리
        else:
            print(f"[INFO] '이용조건' 다운로드 링크 클릭, 별도의 인쇄 대화 상자 처리를 생략합니다.")
            driver.execute_script("arguments[0].click();", link)
            # '이용조건' 링크의 경우 별도의 처리가 필요없으므로 대기만 합니다.
            time.sleep(5)  # 다운로드가 시작되기를 기다립니다.
    except Exception as e:
        print(f"[ERROR] 다운로드 링크 클릭 오류: {e}")

# 브라우저 로그 출력
# print("[INFO] 브라우저 로그를 수집합니다.")
# logs = driver.get_log('browser')
# for log in logs:
#     print(log)

# driver.quit()


# driver.quit()

# %% 231104 Saction_id 미반영
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import warnings
from urllib3.exceptions import InsecureRequestWarning

# HTTPS 요청에 대한 경고를 비활성화
warnings.simplefilter('ignore', InsecureRequestWarning)


# 로그인 함수
def login(driver, app_id, app_pw):
    # 로그인 시도 전 로그 출력
    print("[INFO] 로그인을 시도합니다.")
    id_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')
    password_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[2]/div/div/input')
    login_button = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[3]/button')
    
    act = ActionChains(driver)
    act.send_keys_to_element(id_box, app_id).send_keys_to_element(password_box, app_pw).click(login_button).perform()
    time.sleep(3)

# 메인 실행 코드
if __name__ == "__main__":
    # 웹 드라이버 설정 (Selenium Wire를 사용하는 부분을 제거했습니다)
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        login(driver, 'goguma@krx.co.kr', 'wkrwjs12!@')
        time.sleep(5)  # 로그인 후 리다이렉트 대기
        driver.get('https://dataservice.koscom.co.kr/krx/approval-list')

        # Waiting for the table rows to be visible
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'tbody .el-table__row'))
        )

        # Assuming the document number is located in the fifth column (el-table_1_column_5)
        document_cells = driver.find_elements(By.CSS_SELECTOR, 'tbody .el-table__row .el-table_1_column_5 .cell')

        detail_urls = [
            f"https://dataservice.koscom.co.kr/krx/{cell.text.strip()}/approval-detail"
            for cell in document_cells if cell.text.strip() != ''
        ]

        for url in detail_urls:
            # HEAD 요청을 보내어 실제 URL을 얻습니다.
            response = requests.head(url, allow_redirects=True, verify=False)
            actual_url = response.url  # 리디렉트 된 후의 최종 URL
            print(actual_url)

    except TimeoutException:
        print("[ERROR] 페이지 로딩 시간 초과")
    finally:
        driver.quit()


# %% 231103
from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pandas as pd

def login(driver, app_id, app_pw):
    try:
        driver.get('https://dataservice.koscom.co.kr/login?returnUrl=/krx/approval-list')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')))
        
        id_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')
        password_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[2]/div/div/input')
        login_button = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[3]/button')
        
        actions = ActionChains(driver)
        actions.send_keys_to_element(id_box, app_id)
        actions.send_keys_to_element(password_box, app_pw)
        actions.click(login_button)
        actions.perform()
        
        WebDriverWait(driver, 10).until(EC.url_to_be('https://dataservice.koscom.co.kr/krx/approval-list'))
        
    except NoSuchElementException as e:
        print("[ERROR] One of the login elements could not be found.", e)
        driver.quit()
    except TimeoutException as e:
        print("[ERROR] Timeout occurred during login.", e)

def extract_data(driver, num):
    base_url = f"https://dataservice.koscom.co.kr/krx/{num}/approval-detail"
    driver.get(base_url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'table > tbody > tr'))
    )

    rows = driver.find_elements(By.CSS_SELECTOR, 'table > tbody > tr')
    result = []
    for row in rows:
        cells = row.find_elements(By.CSS_SELECTOR, 'td')
        result.append([cell.text for cell in cells])

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@style, 'margin-top:') and contains(text(), '주')]"))
    )

    notes = driver.find_elements(By.XPATH, "//div[contains(@style, 'margin-top:') and contains(text(), '주')]")
    notes_text = [note.text for note in notes]

    return result, notes_text

def convert_to_dataframes(data_list, notes_list):
    headers = ["구분", "상품명", "화폐단위", "이용료(월)", "제공방식", "계약 효력일"]
    df = pd.DataFrame(data_list, columns=headers)
    notes_df = pd.DataFrame(notes_list, columns=["Notes"])
    return df, notes_df

# 메인 실행 코드
if __name__ == "__main__":
    seleniumwire_options = {
        'connection_timeout': None,
        'verify_ssl': False,
    }

    driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options)

    try:
        # Login
        login(driver, 'goguma@krx.co.kr', 'wkrwjs12!@')

        # Extract data
        num = 100562 # Example number, replace with actual value if necessary
        data_result, notes_result = extract_data(driver, num)

        # Convert the data to DataFrame
        data_df, notes_df = convert_to_dataframes(data_result, notes_result)

        # Display the data
        print(data_df)
        print(notes_df)

    except Exception as e:
        print("[ERROR] An error occurred:", e)
    finally:
        driver.quit()

# %% 231105 1220 웹사이트 로그인 및 동적 JSON 데이터 추출 자동화 스크립트
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import json
import time
import gzip
import os
import traceback

# 로그인 함수
def login(driver, app_id, app_pw):
    print("[INFO] 로그인을 시도합니다.")
    driver.get('https://dataservice.koscom.co.kr/login?returnUrl=/krx/approval-list')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')))
    id_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')
    password_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[2]/div/div/input')
    login_button = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[3]/button')
    id_box.send_keys(app_id)
    password_box.send_keys(app_pw)
    login_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be('https://dataservice.koscom.co.kr/krx/approval-list'))

# 데이터 추출 함수
def table_iter(num, driver):
    print(f"[INFO] 상세 페이지로 이동합니다: {num}")
    base_url = f"https://dataservice.koscom.co.kr/krx/{num}/approval-detail"
    driver.get(base_url)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'table > tbody > tr')))
    rows = driver.find_elements(By.CSS_SELECTOR, 'table > tbody > tr')
    result = [[cell.text for cell in row.find_elements(By.CSS_SELECTOR, 'td')] for row in rows]
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@style, 'margin-top:') and contains(text(), '주')]")))
    notes = [note.text for note in driver.find_elements(By.XPATH, "//div[contains(@style, 'margin-top:') and contains(text(), '주')]")]
    return result, notes

# 데이터를 DataFrame으로 변환하는 함수
def convert_to_dataframes(data_list, notes_list):
    headers = ["구분", "상품명", "화폐단위", "이용료(월)", "제공방식", "계약 효력일"]
    df = pd.DataFrame(data_list, columns=headers)
    notes_df = pd.DataFrame(notes_list, columns=["Notes"])
    return df, notes_df

# JSON 데이터를 파일에 저장하는 함수
def save_json_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 메인 실행 코드입니다.
if __name__ == "__main__":
    seleniumwire_options = {
        'connection_timeout': None,
        'verify_ssl': False,
    }
    driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options)

    try:
        login(driver, 'goguma@krx.co.kr', 'wkrwjs12!@')

        # 데이터 추출
        num = '100562'
        data_result, notes_result = table_iter(num, driver)
        data_df, notes_df = convert_to_dataframes(data_result, notes_result)

        # 클릭할 다운로드 버튼 요소를 찾습니다.
        download_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.iconset.icon-down-attach'))
        )
        download_link.click()  # 요소를 클릭합니다.

        # 클릭 후에 발생하는 요청을 필터링합니다.
        time.sleep(3)  # 네트워크 트래픽을 기다립니다.
        json_responses = []
        for request in driver.requests:
            if request.response and 'application/json' in request.response.headers.get('Content-Type', ''):
                print(f"요청 URL: {request.url}")
                print(f"응답 코드: {request.response.status_code}")
                content_encoding = request.response.headers.get('Content-Encoding', '')
                if 'gzip' in content_encoding:
                    json_data = gzip.decompress(request.response.body).decode('utf-8')
                else:
                    json_data = request.response.body.decode('utf-8')
                
                # JSON 데이터를 파이썬 객체로 변환하고 리스트에 추가합니다.
                json_obj = json.loads(json_data)
                # 요청 URL을 JSON 객체에 추가합니다.
                # 만약 json_obj가 리스트 형태라면 각 항목에 URL을 추가해야 합니다.
                if isinstance(json_obj, list):
                    for item in json_obj:
                        if isinstance(item, dict):
                            item['request_url'] = request.url
                    json_responses.extend(json_obj)
                else:
                    json_obj['request_url'] = request.url
                    json_responses.append(json_obj)

        # JSON 데이터를 파일에 저장합니다.
        save_json_to_file(json_responses, 'output.json')
        
        # 파일에서 DataFrame으로 변환합니다.
        # DataFrame 생성 전에 json_responses 내부의 모든 원소가 딕셔너리 형인지 확인합니다.
        if all(isinstance(item, dict) for item in json_responses):
            df_from_json = pd.json_normalize(json_responses, sep='_')
            print(df_from_json)  # DataFrame 출력
        else:
            print("Error: Not all items in json_responses are dictionaries.")

        # 원래 데이터 프레임 출력
        print(data_df)
        print(notes_df)

    except Exception as e:
        print("[ERROR] An error occurred:", traceback.format_exc())
    finally:
        driver.quit()
        if os.path.exists('output.json'):
            os.remove('output.json')

# %% 231106 자동화된 웹 브라우저를 통한 로그인 및 데이터 추출 시스템 (헤더 포함)
from seleniumwire import webdriver  # Selenium Wire를 임포트합니다.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import json
import time
import gzip
import os
import traceback

# 로그인 함수
def login(driver, app_id, app_pw):
    print("[INFO] 로그인을 시도합니다.")
    driver.get('https://dataservice.koscom.co.kr/login?returnUrl=/krx/approval-list')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')))
    id_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')
    password_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[2]/div/div/input')
    login_button = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[3]/button')
    id_box.send_keys(app_id)
    password_box.send_keys(app_pw)
    login_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be('https://dataservice.koscom.co.kr/krx/approval-list'))

# 데이터 추출 함수
def table_iter(num, driver):
    print(f"[INFO] 상세 페이지로 이동합니다: {num}")
    base_url = f"https://dataservice.koscom.co.kr/krx/{num}/approval-detail"
    driver.get(base_url)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'table > tbody > tr')))
    rows = driver.find_elements(By.CSS_SELECTOR, 'table > tbody > tr')
    result = [[cell.text for cell in row.find_elements(By.CSS_SELECTOR, 'td')] for row in rows]
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@style, 'margin-top:') and contains(text(), '주')]")))
    notes = [note.text for note in driver.find_elements(By.XPATH, "//div[contains(@style, 'margin-top:') and contains(text(), '주')]")]
    return result, notes

# 데이터를 DataFrame으로 변환하는 함수
def convert_to_dataframes(data_list, notes_list):
    headers = ["구분", "상품명", "화폐단위", "이용료(월)", "제공방식", "계약 효력일"]
    df = pd.DataFrame(data_list, columns=headers)
    notes_df = pd.DataFrame(notes_list, columns=["Notes"])
    return df, notes_df

# JSON 데이터를 파일에 저장하는 함수
def save_json_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 메인 실행 코드
if __name__ == "__main__":
    seleniumwire_options = {
        'connection_timeout': None,
        'verify_ssl': False,
    }
    driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options)

    try:
        # 실제 사용자 정보로 변경해야 합니다.
        login(driver, 'goguma@krx.co.kr', 'wkrwjs12!@')

        # 데이터 추출
        num = '100562'
        data_result, notes_result = table_iter(num, driver)
        data_df, notes_df = convert_to_dataframes(data_result, notes_result)

        # 클릭할 다운로드 버튼 요소를 찾습니다.
        download_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.iconset.icon-down-attach'))
        )
        download_link.click()  # 요소를 클릭합니다.

        # 클릭 후에 발생하는 요청을 필터링합니다.
        time.sleep(3)  # 네트워크 트래픽을 기다립니다.
        for request in driver.requests:
            if request.response and 'application/json' in request.response.headers.get('Content-Type', ''):
                print(f"요청 URL: {request.url}")
                print(f"응답 코드: {request.response.status_code}")
                print(f"요청 헤더: {request.headers}")
                if request.body:
                    # 요청 본문이 있다면 출력합니다.
                    print(f"요청 바디: {request.body.decode('utf-8', 'ignore')}")
                else:
                    print("요청 바디: None")
                
                # 응답 본문을 출력할 수도 있습니다.
                # 만약 응답이 크다면 이를 출력하지 않거나 적절하게 처리해야 할 수 있습니다.
                # if request.response.body:
                #     print(f"응답 바디: {request.response.body.decode('utf-8', 'ignore')}")

        # 원래 데이터 프레임 출력
        print(data_df)
        print(notes_df)

    except Exception as e:
        print("[ERROR] An error occurred:", traceback.format_exc())
    finally:
        driver.quit()

# %% 231106 1130 Selenium Wire를 활용한 웹 자동 로그인 및 인증 헤더 추출을 통한 API 호출 자동화
from seleniumwire import webdriver  # Selenium Wire를 임포트합니다.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import json
import time
import gzip
import os
import traceback

# 로그인 함수
def login(driver, app_id, app_pw):
    print("[INFO] 로그인을 시도합니다.")
    driver.get('https://dataservice.koscom.co.kr/login?returnUrl=/krx/approval-list')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')))
    id_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')
    password_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[2]/div/div/input')
    login_button = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[3]/button')
    id_box.send_keys(app_id)
    password_box.send_keys(app_pw)
    login_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be('https://dataservice.koscom.co.kr/krx/approval-list'))

# 데이터 추출 함수
def table_iter(num, driver):
    print(f"[INFO] 상세 페이지로 이동합니다: {num}")
    base_url = f"https://dataservice.koscom.co.kr/krx/{num}/approval-detail"
    driver.get(base_url)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'table > tbody > tr')))
    rows = driver.find_elements(By.CSS_SELECTOR, 'table > tbody > tr')
    result = [[cell.text for cell in row.find_elements(By.CSS_SELECTOR, 'td')] for row in rows]
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@style, 'margin-top:') and contains(text(), '주')]")))
    notes = [note.text for note in driver.find_elements(By.XPATH, "//div[contains(@style, 'margin-top:') and contains(text(), '주')]")]
    return result, notes

# 데이터를 DataFrame으로 변환하는 함수
def convert_to_dataframes(data_list, notes_list):
    headers = ["구분", "상품명", "화폐단위", "이용료(월)", "제공방식", "계약 효력일"]
    df = pd.DataFrame(data_list, columns=headers)
    notes_df = pd.DataFrame(notes_list, columns=["Notes"])
    return df, notes_df

# JSON 데이터를 파일에 저장하는 함수
def save_json_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 메인 실행 코드
if __name__ == "__main__":
    seleniumwire_options = {
        'connection_timeout': None,
        'verify_ssl': False,
    }
    driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options)

    try:
        login(driver, 'goguma@krx.co.kr', 'wkrwjs12!@')

        # 데이터 추출
        num = '100562'
        data_result, notes_result = table_iter(num, driver)
        data_df, notes_df = convert_to_dataframes(data_result, notes_result)

        # 클릭할 다운로드 버튼 요소를 찾습니다.
        download_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.iconset.icon-down-attach'))
        )
        download_link.click()  # 요소를 클릭합니다.

        # 클릭 후에 발생하는 요청을 필터링합니다.
        time.sleep(3)  # 네트워크 트래픽을 기다립니다.
        json_responses = []
        for request in driver.requests:
            if request.response and 'application/json' in request.response.headers.get('Content-Type', ''):
                print(f"요청 URL: {request.url}")
                print(f"응답 코드: {request.response.status_code}")
                print(f"요청 헤더: {request.headers}")
                if request.body:
                    # 요청 본문이 있다면 출력합니다.
                    print(f"요청 바디: {request.body.decode('utf-8', 'ignore')}")
                else:
                    print("요청 바디: None")

                # 응답이 gzip으로 압축되었다면 압축 해제합니다.
                content_encoding = request.response.headers.get('Content-Encoding', '')
                if 'gzip' in content_encoding:
                    response_body = gzip.decompress(request.response.body).decode('utf-8')
                else:
                    response_body = request.response.body.decode('utf-8')

                # JSON 응답을 파이썬 객체로 변환하여 리스트에 추가합니다.
                json_responses.append(json.loads(response_body))

        # JSON 응답을 파일에 저장합니다.
        save_json_to_file(json_responses, 'api_responses.json')
        print("[INFO] JSON 응답이 파일에 저장되었습니다.")

        # 원래 데이터 프레임 출력
        print(data_df)
        print(notes_df)

    except Exception as e:
        print("[ERROR] An error occurred:", traceback.format_exc())
    finally:
        driver.quit()

# %% 231106 2230 웹 자동화를 통한 API 응답 데이터 추출 및 저장
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import json
import time
import gzip
import traceback

# 로그인 함수
def login(driver, app_id, app_pw):
    print("[INFO] 로그인을 시도합니다.")
    driver.get('https://dataservice.koscom.co.kr/login?returnUrl=/krx/approval-list')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')))
    id_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')
    password_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[2]/div/div/input')
    login_button = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[3]/button')
    id_box.send_keys(app_id)
    password_box.send_keys(app_pw)
    login_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be('https://dataservice.koscom.co.kr/krx/approval-list'))

# 데이터 추출 함수
def table_iter(num, driver):
    print(f"[INFO] 상세 페이지로 이동합니다: {num}")
    base_url = f"https://dataservice.koscom.co.kr/krx/{num}/approval-detail"
    driver.get(base_url)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'table > tbody > tr')))
    rows = driver.find_elements(By.CSS_SELECTOR, 'table > tbody > tr')
    result = [[cell.text for cell in row.find_elements(By.CSS_SELECTOR, 'td')] for row in rows]
    return result

# 데이터를 DataFrame으로 변환하는 함수
def convert_to_dataframes(data_list):
    headers = ["구분", "상품명", "화폐단위", "이용료(월)", "제공방식", "계약 효력일"]
    df = pd.DataFrame(data_list, columns=headers)
    return df

# 메인 실행 코드
if __name__ == "__main__":
    seleniumwire_options = {
        'connection_timeout': None,
        'verify_ssl': False,
    }
    driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options)

    try:
        # 실제 사용자 정보로 변경해야 합니다.
        login(driver, 'goguma@krx.co.kr', 'wkrwjs12!@')

        # 데이터 추출
        num = '100562'
        data_result = table_iter(num, driver)
        data_df = convert_to_dataframes(data_result)

        # 클릭 후에 발생하는 요청을 필터링합니다.
        time.sleep(3)  # 네트워크 트래픽을 기다립니다.
        json_responses = []
        for request in driver.requests:
            if request.response and 'application/json' in request.response.headers.get('Content-Type', ''):
                response_body = request.response.body
                if 'gzip' in request.response.headers.get('Content-Encoding', ''):
                    response_body = gzip.decompress(response_body)
                response_body = response_body.decode('utf-8')
                json_data = json.loads(response_body)

                # Check if request is a POST and has a body
                request_body = None
                if request.method == 'POST' and request.body:
                    request_body = request.body.decode('utf-8')
                    try:
                        request_body = json.loads(request_body)
                    except json.JSONDecodeError:
                        pass  # request_body remains a string if it's not JSON

                response_info = {
                    'request_url': request.url,
                    'request_method': request.method,
                    'request_body': request_body,
                    'request_headers': dict(request.headers),
                    'response_code': request.response.status_code,
                    'response_headers': dict(request.response.headers),
                    'response_body': json_data
                }
                json_responses.append(response_info)

        # JSON 응답을 파일에 저장합니다.
        with open('api_responses.json', 'w', encoding='utf-8') as f:
            json.dump(json_responses, f, ensure_ascii=False, indent=4)

        print("[INFO] JSON 응답이 파일에 저장되었습니다.")

        # 데이터 프레임을 출력하거나 파일로 저장할 수 있습니다.
        print(data_df)

    except Exception as e:
        print("[ERROR] An error occurred:", traceback.format_exc())
    finally:
        driver.quit()

# %% 231106 2325 Not working, for Debug (Profile Login)
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import json
import requests
import traceback
import os

# 로그인 함수
def login(driver, app_id, app_pw):
    print("[INFO] 로그인을 시도합니다.")
    driver.get('https://dataservice.koscom.co.kr/login?returnUrl=/krx/approval-list')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')))
    id_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')
    password_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[2]/div/div/input')
    login_button = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[3]/button')

    id_box.send_keys(app_id)
    password_box.send_keys(app_pw)
    login_button.click()

    WebDriverWait(driver, 10).until(EC.url_to_be('https://dataservice.koscom.co.kr/krx/approval-list'))
    print("[INFO] 로그인에 성공했습니다.")

# 메인 실행 코드
if __name__ == "__main__":
    # Chrome 드라이버 경로 설정
    CHROMEDRIVER_PATH = os.path.expanduser('~/chromedriver')  # Home 디렉토리의 chromedriver 경로

    # ChromeDriver가 실제로 존재하는지 확인
    if not os.path.exists(CHROMEDRIVER_PATH):
        raise Exception(f"ChromeDriver not found at {CHROMEDRIVER_PATH}")

    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    try:
        # 로그인 수행
        login(driver, 'goguma@krx.co.kr', 'wkrwjs12!@')

        # 로그인 이후 발생하는 모든 요청에서 Authorization 헤더를 찾습니다.
        headers = None
        for request in driver.requests:
            if 'Authorization' in request.headers:
                headers = {'Authorization': request.headers['Authorization']}
                break

        # Authorization 헤더를 찾지 못한 경우 에러 메시지 출력
        if not headers:
            print("[ERROR] Authorization 헤더를 찾을 수 없습니다.")
        else:
            # API URL 설정
            api_url = 'https://dataservice.koscom.co.kr/apis/v1/user/approvals/100562'

            # API 요청 보내기
            api_response = send_api_request(api_url, headers)

            # API 응답 확인 및 출력
            if api_response:
                print("[INFO] API 응답 데이터:")
                print(json.dumps(api_response, indent=4, ensure_ascii=False))
            else:
                print("[ERROR] API 요청 실패")

    except Exception as e:
        print("[ERROR] 예외가 발생했습니다:", traceback.format_exc())
    finally:
        driver.quit()
        print("프로세스가 완료되었습니다.")

# API 요청을 보내는 함수
def send_api_request(url, headers):
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"[ERROR] API 요청 실패. Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

# %% 231106 2330 코스콤 데이터 서비스 로그인 및 API 호출 자동화 스크립트
# 프로필 로그인을 위해서는 프로필 (C:\Users\221016\AppData\Local\Google\Chrome\User Data) 
# 정보를 다른 DIR 에 복사하여 설정해주어야 충돌 문제가 없음
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver as seleniumwire_webdriver  # seleniumwire 추가
import json
import requests
import traceback
import os

# 로그인 함수
def login(driver, app_id, app_pw):
    print("[INFO] 로그인을 시도합니다.")
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')))
    id_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[1]/div/div/input')
    password_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[2]/div/div/input')
    login_button = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/form/div[3]/button')

    id_box.send_keys(app_id)
    password_box.send_keys(app_pw)
    login_button.click()

    WebDriverWait(driver, 10).until(EC.url_to_be(TARGET_URL))
    print("[INFO] 로그인에 성공했습니다.")

# API 요청을 보내는 함수
def send_api_request(url, headers):
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"[ERROR] API 요청 실패. Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

# 사용자의 크롬 프로필 경로 설정
PROFILE_PATH = 'C:\\Users\\KRX\\Desktop\\201021'  # 사용자 데이터 디렉토리 경로
PROFILE_NAME = 'Profile 4'  # 프로필 이름

# 로그인 URL과 목표 URL 설정
LOGIN_URL = 'https://dataservice.koscom.co.kr/login?returnUrl=/krx/approval-list'
TARGET_URL = 'https://dataservice.koscom.co.kr/krx/approval-list'

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument(f'user-data-dir={PROFILE_PATH}')
chrome_options.add_argument(f'profile-directory={PROFILE_NAME}')
chrome_options.add_argument("start-maximized")  # Chrome을 최대화하여 시작
chrome_options.add_argument("disable-infobars")  # Chrome의 정보 바 비활성화
chrome_options.add_argument("--disable-extensions")  # 확장 기능 비활성화
chrome_options.add_argument("--disable-gpu")  # GPU 하드웨어 가속 비활성화
chrome_options.add_argument("--no-sandbox")  # 샌드박스 모드 비활성화

# Chrome 드라이버 경로 설정 (현재 작업 디렉토리를 사용)
CHROMEDRIVER_PATH = os.path.join(os.getcwd(), 'chromedriver.exe')

# ChromeDriver가 실제로 존재하는지 확인
if not os.path.exists(CHROMEDRIVER_PATH):
    raise Exception(f"ChromeDriver not found at {CHROMEDRIVER_PATH}")

# 서비스 객체를 생성하고 경로를 지정합니다.
service = Service(executable_path=CHROMEDRIVER_PATH)
driver = seleniumwire_webdriver.Chrome(service=service, options=chrome_options)

# 메인 실행 코드
if __name__ == "__main__":
    try:
        # 로그인 수행
        login(driver, 'goguma@krx.co.kr', 'wkrwjs12!@')

        # 로그인 이후 발생하는 모든 요청에서 Authorization 헤더를 찾습니다.
        headers = None
        for request in driver.requests:
            if 'Authorization' in request.headers:
                headers = {'Authorization': request.headers['Authorization']}
                break

        # Authorization 헤더를 찾지 못한 경우 에러 메시지 출력
        if not headers:
            print("[ERROR] Authorization 헤더를 찾을 수 없습니다.")
        else:
            # API URL 설정
            YOUR_API_URL = 'https://dataservice.koscom.co.kr/apis/v1/user/approvals/100562'
            # API 요청 보내기
            api_response = send_api_request(YOUR_API_URL, headers)

            # API 응답 확인 및 출력
            if api_response:
                print("[INFO] API 응답 데이터:")
                print(json.dumps(api_response, indent=4, ensure_ascii=False))
            else:
                print("[ERROR] API 요청 실패")

    except Exception as e:
        print("[ERROR] 예외가 발생했습니다:", traceback.format_exc())
    finally:
        driver.quit()
        print("프로세스가 완료되었습니다.")


