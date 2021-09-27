# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 09:25:29 2021

@author: user
"""

import datetime as dt                # 객체를 date 타입으로 만들어줄 모듈
from urllib.request import urlopen   # 소스코드는 get해올 모듈(requests와 비슷)
from bs4 import BeautifulSoup
import re as hi
import requests as re
import pandas as pd
import pandas_datareader as pdr
import os
os.chdir('C:/Users/user/Desktop')


pd.set_option('display.max_row', 50)

# naver_index = r'https://finance.naver.com/marketindex/interestDailyQuote.naver?marketindexCd=' + r'IRR_GOVT03Y' + "&" + "page=" + str("1")
# url = re.get(naver_index)
# html = BeautifulSoup(url.text,'html.parser')
# print(html)
# fn_body = html.find('tr', {'class':'up'})
#content > div:nth-child(10) > div.VTablePrice_article__2wmYd > table > tbody > tr:nth-child(1)
#content > div:nth-child(10) > div.VTablePrice_article__2wmYd > table > tbody > tr:nth-child(1) > td:nth-child(1) > time

# dates = html.find_all('td', class_ = 'date')          # 날짜수집
# prices = html.find_all('td', class_ = 'number_1')     # 지수수집

# print(dates)
# print(prices)

#content > div:nth-child(10) > div.VTablePrice_article__2wmYd
# source = urlopen(naver_index).read()
# source = BeautifulSoup(source, 'html')

def date_format(d):                     # 코스피200 일자별시세에서 날짜데이터를 가져와 date타입으로 바꿀 함수
    d = str(d).replace('-', '.') # d는  # d(날짜) 형태에서 -를 .으로 바꿔준다 (ex. 2020-5-11 -> 2020.5.11)
    yyyy = int(d.split('.')[0])         # 2020.5.11을 점기준 split 하면 2020, 5, 11 이 되는데 첫번째 인덱스 2020로 yyyy를 정의
    mm = int(d.split('.')[1])           # 두번째 인덱스 5로 mm을 정의
    dd = int(d.split('.')[2])           # 세번째 인덱스 11로 dd를 정의
    
    this_date = dt.date(yyyy, mm, dd)   # (2020, 5, 11)이 date 타입이 됨
    return this_date

### (1) Domestic index (2) ----

"""
Kospi, Kosdaq
"""
def historical_index_naver(index_cd, start_date='', end_date='', page_n=1, last_page=0):
    # 파라미터로는 
    # index_cd : 코드명, 코스피 (KOSPI) / 코스피200 (KPI200) / 코스닥 (KOSDAQ) 
    # start_date(원하는 기간의 시작일), end_date(종료일) 날짜를 문자열로 넣는다
    # page_n =1   항상 1페이지 부터 시작한다
    # last_page = 0  마지막페이지는 아직 몇인지 모르니 우선 0으로 놓는다
    
    if start_date:                                   # 만약 start_date를 정의해줬으면
        start_date = date_format(start_date)        # start_date를 위에서 만든 date_format함수로 원하는 형태로 바꿔주자
    else:
        start_date = dt.date.today()                # 만약 start_date를 정의해주지 않았다면 오늘 날짜로 정의
    
    if end_date:                                    # 만약 end_date를 정의해줬으면
        end_date = date_format(end_date)            # end_date를 위에서 만든 date_format함수로 원하는 형태로 바꿔주자
    else:
        end_date = dt.date.today()                  # 만약 end_date를 정의해주지 않았다면 오늘 날짜로 정의
        
    # 일별시세 url 소스코드를 가져오기
        
    naver_index = r'https://finance.naver.com/sise/sise_index_day.nhn?code=' + index_cd + r'&page=' + str(page_n)
    source = urlopen(naver_index).read()
    source = BeautifulSoup(source, 'lxml')
    
    dates = source.find_all('td', class_ = 'date')          # 날짜수집
    prices = source.find_all('td', class_ = 'number_1')     # 지수수집
    
    
    
    for n in range(len(dates)): # 특정페이지에서 6개의 날짜가 출력됨. 6개의 날짜데이터 모두 코르블록 실행
        
        if dates[n].text.split('.')[0].isdigit():  # 만약 n번째 페이지의 날짜데이터의 첫번째 인덱스가 숫자라면 코드블록 실행
                                                   # (날짜데이터가 맞는지 확인하는?)
        
            # 날짜 처리를 처리
            
            this_date = dates[n].text              # n번째 태그에서 날짜인 text만 가져오기
            this_date = date_format(this_date)     # 위에서 정의해준 date_format함수로 원하는 형태로 날짜 만들어주기
            
            # 만약 this_date가 정의해줄 end_date보다 작거나 같고 start_date보다 크거나 같으면 코드블록 실행
            # 즉 end_date와 start_date 사이의 날짜들에 대해서만 코드 실행
            
            if this_date <= end_date and this_date >=start_date:  
                
            # 종가 처리
                this_close = prices[n*4].text            #종가는 ('td', class_='number_1')을 가진 소스들의 5번째에 옴
                                                         # 그러므르 인덱스는 4의 배수(4*n)이 필요

                this_close = this_close.replace(',', '')  # 숫자의 천 단위마다 있는 ,를 빼준다.
                this_close = float(this_close)            # 그후 실수타입으로 바꿔줌

            # 딕셔너리에 저장
                historical_prices[this_date] = this_close # 날짜:종가 형태가 나올 수 있도록 dict에 저장
            
            elif this_date < start_date:                  
                return historical_prices
            
    # 페이지 내비게이션 / 일별시세의 마지막 페이지가 몇인지 알기위함
    if last_page == 0:                          
        last_page = source.find('td', class_ = 'pgRR').find('a')['href']
        last_page = last_page.split('&')[1]
        last_page = int(last_page.split('=')[1])
    
    # 다음페이지 호출
    if page_n <= last_page: #페이지가 마지막 페이지까지 돌 수 있도록 하기
        page_n += 1        #페이지는 하나씩 올라가야함
        historical_index_naver(index_cd, start_date, end_date, page_n, last_page)
        
        # 만약 마지막 페이지가 5라고 하면
        # 우리가 정의해준 함수 historical_index_naver는
        # historical_index_naver(index_cd, start_date, end_date, 1, 5)
        # historical_index_naver(index_cd, start_date, end_date, 2, 5) ... 이런식으로 page_n가 5가 될때까지 실행
    
    return historical_prices # 반환은 dict 타입인 historical_prices로 한다

# today = "2021-9-23"
# index_cd = 'KPI200'
# historical_index_naver(index_cd, start_date = '2021-1-1', end_date = today)

# Result
today = str(dt.datetime.today().year) + "-" + str(dt.datetime.today().month) \
    + "-" + str(dt.datetime.today().day)

# df_KPI200  = historical_index_naver("KPI200", start_date = '2021-1-1', end_date = today)
historical_prices = dict()
df_KPI200 = pd.DataFrame.from_dict(historical_index_naver("KPI200", start_date = '2021-1-1', end_date = today), orient = "index")
df_KPI200.columns = ["코스피200"]
df_KPI200 = df_KPI200.loc[::-1]
df_KPI200.index = [i.strftime("%y-%m-%d") for i in df_KPI200.index]

historical_prices = dict()
df_KPI = pd.DataFrame.from_dict(historical_index_naver("Kospi", start_date = '2021-1-1', end_date = today), orient = "index")
df_KPI.columns = ["코스피"]
df_KPI = df_KPI[::-1]
df_KPI.index = [i.strftime("%y-%m-%d") for i in df_KPI.index]

historical_prices = dict()
df_KOS = pd.DataFrame.from_dict(historical_index_naver("Kosdaq", start_date = '2021-1-1', end_date = today), orient = "index")
df_KOS.columns = ["코스닥"]
df_KOS = df_KOS[::-1]
df_KOS.index = [i.strftime("%y-%m-%d") for i in df_KOS.index]


### (2) Domestic interest (4) ----

def historical_interest_naver(interest_cd, start_date='', end_date='', page_n=1, last_page=0):
    # 파라미터로는 
    # interest_cd : IRR_GOVT03Y (국고채 3년), IRR_CORP03Y (회사채 3년), 
    #               IRR_CALL(Call), IRR_CD91 (CD 금리), 
    # start_date(원하는 기간의 시작일), end_date(종료일) 날짜를 문자열로 넣는다
    # page_n =1   항상 1페이지 부터 시작한다
    # last_page = 0  마지막페이지는 아직 몇인지 모르니 우선 0으로 놓는다
    
    if start_date:                                   # 만약 start_date를 정의해줬으면
        start_date = date_format(start_date)        # start_date를 위에서 만든 date_format함수로 원하는 형태로 바꿔주자
    else:
        start_date = dt.date.today()                # 만약 start_date를 정의해주지 않았다면 오늘 날짜로 정의
    
    if end_date:                                    # 만약 end_date를 정의해줬으면
        end_date = date_format(end_date)            # end_date를 위에서 만든 date_format함수로 원하는 형태로 바꿔주자
    else:
        end_date = dt.date.today()                  # 만약 end_date를 정의해주지 않았다면 오늘 날짜로 정의
        
    # 일별시세 url 소스코드를 가져오기
        
    naver_interest = r'https://finance.naver.com/marketindex/interestDailyQuote.naver?marketindexCd=' + interest_cd + r'&page=' + str(page_n)
    source = urlopen(naver_interest).read()
    source = BeautifulSoup(source, 'lxml')
    
    dates = source.find_all('td', class_ = 'date')          # 날짜수집
    prices = source.find_all('td', class_ = 'num')     # 지수수집
    
    for n in range(len(dates)): # 특정페이지에서 6개의 날짜가 출력됨. 6개의 날짜데이터 모두 코르블록 실행
        
        if hi.sub(r"[^a-zA-Z0-9]","",dates[n].text).isdigit():
                                                   # 만약 n번째 페이지의 날짜데이터의 첫번째 인덱스가 숫자라면 코드블록 실행
                                                   # (날짜데이터가 맞는지 확인하는?)
        
            # 날짜 처리를 처리
            
            # this_date = dates[n].text              # n번째 태그에서 날짜인 text만 가져오기
            this_date = hi.sub(r"[^a-zA-Z0-9]","",dates[n].text)
            this_date = dt.datetime.date(dt.datetime.strptime(this_date, "%Y%m%d"))
            
            # this_date = date_format(this_date)     # 위에서 정의해준 date_format함수로 원하는 형태로 날짜 만들어주기
            
            # 만약 this_date가 정의해줄 end_date보다 작거나 같고 start_date보다 크거나 같으면 코드블록 실행
            # 즉 end_date와 start_date 사이의 날짜들에 대해서만 코드 실행
            
            if this_date <= end_date and this_date >=start_date:  
                
            # 종가 처리
                this_close = prices[n*3].text            #종가는 ('td', class_='number_1')을 가진 소스들의 5번째에 옴
                                                         # 그러므르 인덱스는 4의 배수(4*n)이 필요

                this_close = this_close.replace(',', '')  # 숫자의 천 단위마다 있는 ,를 빼준다.
                this_close = float(this_close)            # 그후 실수타입으로 바꿔줌

            # 딕셔너리에 저장
                historical_prices[this_date] = this_close # 날짜:종가 형태가 나올 수 있도록 dict에 저장
            
            elif this_date < start_date:                  
                return historical_prices
            
    # 페이지 내비게이션 / 일별시세의 마지막 페이지가 몇인지 알기위함
    #if last_page == 0:                          
    #    last_page = source.find('td', class_ = 'pgRR').find('a')['href']
    #    last_page = last_page.split('&')[1]
    #    last_page = int(last_page.split('=')[1])
    last_page = 1000
    # 다음페이지 호출
    if page_n <= last_page: #페이지가 마지막 페이지까지 돌 수 있도록 하기
        page_n += 1        #페이지는 하나씩 올라가야함
        historical_interest_naver(interest_cd, start_date, end_date, page_n, last_page)
        
        # 만약 마지막 페이지가 5라고 하면
        # 우리가 정의해준 함수 historical_interest_naver는
        # historical_interest_naver(interest_cd, start_date, end_date, 1, 5)
        # historical_interest_naver(interest_cd, start_date, end_date, 2, 5) ... 이런식으로 page_n가 5가 될때까지 실행
    
    return historical_prices # 반환은 dict 타입인 historical_prices로 한다
historical_interest_naver("IRR_GOVT03Y", start_date = '2021-1-1', end_date = today)

historical_prices = dict()
df_KR3_gov = pd.DataFrame.from_dict(historical_interest_naver("IRR_GOVT03Y", start_date = '2021-1-1', end_date = today), orient = "index")
df_KR3_gov.columns = ["국고채(3년)"]
df_KR3_gov = df_KR3_gov[::-1]
df_KR3_gov.index = [i.strftime("%y-%m-%d") for i in df_KR3_gov.index]

historical_prices = dict()
df_KR3_cop = pd.DataFrame.from_dict(historical_interest_naver("IRR_CORP03Y", start_date = '2021-1-1', end_date = today), orient = "index")
df_KR3_cop.columns = ["회사채(3년)"]
df_KR3_cop = df_KR3_cop[::-1]
df_KR3_cop.index = [i.strftime("%y-%m-%d") for i in df_KR3_cop.index]

historical_prices = dict()
df_CD = pd.DataFrame.from_dict(historical_interest_naver("IRR_CD91", start_date = '2021-1-1', end_date = today), orient = "index")
df_CD.columns = ["CD91"]
df_CD = df_CD[::-1]
df_CD.index = [i.strftime("%y-%m-%d") for i in df_CD.index]

historical_prices = dict()
df_Call = pd.DataFrame.from_dict(historical_interest_naver("IRR_CALL", start_date = '2021-1-1', end_date = today), orient = "index")
df_Call.columns = ["Call"]
df_Call = df_Call[::-1]
df_Call.index = [i.strftime("%y-%m-%d") for i in df_Call.index]


### (3) FDR index (6) ----
"""
DJI(다우지수), IXIC(나스닥 지수), US500(S&P 500) SPX, VIX (공포 지수),
HSI (항셍 지수), 
USD/KRW (원달러 환율), 
US10YT=X (미국 10년 국채), KR10YT=RR(한국 10년 국채)
"""
import FinanceDataReader as fdr

df_Dji = fdr.DataReader('DJI', start = "2021-01-01")
df_Dji = pd.DataFrame(df_Dji["Close"])
df_Dji.index.name = None
df_Dji.columns = ["다우"]
df_Dji.index = df_Dji.index.strftime("%y-%m-%d") 

df_IXIC = fdr.DataReader('IXIC', start = "2021-01-01")
df_IXIC = pd.DataFrame(df_IXIC["Close"])
df_IXIC.index.name = None
df_IXIC.columns = ["나스닥"]
df_IXIC.index = df_IXIC.index.strftime("%y-%m-%d") 

df_SP500 = fdr.DataReader('US500', start = "2021-01-01")
df_SP500 = pd.DataFrame(df_SP500["Close"])
df_SP500.index.name = None
df_SP500.columns = ["SP500"]
df_SP500.index = df_SP500.index.strftime("%y-%m-%d") 

df_USD = fdr.DataReader('USD/KRW', start = "2021-01-01")
df_USD = pd.DataFrame(df_USD["Close"])
df_USD.index.name = None
df_USD.columns = ["환율"]
df_USD.index = df_USD.index.strftime("%y-%m-%d") 

df_US10 = fdr.DataReader('US10YT=X', start = "2021-01-01")
df_US10 = pd.DataFrame(df_US10["Close"])
df_US10.index.name = None
df_US10.columns = ["미국채(10년)"]
df_US10.index = df_US10.index.strftime("%y-%m-%d") 

df_US2 = fdr.DataReader('US2YT=X', start = "2021-01-01")
df_US2 = pd.DataFrame(df_US2["Close"])
df_US2.index.name = None
df_US2.columns = ["미국채(2년)"]
df_US2.index = df_US2.index.strftime("%y-%m-%d") 

df_KR10 = fdr.DataReader('KR10YT=RR', start = "2021-01-01")
df_KR10 = pd.DataFrame(df_KR10["Close"])
df_KR10.index.name = None
df_KR10.columns = ["국고채(10년)"]
df_KR10.index = df_KR10.index.strftime("%y-%m-%d") 

df_Vix = fdr.DataReader('VIX', start = "2021-01-01")
df_Vix = pd.DataFrame(df_Vix["Close"])
df_Vix.index.name = None
df_Vix.columns = ["VIX"]
df_Vix.index = df_Vix.index.strftime("%y-%m-%d") 

df_Hsi = fdr.DataReader('HSI', start = "2021-01-01")
df_Hsi = pd.DataFrame(df_Hsi["Close"])
df_Hsi.index.name = None
df_Hsi.columns = ["항셍"]
df_Hsi.index = df_Hsi.index.strftime("%y-%m-%d") 

### (4) Raw material (2) 
df_gold = pdr.DataReader('GOLDAMGBD228NLBM', 'fred', start='2021-01-01')
df_gold.index = df_gold.index.strftime("%y-%m-%d") 
df_gold.index.name = "Index"
df_gold.columns = ["gold"]

def historical_raw_naver(raw_cd, start_date='', end_date='', page_n=1, last_page=0):
    # 파라미터로는 
    # raw_cd : OIL_CL&fdtc=2 (WTI)
    # start_date(원하는 기간의 시작일), end_date(종료일) 날짜를 문자열로 넣는다
    # page_n =1   항상 1페이지 부터 시작한다
    # last_page = 0  마지막페이지는 아직 몇인지 모르니 우선 0으로 놓는다
    
    if start_date:                                   # 만약 start_date를 정의해줬으면
        start_date = date_format(start_date)        # start_date를 위에서 만든 date_format함수로 원하는 형태로 바꿔주자
    else:
        start_date = dt.date.today()                # 만약 start_date를 정의해주지 않았다면 오늘 날짜로 정의
    
    if end_date:                                    # 만약 end_date를 정의해줬으면
        end_date = date_format(end_date)            # end_date를 위에서 만든 date_format함수로 원하는 형태로 바꿔주자
    else:
        end_date = dt.date.today()                  # 만약 end_date를 정의해주지 않았다면 오늘 날짜로 정의
        
    # 일별시세 url 소스코드를 가져오기
        
    naver_raw = r'https://finance.naver.com/marketindex/worldDailyQuote.naver?marketindexCd=' + raw_cd + r'&page=' + str(page_n)
    source = urlopen(naver_raw).read()
    source = BeautifulSoup(source, 'lxml')
    
    dates = source.find_all('td', class_ = 'date')          # 날짜수집
    prices = source.find_all('td', class_ = 'num')     # 지수수집
    
    for n in range(len(dates)): # 특정페이지에서 6개의 날짜가 출력됨. 6개의 날짜데이터 모두 코르블록 실행
        
        if hi.sub(r"[^a-zA-Z0-9]","",dates[n].text).isdigit():
                                                   # 만약 n번째 페이지의 날짜데이터의 첫번째 인덱스가 숫자라면 코드블록 실행
                                                   # (날짜데이터가 맞는지 확인하는?)
        
            # 날짜 처리를 처리
            
            # this_date = dates[n].text              # n번째 태그에서 날짜인 text만 가져오기
            this_date = hi.sub(r"[^a-zA-Z0-9]","",dates[n].text)
            this_date = dt.datetime.date(dt.datetime.strptime(this_date, "%Y%m%d"))
            
            # this_date = date_format(this_date)     # 위에서 정의해준 date_format함수로 원하는 형태로 날짜 만들어주기
            
            # 만약 this_date가 정의해줄 end_date보다 작거나 같고 start_date보다 크거나 같으면 코드블록 실행
            # 즉 end_date와 start_date 사이의 날짜들에 대해서만 코드 실행
            
            if this_date <= end_date and this_date >=start_date:  
                
            # 종가 처리
                this_close = prices[n*3].text            #종가는 ('td', class_='number_1')을 가진 소스들의 5번째에 옴
                                                         # 그러므르 인덱스는 4의 배수(4*n)이 필요

                this_close = this_close.replace(',', '')  # 숫자의 천 단위마다 있는 ,를 빼준다.
                this_close = float(this_close)            # 그후 실수타입으로 바꿔줌

            # 딕셔너리에 저장
                historical_prices[this_date] = this_close # 날짜:종가 형태가 나올 수 있도록 dict에 저장
            
            elif this_date < start_date:                  
                return historical_prices
            
    # 페이지 내비게이션 / 일별시세의 마지막 페이지가 몇인지 알기위함
    #if last_page == 0:                          
    #    last_page = source.find('td', class_ = 'pgRR').find('a')['href']
    #    last_page = last_page.split('&')[1]
    #    last_page = int(last_page.split('=')[1])
    last_page = 1000
    # 다음페이지 호출
    if page_n <= last_page: #페이지가 마지막 페이지까지 돌 수 있도록 하기
        page_n += 1        #페이지는 하나씩 올라가야함
        historical_raw_naver(raw_cd, start_date, end_date, page_n, last_page)
        
        # 만약 마지막 페이지가 5라고 하면
        # 우리가 정의해준 함수 historical_raw_naver는
        # historical_raw_naver(raw_cd, start_date, end_date, 1, 5)
        # historical_raw_naver(raw_cd, start_date, end_date, 2, 5) ... 이런식으로 page_n가 5가 될때까지 실행
    
    return historical_prices # 반환은 dict 타입인 historical_prices로 한다

historical_prices = dict()
df_wt = pd.DataFrame.from_dict(historical_raw_naver("OIL_CL&fdtc=2", start_date = '2021-1-1', end_date = today), orient = "index")
df_wt.columns = ["WTI"]
df_wt = df_wt[::-1]
df_wt.index = [i.strftime("%y-%m-%d") for i in df_wt.index]


# df_wt = pdr.DataReader('POILWTIUSDM', 'fred', start='2021-01-01')
# df_wt.index = df_wt.index.strftime("%y-%m-%d") 
# df_wt.index.name = "Index"
# df_wt.columns = ["wti"]

### (5) Concat
WTS = pd.merge(df_KPI, df_KPI200, left_index = True, right_index = True, how = "left")
WTS = pd.merge(WTS, df_KOS, left_index = True, right_index = True, how = "left")

WTS = pd.merge(WTS, df_IXIC, left_index = True, right_index = True, how = "left")
WTS = pd.merge(WTS, df_SP500, left_index = True, right_index = True, how = "left")
WTS = pd.merge(WTS, df_Dji, left_index = True, right_index = True, how = "left")
WTS = pd.merge(WTS, df_Vix, left_index = True, right_index = True, how = "left")
WTS = pd.merge(WTS, df_Hsi, left_index = True, right_index = True, how = "left")

WTS = pd.merge(WTS, df_CD, left_index = True, right_index = True, how = "left")
WTS = pd.merge(WTS, df_Call, left_index = True, right_index = True, how = "left")
WTS = pd.merge(WTS, df_KR3_gov, left_index = True, right_index = True, how = "left")
WTS = pd.merge(WTS, df_KR10, left_index = True, right_index = True, how = "left")
WTS = pd.merge(WTS, df_KR3_cop, left_index = True, right_index = True, how = "left")

WTS = pd.merge(WTS, df_US10, left_index = True, right_index = True, how = "left")
WTS = pd.merge(WTS, df_US2, left_index = True, right_index = True, how = "left")
WTS = pd.merge(WTS, df_USD, left_index = True, right_index = True, how = "left")


WTS = pd.merge(WTS, df_gold, left_index = True, right_index = True, how = "left")
WTS = pd.merge(WTS, df_wt, left_index = True, right_index = True, how = "left")

### Stock Maket과 다르게, 휴장이 없는 interest MKT을 위한 추가 데이터셋
WTS_2 = pd.merge(df_US2, df_US10, left_index = True, right_index = True, how = "left")
WTS_2 = pd.merge(WTS_2 , df_CD, left_index = True, right_index = True, how = "left")
WTS_2 = pd.merge(WTS_2 , df_Call, left_index = True, right_index = True, how = "left")
WTS_2 = pd.merge(WTS_2 , df_KR3_gov, left_index = True, right_index = True, how = "left")
WTS_2 = pd.merge(WTS_2 , df_KR3_cop, left_index = True, right_index = True, how = "left")
WTS_2 = pd.merge(WTS_2 , df_KR10, left_index = True, right_index = True, how = "left")


WTS.to_csv("WTS.csv", encoding = "euc-kr")
WTS_2.to_csv("WTS(interest_daily).csv", encoding = "euc-kr")
 # Hsi index : https://kr.investing.com/indices/hang-sen-40
 
### (6) Graph
import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm

WTS.index = [dt.datetime.strptime(i, "%y-%m-%d") for i in WTS.index]


for i in range(0, len(WTS.columns)):
    plt.rcParams["font.family"] = "S-Core Dream"

    # labels = [WTS.columns[i]]
    plt.figure(figsize=(15,5))
    plt.title(WTS.columns[i] + " 추이 " + "(update : " + str(today) + ")", fontsize = 25)
    plt.grid()
    # plt.legend(labels)
    plt.plot(WTS.iloc[:,i])
    plt.savefig(str(WTS.columns[i]) + ".png", dpi=1200)

WTS_2.index = [dt.datetime.strptime(i, "%y-%m-%d") for i in WTS_2.index]
for i in range(0, len(WTS_2.columns)):
    plt.rcParams["font.family"] = "S-Core Dream"

    # labels = [WTS.columns[i]]
    plt.figure(figsize=(15,5))
    plt.title(WTS_2.columns[i] + " 추이 " + "(update : " + str(today) + ")", fontsize = 25)
    plt.grid()
    # plt.legend(labels)
    plt.plot(WTS_2.iloc[:,i])
    plt.savefig(str(WTS_2.columns[i]) + ".png", dpi=1200)

ax1 = plt.subplot(1,1,1)
ax1 = plt.plot(WTS_2["미국채(2년)"])
ax1 = plt.plot(WTS_2["미국채(10년)"])
plt.axvspan(dt.datetime(2021, 9, 24), dt.datetime(2021, 9, 27), alpha = 0.3, color = "pink")
