# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:11:23 2023

@author: Dongjae
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:07:58 2023

@author: Dongjae
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 23:52:26 2023

@author: Dongjae
"""

import requests
from bs4 import BeautifulSoup
import pdfplumber
from PyPDF2 import PdfReader, PdfWriter
import os
import pandas as pd
# %% (0) Working Directory
try : 
    os.chdir("C://Users//Dongjae//Desktop//KRX") # Change Directory

except : 
    print("Directory not found")

# %% ① Crawling #################################################### 
################## Should be exceuted Start ################## 
import chromedriver_autoinstaller
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrom driver is insatlled: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)
################## Should be exceuted End ################## 
"""
# %% 案 7
import re
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
from datetime import datetime

url = 'https://www.spglobal.com/spdji/en/media-center/news-announcements/#indexNews'

##############################Necessary Def Start ##############################
def is_valid_pdf(pdf_content):
    try:
        reader = PdfReader(pdf_content)
        return True
    except:
        return False

def get_filename(date):
    date_obj = datetime.strptime(date, "%b %d, %Y")
    year_month = date_obj.strftime("%Y-%m")
    pdf_count = len([f for f in os.listdir() if f.startswith(year_month) and f.endswith('.pdf')])
    return f"{year_month}_pdf_{pdf_count+1}.pdf"

def categorize_announcement(text):
    if re.search(r'S&P 500', text):
        return 'S&P 500'
    elif re.search(r'Reconstitution|Rebalance', text, re.IGNORECASE):
        return 'Reconstitution/Rebalance'
    elif re.search(r'Indices Changes|Join|Set to Join', text, re.IGNORECASE):
        return 'Indices Changes'
    elif re.search(r'Modification', text, re.IGNORECASE):
        return 'Modification'
    elif re.search(r'Consultation', text, re.IGNORECASE):
        return 'Consultation'
    elif re.search(r'Launch', text, re.IGNORECASE):
        return 'Launch'
    elif re.search(r'Announcement', text, re.IGNORECASE):
        return 'Announcement'
    elif re.search(r'Removal', text, re.IGNORECASE):
        return 'Removal'
    else:
        return 'Others'
    
##############################Necessary Def end ##############################

# 웹 드라이버 설정 (Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

driver = webdriver.Chrome(driver_path)
driver.get("https://google.com")
driver.get(url)

# Your Cookie Controls 창 숨기기
cookie_controls = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='onetrust-banner-sdk']"))
)
driver.execute_script("arguments[0].style.display = 'none';", cookie_controls)

pdf_links = []
dates = []
titles = []
asset_classes = []
max_retries = 3

while True:
    retries = 0
    load_more_button_exists = True
    while retries < max_retries:
        try:
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "button-load-more arrow") and contains(@data-gtm-category, "Index Announcements_Simple List")]'))
            )
            load_more_button.click()
            time.sleep(5)
            break
        except Exception as e:
            retries += 1
            if retries == max_retries:
                load_more_button_exists = False
                print("Load More 버튼을 더 이상 클릭할 수 없습니다.")
                break
            else:
                print(f"Load More 버튼 클릭에 실패했습니다. {retries}번째 재시도 중...")
                time.sleep(5)

    if not load_more_button_exists:
        break

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    new_pdf_links = ['https://www.spglobal.com' + a['href'] for a in soup.select('span.download-wrapper > a.link.data-item')]

    pdf_links.extend([link for link in new_pdf_links])

    new_dates = [item.text for item in soup.select("span[data-fieldname='date']")]
    new_titles = [item.text for item in soup.select("a[data-fieldname='link']")]
    new_asset_classes = [item.text.strip() for item in soup.select("span[data-fieldname='assetclass']")]

    dates.extend(new_dates)
    titles.extend(new_titles)
    asset_classes.extend(new_asset_classes)

    if len(new_pdf_links) < 10:
        break

data = {'Date': dates, 'Title': titles, 'Asset Class': asset_classes, 'PDF Link': pdf_links}
df = pd.DataFrame(data)
df = df.drop_duplicates()

last_title = "S&P: US Healthcare Costs Rise 6.27% Over the 12-Months Ending November 2010"
if titles[-1] != last_title:
    remaining_titles = [last_title]
    remaining_dates = [""] * len(remaining_titles)
    remaining_asset_classes = [""] * len(remaining_titles)
    remaining_pdf_links = [""] * len(remaining_titles)

    remaining_data = {'Date': remaining_dates, 'Title': remaining_titles, 'Asset Class': remaining_asset_classes, 'PDF Link': remaining_pdf_links}
    remaining_df = pd.DataFrame(remaining_data)

    df = df.append(remaining_df, ignore_index=True)

df['Category'] = df['Title'].apply(categorize_announcement)
df.to_excel("s_and_p_500_data.xlsx", index=False)
"""
# %% 案 8 - Multiprocessing
from concurrent.futures import ThreadPoolExecutor
import re
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
from datetime import datetime

url = 'https://www.spglobal.com/spdji/en/media-center/news-announcements/#indexNews'

##############################Necessary Def Start ##############################
def is_valid_pdf(pdf_content):
    try:
        reader = PdfReader(pdf_content)
        return True
    except:
        return False

def get_filename(date):
    date_obj = datetime.strptime(date, "%b %d, %Y")
    year_month = date_obj.strftime("%Y-%m")
    pdf_count = len([f for f in os.listdir() if f.startswith(year_month) and f.endswith('.pdf')])
    return f"{year_month}_pdf_{pdf_count+1}.pdf"

def categorize_announcement(text):
    if re.search(r'S&P 500', text):
        return 'S&P 500'
    elif re.search(r'Reconstitution|Rebalance', text, re.IGNORECASE):
        return 'Reconstitution/Rebalance'
    elif re.search(r'Indices Changes|Join|Set to Join', text, re.IGNORECASE):
        return 'Indices Changes'
    elif re.search(r'Modification', text, re.IGNORECASE):
        return 'Modification'
    elif re.search(r'Consultation', text, re.IGNORECASE):
        return 'Consultation'
    elif re.search(r'Launch', text, re.IGNORECASE):
        return 'Launch'
    elif re.search(r'Announcement', text, re.IGNORECASE):
        return 'Announcement'
    elif re.search(r'Removal', text, re.IGNORECASE):
        return 'Removal'
    else:
        return 'Others'
    
##############################Necessary Def end ##############################
# 웹 드라이버 설정 (Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

driver = webdriver.Chrome(driver_path)
driver.get("https://google.com")
driver.get(url)

# Your Cookie Controls 창 숨기기
cookie_controls = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='onetrust-banner-sdk']"))
)
driver.execute_script("arguments[0].style.display = 'none';", cookie_controls)

pdf_links = []
dates = []
titles = []
asset_classes = []
max_retries = 3

def load_more_button_click(driver):
    try:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "button-load-more arrow") and contains(@data-gtm-category, "Index Announcements_Simple List")]'))
        )
        load_more_button.click()
        return True
    except Exception as e:
        return False

def get_announcement_data(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    new_pdf_links = ['https://www.spglobal.com' + a['href'] for a in soup.select('span.download-wrapper > a.link.data-item')]

    new_dates = [item.text for item in soup.select("span[data-fieldname='date']")]
    new_titles = [item.text for item in soup.select("a[data-fieldname='link']")]
    new_asset_classes = [item.text.strip() for item in soup.select("span[data-fieldname='assetclass']")]

    return new_pdf_links, new_dates, new_titles, new_asset_classes

def load_data(driver, max_retries):
    while True:
        retries = 0
        load_more_button_exists = True
        while retries < max_retries:
            success = load_more_button_click(driver)
            if success:
                break
            else:
                retries += 1
                if retries == max_retries:
                    load_more_button_exists = False
                    print("Load More 버튼을 더 이상 클릭할 수 없습니다.")
                    break
                else:
                    print(f"Load More 버튼 클릭에 실패했습니다. {retries}번째 재시도 중...")
                    time.sleep(5)

        if not load_more_button_exists:
            break

        new_pdf_links, new_dates, new_titles, new_asset_classes = get_announcement_data(driver)
        pdf_links.extend(new_pdf_links)
        dates.extend(new_dates)
        titles.extend(new_titles)
        asset_classes.extend(new_asset_classes)

        if len(new_pdf_links) < 10:
            break

    data = {'Date': dates, 'Title': titles, 'Asset Class': asset_classes, 'PDF Link': pdf_links}
    df = pd.DataFrame(data)
    df = df.drop_duplicates()

    last_title = "S&P: US Healthcare Costs Rise 6.27% Over the 12-Months Ending November 2010"
    if titles[-1] != last_title:
        remaining_titles = [last_title]
        remaining_dates = [""] * len(remaining_titles)
        remaining_asset_classes = [""] * len(remaining_titles)
        remaining_pdf_links = [""] * len(remaining_titles)

        remaining_data = {'Date': remaining_dates, 'Title': remaining_titles, 'Asset Class': remaining_asset_classes, 'PDF Link': remaining_pdf_links}
        remaining_df = pd.DataFrame(remaining_data)

        df = df.append(remaining_df, ignore_index=True)

    df['Category'] = df['Title'].apply(categorize_announcement)
    df.to_excel("s_and_p_500_data.xlsx", index=False)

if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        future = executor.submit(load_data, driver, max_retries)
        future.result()
# %% ② Handling #################################################### 
# %% ticker ↔ symbol 
from itertools import chain
from pytickersymbols import PyTickerSymbols

def search_symbol_by_ticker(symbol):
    stock_data = PyTickerSymbols()
    nasdaq_100 = stock_data.get_stocks_by_index('NASDAQ 100')
    sp_500 = stock_data.get_stocks_by_index('S&P 500')

    for stock in chain(nasdaq_100, sp_500):
        if stock['name'] == symbol:
            return stock['symbol']
    return None

def search_ticker_by_symbol(ticker):
    stock_data = PyTickerSymbols()
    nasdaq_100 = stock_data.get_stocks_by_index('NASDAQ 100')
    sp_500 = stock_data.get_stocks_by_index('S&P 500')

    for stock in chain(nasdaq_100, sp_500):
        if stock['symbol'] == ticker:
            return stock['name']
    return None

print(search_symbol_by_ticker('Apple Inc.'))
print(search_ticker_by_symbol('AAPL'))

# %% news_title categorize
# %% 4 案
"""
import re
import pandas as pd

def classify_titles(title_list):
    categories = {
        'inclusion_exclusion': [],
        'rebalancing': [],
        'price_index': [],
        'methodology_change': [],
        'general_update': [],
        'other': []
    }

    inclusion_exclusion_keywords = ['join', 'set to', 'constituent change', 'enter', 'added', 'removed', 'reconstitution', 'treatment']
    rebalancing_keywords = ['rebalancing', 'rebalance']
    price_index_keywords = ['case-shiller', 'home price']
    methodology_change_keywords = ['modification', 'consultation']

    for title in title_list:
        lowercase_title = title.lower()
        classified = []
        
        if any(keyword in lowercase_title for keyword in inclusion_exclusion_keywords):
            classified.append('inclusion_exclusion')
        if any(keyword in lowercase_title for keyword in rebalancing_keywords):
            classified.append('rebalancing')
        if any(keyword in lowercase_title for keyword in price_index_keywords):
            classified.append('price_index')
        if any(keyword in lowercase_title for keyword in methodology_change_keywords):
            classified.append('methodology_change')
        if 'update' in lowercase_title:
            classified.append('general_update')

        if not classified:
            classified.append('other')
        
        data.loc[titles.index(title), 'Category'] = ', '.join(classified)

    return categories

def extract_indices_from_sentence(sentence):
    # Define the index pattern and the unwanted content pattern
    index_pattern = re.compile(r"(?:S&P[^,]*?)(?:Index|Indices)")
    unwanted_content_before_index_pattern = re.compile(r"(S&P Global Sustainable1 Launch)")

    # Find all matches for index names
    matches = index_pattern.findall(sentence)

    # Iterate over each match and remove the unwanted content
    cleaned_matches = []
    for match in matches:
        cleaned_match = unwanted_content_before_index_pattern.sub("", match).strip()
        cleaned_matches.append(cleaned_match)

    return cleaned_matches


def extract_indices_mentioned(title_list):
    indices_mentioned = []

    # Define patterns to remove certain keywords and phrases from titles
    consultation_pattern = re.compile(r'\b(?:consultation\b.*).*', flags=re.IGNORECASE)
    show_pattern = re.compile(r'\b(?:Show\b.*).*', flags=re.IGNORECASE)
    decline_pattern = re.compile(r'\b(?:Decline\b.*).*', flags=re.IGNORECASE)

    organization_pattern = re.compile(r'S&P Dow Jones Indices')
    verb_pattern = re.compile(r'\b(?:Continued\s+To\s+Decline|Continued|Declining|Trend|Tick up|Show|Reports)\b', re.IGNORECASE)
    exclude_pattern = re.compile(r'\b(?:Trend|Continued|Methodology Update|Consultation|Composite Rate|For|Consecutive|Month|Straight|Increase|Drop|Loan Types)\b', re.IGNORECASE)
    verb_object_pattern = re.compile(r'\b(?:on|of|at|in|to|for)\b\s+(?:Constituent Weighting|Minimum Size Threshold|Eligibility Factors|the)', re.IGNORECASE)
    buybacks_pattern = re.compile(r'\b(?:Buybacks)\b', re.IGNORECASE)
    quarter_buybacks_pattern = re.compile(r'\b(?:Q\d{1}\s\d{4}\sBuybacks)\b', re.IGNORECASE)

    # Add this pattern to find content like "Continued"
    continued_pattern = re.compile(r'\b(?:Continued)\b', re.IGNORECASE)

    for title in title_list:
        # Remove consultation and everything following it
        title_without_consultation = consultation_pattern.sub('', title)

        # Remove "Show" and everything following it
        title_without_show = show_pattern.sub('', title_without_consultation)

        # Remove "Decline" and everything following it
        title_without_decline = decline_pattern.sub('', title_without_show)

        # Remove everything after "Continued"
        continued_match = continued_pattern.search(title_without_decline)
        if continued_match:
            title_without_continued = title_without_decline[:continued_match.start()].rstrip()
        else:
            title_without_continued = title_without_decline

        # Remove organization names, excluded keywords, verb objects, and buybacks
        title_without_organization = organization_pattern.sub('', title_without_continued)
        title_without_excluded_keywords = exclude_pattern.sub('', title_without_organization)
        title_without_verb_objects = verb_object_pattern.sub('', title_without_excluded_keywords)
        title_without_buybacks = buybacks_pattern.sub('', title_without_verb_objects)

        # Find indices in the title based on different conditions
        if quarter_buybacks_pattern.search(title_without_organization):
            title_without_quarter_buybacks = quarter_buybacks_pattern.sub('', title_without_organization)
            indices_found = extract_indices_from_sentence(title_without_quarter_buybacks)
        elif verb_pattern.search(title_without_organization):
            # Split the sentence into phrases by commas or verbs
            phrases = re.split(r',| and | to | for | in | on | of | at ', title_without_verb_objects)
            indices_found = []
            for phrase in phrases:
                # Extract index names from each phrase
                indices_found.extend(extract_indices_from_sentence(phrase))

            # Remove any content after the last verb
            last_verb = verb_pattern.search(title_without_organization)
            if last_verb:
                title_without_content_after_last_verb = title_without_organization[:last_verb.end()].rstrip()
                indices_found_after_last_verb = extract_indices_from_sentence(title_without_content_after_last_verb)
                if indices_found_after_last_verb:
                    indices_found = indices_found_after_last_verb
        else:
            indices_found = extract_indices_from_sentence(title_without_verb_objects)

        # Update the 'Category' column with Buybacks if found in the title
        if buybacks_pattern.search(title_without_buybacks):
            data.loc[titles.index(title), 'Category'] += ', Buybacks'

        # Add the extracted indices to the indices_mentioned list
        if indices_found:
            indices_found = [index_name.strip() for index_name in indices_found]
            indices_mentioned.append(indices_found)
        else:
            indices_mentioned.append([])
            
    return indices_mentioned
  
def extract_index_name(title):
    # Remove any lowercase word that comes after "INDEX"
    post_index_pattern = re.compile(r'(?<=INDEX)\s+[a-z]+', flags=re.IGNORECASE)
    verb_pattern = re.compile(r'\b(?:Continued\s+To\s+Decline|Continued|Declining|Trend|Tick up|Show)\b', re.IGNORECASE)
    
    title = verb_pattern.sub('', title)
    title = post_index_pattern.sub('', title)

    consultation_pattern = r'\b(?:consultation)\b.*'
    title = re.sub(consultation_pattern, '', title, flags=re.IGNORECASE)
    title = re.sub('\b(?:Launched|Show|Announced|Announces|Result|Results|Update|Updates|Methodology|Launch|Launches|Additions|Rebalancing)\b.*', '', title, flags=re.IGNORECASE)
    title = re.sub('\b(?:on|for|about|regarding|concerning|in)\b.*', '', title, flags=re.IGNORECASE)
    title = re.sub('\b(?:by|with)\b.*', '', title, flags=re.IGNORECASE)
    title = re.sub('\b(?:of|and)\b', '', title, flags=re.IGNORECASE)

    consultation_pattern = r'\b(?:consultation)\b.*'
    title = re.sub(consultation_pattern, '', title, flags=re.IGNORECASE)

    title = re.sub(r'\b(?:Declining|Tick up|Show)\b', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\b(?:U\.S\.|U\.K\.|U\.A\.E\.)\b', lambda match: match.group(0).replace('.', ''), title)
    title = re.sub(r'\b(?:Updated)\b', '', title, flags=re.IGNORECASE)
    title = re.sub('\s+', ' ', title).strip()

    # Remove content like "2022 Review Results"
    results_pattern = r'\b(?:\d{4}\sReview\sResults)\b'
    title = re.sub(results_pattern, '', title, flags=re.IGNORECASE)

    # Remove content like "to Track Australia" after "Index"
    track_pattern = r'\b(?:to\s+Track\s+[a-zA-Z]+)\b'
    title = re.sub(track_pattern, '', title, flags=re.IGNORECASE)

    # Add this pattern to remove hyphen and following content after "Index"
    index_hyphen_pattern = r'(?<=Index)\s*-\s*.*'
    title = re.sub(index_hyphen_pattern, '', title, flags=re.IGNORECASE)

    # Add this pattern to remove spaces and following content after "indices"
    indices_space_pattern = r'(?<=indices)\s*.*'
    title = re.sub(indices_space_pattern, '', title, flags=re.IGNORECASE)

    # Remove unnecessary spaces at the beginning and end of the title
    title = title.strip()    
    return title


data = pd.read_excel("s_and_p_500_data.xlsx")

titles = data['Title']

# 각 타이틀에 언급된 인덱스 이름들을 추출합니다.
all_indices_mentioned = extract_indices_mentioned(titles)

# DataFrame에 새로운 열을 추가하여 각 타이틀에 해당하는 인
data['Indices_Mentioned'] = all_indices_mentioned
data.to_excel("s_and_p_500_data_IA.xlsx", index=False) # Index Added
"""
# %% 6 案 : with pdf handling 
import requests
from io import BytesIO
import io
from PyPDF4 import PdfFileReader, utils
import pdfplumber
import re
from tqdm import tqdm
import pandas as pd
import pytesseract
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse


# setting
data = pd.read_excel("s_and_p_500_data.xlsx")
pdf_links = data['PDF Link']
titles = data['Title']

def classify_titles(title_list):
    categories = {
        'inclusion_exclusion': [],
        'rebalancing': [],
        'price_index': [],
        'methodology_change': [],
        'general_update': [],
        'other': []
    }

    inclusion_exclusion_keywords = ['join', 'set to', 'constituent change', 'enter', 'added', 'removed', 'reconstitution', 'treatment']
    rebalancing_keywords = ['rebalancing', 'rebalance']
    price_index_keywords = ['case-shiller', 'home price']
    methodology_change_keywords = ['modification', 'consultation']

    for title in title_list:
        lowercase_title = title.lower()
        classified = []
        
        if any(keyword in lowercase_title for keyword in inclusion_exclusion_keywords):
            classified.append('inclusion_exclusion')
        if any(keyword in lowercase_title for keyword in rebalancing_keywords):
            classified.append('rebalancing')
        if any(keyword in lowercase_title for keyword in price_index_keywords):
            classified.append('price_index')
        if any(keyword in lowercase_title for keyword in methodology_change_keywords):
            classified.append('methodology_change')
        if 'update' in lowercase_title:
            classified.append('general_update')

        if not classified:
            classified.append('other')
        
        data.loc[titles.index(title), 'Category_AK'] = ', '.join(classified)

    return categories

def extract_indices_from_sentence(sentence):
    # Define the index pattern and the unwanted content pattern
    index_pattern = re.compile(r"(?:S&P[^,]*?)(?:Index|Indices)")
    unwanted_content_before_index_pattern = re.compile(r"(S&P Global Sustainable1 Launch)")

    # Find all matches for index names
    matches = index_pattern.findall(sentence)

    # Iterate over each match and remove the unwanted content
    cleaned_matches = []
    for match in matches:
        cleaned_match = unwanted_content_before_index_pattern.sub("", match).strip()
        cleaned_matches.append(cleaned_match)

    return cleaned_matches


def extract_indices_mentioned(title_list):
    indices_mentioned = []

    # Define patterns to remove certain keywords and phrases from titles
    consultation_pattern = re.compile(r'\b(?:consultation\b.*).*', flags=re.IGNORECASE)
    show_pattern = re.compile(r'\b(?:Show\b.*).*', flags=re.IGNORECASE)
    decline_pattern = re.compile(r'\b(?:Decline\b.*).*', flags=re.IGNORECASE)

    organization_pattern = re.compile(r'S&P Dow Jones Indices')
    verb_pattern = re.compile(r'\b(?:Continued\s+To\s+Decline|Continued|Declining|Trend|Tick up|Show|Reports)\b', re.IGNORECASE)
    exclude_pattern = re.compile(r'\b(?:Trend|Continued|Methodology Update|Consultation|Composite Rate|For|Consecutive|Month|Straight|Increase|Drop|Loan Types)\b', re.IGNORECASE)
    verb_object_pattern = re.compile(r'\b(?:on|of|at|in|to|for)\b\s+(?:Constituent Weighting|Minimum Size Threshold|Eligibility Factors|the)', re.IGNORECASE)
    buybacks_pattern = re.compile(r'\b(?:Buybacks)\b', re.IGNORECASE)
    quarter_buybacks_pattern = re.compile(r'\b(?:Q\d{1}\s\d{4}\sBuybacks)\b', re.IGNORECASE)

    # Add this pattern to find content like "Continued"
    continued_pattern = re.compile(r'\b(?:Continued)\b', re.IGNORECASE)

    for title in title_list:
        # Remove consultation and everything following it
        title_without_consultation = consultation_pattern.sub('', title)

        # Remove "Show" and everything following it
        title_without_show = show_pattern.sub('', title_without_consultation)

        # Remove "Decline" and everything following it
        title_without_decline = decline_pattern.sub('', title_without_show)

        # Remove everything after "Continued"
        continued_match = continued_pattern.search(title_without_decline)
        if continued_match:
            title_without_continued = title_without_decline[:continued_match.start()].rstrip()
        else:
            title_without_continued = title_without_decline

        # Remove organization names, excluded keywords, verb objects, and buybacks
        title_without_organization = organization_pattern.sub('', title_without_continued)
        title_without_excluded_keywords = exclude_pattern.sub('', title_without_organization)
        title_without_verb_objects = verb_object_pattern.sub('', title_without_excluded_keywords)
        title_without_buybacks = buybacks_pattern.sub('', title_without_verb_objects)

        # Find indices in the title based on different conditions
        if quarter_buybacks_pattern.search(title_without_organization):
            title_without_quarter_buybacks = quarter_buybacks_pattern.sub('', title_without_organization)
            indices_found = extract_indices_from_sentence(title_without_quarter_buybacks)
        elif verb_pattern.search(title_without_organization):
            # Split the sentence into phrases by commas or verbs
            phrases = re.split(r',| and | to | for | in | on | of | at ', title_without_verb_objects)
            indices_found = []
            for phrase in phrases:
                # Extract index names from each phrase
                indices_found.extend(extract_indices_from_sentence(phrase))

            # Remove any content after the last verb
            last_verb = verb_pattern.search(title_without_organization)
            if last_verb:
                title_without_content_after_last_verb = title_without_organization[:last_verb.end()].rstrip()
                indices_found_after_last_verb = extract_indices_from_sentence(title_without_content_after_last_verb)
                if indices_found_after_last_verb:
                    indices_found = indices_found_after_last_verb
        else:
            indices_found = extract_indices_from_sentence(title_without_verb_objects)

        # Update the 'Category' column with Buybacks if found in the title
        if buybacks_pattern.search(title_without_buybacks):
            data.loc[titles.index(title), 'Category'] += ', Buybacks'

        # Add the extracted indices to the indices_mentioned list
        if indices_found:
            indices_found = [index_name.strip() for index_name in indices_found]
            indices_mentioned.append(indices_found)
        else:
            indices_mentioned.append([])
            
    return indices_mentioned
  
def extract_index_name(title):
    # Remove any lowercase word that comes after "INDEX"
    post_index_pattern = re.compile(r'(?<=INDEX)\s+[a-z]+', flags=re.IGNORECASE)
    verb_pattern = re.compile(r'\b(?:Continued\s+To\s+Decline|Continued|Declining|Trend|Tick up|Show)\b', re.IGNORECASE)
    
    title = verb_pattern.sub('', title)
    title = post_index_pattern.sub('', title)

    consultation_pattern = r'\b(?:consultation)\b.*'
    title = re.sub(consultation_pattern, '', title, flags=re.IGNORECASE)
    title = re.sub('\b(?:Launched|Show|Announced|Announces|Result|Results|Update|Updates|Methodology|Launch|Launches|Additions|Rebalancing)\b.*', '', title, flags=re.IGNORECASE)
    title = re.sub('\b(?:on|for|about|regarding|concerning|in)\b.*', '', title, flags=re.IGNORECASE)
    title = re.sub('\b(?:by|with)\b.*', '', title, flags=re.IGNORECASE)
    title = re.sub('\b(?:of|and)\b', '', title, flags=re.IGNORECASE)

    consultation_pattern = r'\b(?:consultation)\b.*'
    title = re.sub(consultation_pattern, '', title, flags=re.IGNORECASE)

    title = re.sub(r'\b(?:Declining|Tick up|Show)\b', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\b(?:U\.S\.|U\.K\.|U\.A\.E\.)\b', lambda match: match.group(0).replace('.', ''), title)
    title = re.sub(r'\b(?:Updated)\b', '', title, flags=re.IGNORECASE)
    title = re.sub('\s+', ' ', title).strip()

    # Remove content like "2022 Review Results"
    results_pattern = r'\b(?:\d{4}\sReview\sResults)\b'
    title = re.sub(results_pattern, '', title, flags=re.IGNORECASE)

    # Remove content like "to Track Australia" after "Index"
    track_pattern = r'\b(?:to\s+Track\s+[a-zA-Z]+)\b'
    title = re.sub(track_pattern, '', title, flags=re.IGNORECASE)

    # Add this pattern to remove hyphen and following content after "Index"
    index_hyphen_pattern = r'(?<=Index)\s*-\s*.*'
    title = re.sub(index_hyphen_pattern, '', title, flags=re.IGNORECASE)

    # Add this pattern to remove spaces and following content after "indices"
    indices_space_pattern = r'(?<=indices)\s*.*'
    title = re.sub(indices_space_pattern, '', title, flags=re.IGNORECASE)

    # Remove unnecessary spaces at the beginning and end of the title
    title = title.strip()    
    return title


# ===================pdf 에서 내용 종목 코드 추출 Start ===================
stock_pattern = re.compile(r'\b[A-Z]{2,}\b')  # 종목 코드를 찾기 위한 정규 표현식

# 문제가 있는 PDF 링크를 저장할 리스트
unavailable_pdfs = []

## ===================종목코드 라벨링 Start (Unused) ===================
addition_pattern = re.compile(r'\b(?:addition|added)\b', re.IGNORECASE)
rebalancing_pattern = re.compile(r'\b(?:rebalancing|rebalanced)\b', re.IGNORECASE)
removal_pattern = re.compile(r'\b(?:removal|removed)\b', re.IGNORECASE)

def label_stocks(text, stocks):
    labeled_stocks = set()
    
    for stock in stocks:
        if addition_pattern.search(text):
            labeled_stocks.add(f"{stock}_addition")
        elif rebalancing_pattern.search(text):
            labeled_stocks.add(f"{stock}_rebalancing")
        elif removal_pattern.search(text):
            labeled_stocks.add(f"{stock}_removal")
        else:
            labeled_stocks.add(stock)
    
    return labeled_stocks

def extract_text_from_pdf_with_ocr(pdf_data):
    img = Image.open(io.BytesIO(pdf_data))
    text = pytesseract.image_to_string(img)
    return text

def extract_stocks_from_pdf(pdf_url):
    # Check if the URL has a valid scheme
    parsed_url = urlparse(str(pdf_url))
    if not parsed_url.scheme or not parsed_url.netloc:
        print(f"Invalid URL: {pdf_url}")
        return set()

    response = requests.get(pdf_url)
    try:
        pdf_file = PdfFileReader(BytesIO(response.content))
    except (utils.PdfReadError, IOError):
        print(f"Unable to read PDF file with PyPDF4: {pdf_url}")
        print("Trying with pdfplumber...")

        try:
            with pdfplumber.open(BytesIO(response.content)) as pdf_file:
                stocks = set()
                for page in pdf_file.pages:
                    text = page.extract_text()
                    stocks_in_page = stock_pattern.findall(text)
                    labeled_stocks = label_stocks(text, stocks_in_page)
                    stocks.update(labeled_stocks)
                return stocks
        except Exception as e:
            print(f"Unable to read PDF file with pdfplumber: {pdf_url}")
            print("Trying with OCR...")
            try:
                text = extract_text_from_pdf_with_ocr(response.content)
                stocks = stock_pattern.findall(text)
                labeled_stocks = label_stocks(text, stocks)
                return set(labeled_stocks)
            except Exception as e:
                print(f"Unable to extract text with OCR: {pdf_url}")
                unavailable_pdfs.append(pdf_url)
                return set()

    stocks = set()
    for page_num in range(pdf_file.getNumPages()):
        text = pdf_file.getPage(page_num).extractText()
        stocks_in_page = stock_pattern.findall(text)
        labeled_stocks = label_stocks(text, stocks_in_page)
        stocks.update(labeled_stocks)

    return stocks

all_indices_mentioned = extract_indices_mentioned(titles)
data['Indices_Mentioned'] = all_indices_mentioned

# ===================pdf 에서 내용 종목 코드 추출 End ===================
## ===================종목코드 라벨링 End ===================

# 종목명을 추출하고 데이터프레임에 추가합니다.
stocks_mentioned = []
for pdf_link in tqdm(pdf_links):
    stocks = extract_stocks_from_pdf(pdf_link)
    stocks_mentioned.append(stocks)

data['Stocks'] = stocks_mentioned
data.to_excel("s_and_p_500_data_IA.xlsx", index=False)  # Index Added
# %% 7 案 : with pdf handling + Multiprocessing
"""
import requests
from io import BytesIO
import io
from PyPDF4 import PdfFileReader, utils
import pdfplumber
import re
from tqdm import tqdm
import pandas as pd
import pytesseract
from PIL import Image
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Load the data
data = pd.read_excel("s_and_p_500_data.xlsx")
pdf_links = data['PDF Link']
titles = data['Title']

def classify_titles(title_list):
# Function to classify the titles into categories
    categories = {
        'inclusion_exclusion': [],
        'rebalancing': [],
        'price_index': [],
        'methodology_change': [],
        'general_update': [],
        'other': []
    }

    # Keywords for each category
    inclusion_exclusion_keywords = ['join', 'set to', 'constituent change', 'enter', 'added', 'removed', 'reconstitution', 'treatment']
    rebalancing_keywords = ['rebalancing', 'rebalance']
    price_index_keywords = ['case-shiller', 'home price']
    methodology_change_keywords = ['modification', 'consultation']


    # Iterate through the title list and classify each title
    for index, title in title_list.iteritems():
        lowercase_title = title.lower()
        classified = []

        # Check for keywords and classify accordingly
        if any(keyword in lowercase_title for keyword in inclusion_exclusion_keywords):
            classified.append('inclusion_exclusion')
        if any(keyword in lowercase_title for keyword in rebalancing_keywords):
            classified.append('rebalancing')
        if any(keyword in lowercase_title for keyword in price_index_keywords):
            classified.append('price_index')
        if any(keyword in lowercase_title for keyword in methodology_change_keywords):
            classified.append('methodology_change')
        if 'update' in lowercase_title:
            classified.append('general_update')

        # If the title doesn't fit any category, classify it as 'other'
        if not classified:
            classified.append('other')

        # Update the data with the classified category (any_keword)  
        data.loc[index, 'Category_AK'] = ', '.join(classified) 

    return categories

# Function to extract indices from a given sentence
def extract_indices_from_sentence(sentence):
    # Define the index pattern and the unwanted content pattern
    index_pattern = re.compile(r"(?:S&P[^,]*?)(?:Index|Indices)")
    unwanted_content_before_index_pattern = re.compile(r"(S&P Global Sustainable1 Launch)")

    # Find all matches for index names
    matches = index_pattern.findall(sentence)

    # Iterate over each match and remove the unwanted content
    cleaned_matches = []
    for match in matches:
        cleaned_match = unwanted_content_before_index_pattern.sub("", match).strip()
        cleaned_matches.append(cleaned_match)

    return cleaned_matches

# Function to extract indices mentioned in the titles
def extract_indices_mentioned(title_list):
    indices_mentioned = []

    # Define patterns to remove certain keywords and phrases from titles
    consultation_pattern = re.compile(r'\b(?:consultation\b.*).*', flags=re.IGNORECASE)
    show_pattern = re.compile(r'\b(?:Show\b.*).*', flags=re.IGNORECASE)
    decline_pattern = re.compile(r'\b(?:Decline\b.*).*', flags=re.IGNORECASE)

    organization_pattern = re.compile(r'S&P Dow Jones Indices')
    verb_pattern = re.compile(r'\b(?:Continued\s+To\s+Decline|Continued|Declining|Trend|Tick up|Show|Reports)\b', re.IGNORECASE)
    exclude_pattern = re.compile(r'\b(?:Trend|Continued|Methodology Update|Consultation|Composite Rate|For|Consecutive|Month|Straight|Increase|Drop|Loan Types)\b', re.IGNORECASE)
    verb_object_pattern = re.compile(r'\b(?:on|of|at|in|to|for)\b\s+(?:Constituent Weighting|Minimum Size Threshold|Eligibility Factors|the)', re.IGNORECASE)
    buybacks_pattern = re.compile(r'\b(?:Buybacks)\b', re.IGNORECASE)
    quarter_buybacks_pattern = re.compile(r'\b(?:Q\d{1}\s\d{4}\sBuybacks)\b', re.IGNORECASE)

    # Add this pattern to find content like "Continued"
    continued_pattern = re.compile(r'\b(?:Continued)\b', re.IGNORECASE)

    for title in title_list:
        # Remove consultation and everything following it
        title_without_consultation = consultation_pattern.sub('', title)

        # Remove "Show" and everything following it
        title_without_show = show_pattern.sub('', title_without_consultation)

        # Remove "Decline" and everything following it
        title_without_decline = decline_pattern.sub('', title_without_show)

        # Remove everything after "Continued"
        continued_match = continued_pattern.search(title_without_decline)
        if continued_match:
            title_without_continued = title_without_decline[:continued_match.start()].rstrip()
        else:
            title_without_continued = title_without_decline

        # Remove organization names, excluded keywords, verb objects, and buybacks
        title_without_organization = organization_pattern.sub('', title_without_continued)
        title_without_excluded_keywords = exclude_pattern.sub('', title_without_organization)
        title_without_verb_objects = verb_object_pattern.sub('', title_without_excluded_keywords)
        title_without_buybacks = buybacks_pattern.sub('', title_without_verb_objects)

        # Find indices in the title based on different conditions
        if quarter_buybacks_pattern.search(title_without_organization):
            title_without_quarter_buybacks = quarter_buybacks_pattern.sub('', title_without_organization)
            indices_found = extract_indices_from_sentence(title_without_quarter_buybacks)
        elif verb_pattern.search(title_without_organization):
            # Split the sentence into phrases by commas or verbs
            phrases = re.split(r',| and | to | for | in | on | of | at ', title_without_verb_objects)
            indices_found = []
            for phrase in phrases:
                # Extract index names from each phrase
                indices_found.extend(extract_indices_from_sentence(phrase))

            # Remove any content after the last verb
            last_verb = verb_pattern.search(title_without_organization)
            if last_verb:
                title_without_content_after_last_verb = title_without_organization[:last_verb.end()].rstrip()
                indices_found_after_last_verb = extract_indices_from_sentence(title_without_content_after_last_verb)
                if indices_found_after_last_verb:
                    indices_found = indices_found_after_last_verb
        else:
            indices_found = extract_indices_from_sentence(title_without_verb_objects)

        # Update the 'Category' column with Buybacks if found in the title
        if buybacks_pattern.search(title_without_buybacks):
            data.loc[titles.index(title), 'Category'] += ', Buybacks'

        # Add the extracted indices to the indices_mentioned list
        if indices_found:
            indices_found = [index_name.strip() for index_name in indices_found]
            indices_mentioned.append(indices_found)
        else:
            indices_mentioned.append([])
            
    return indices_mentioned

# Function to download a PDF from a given URL
def download_pdf(url):
    response = requests.get(url)
    content = response.content
    try:
        PdfFileReader(BytesIO(content))
        return BytesIO(content)
    except utils.PdfReadError:
        return None

# Function to process a PDF and extract the mentioned indices
def process_pdf(pdf_link):
    return extract_stocks_from_pdf(pdf_link)

def extract_stocks_from_pdf(pdf_url):
    # Check if the URL has a valid scheme
    parsed_url = urlparse(str(pdf_url))
    if not parsed_url.scheme or not parsed_url.netloc:
        print(f"Invalid URL: {pdf_url}")
        return set()

    response = requests.get(pdf_url)
    try:
        pdf_file = PdfFileReader(BytesIO(response.content))
    except (utils.PdfReadError, IOError):
        print(f"Unable to read PDF file with PyPDF4: {pdf_url}")
        print("Trying with pdfplumber...")

        try:
            with pdfplumber.open(BytesIO(response.content)) as pdf_file:
                stocks = set()
                for page in pdf_file.pages:
                    text = page.extract_text()
                    stocks_in_page = stock_pattern.findall(text)
                    labeled_stocks = label_stocks(text, stocks_in_page)
                    stocks.update(labeled_stocks)
                return stocks
        except Exception as e:
            print(f"Unable to read PDF file with pdfplumber: {pdf_url}")
            print("Trying with OCR...")
            try:
                text = extract_text_from_pdf_with_ocr(response.content)
                stocks = stock_pattern.findall(text)
                labeled_stocks = label_stocks(text, stocks)
                return set(labeled_stocks)
            except Exception as e:
                print(f"Unable to extract text with OCR: {pdf_url}")
                unavailable_pdfs.append(pdf_url)
                return set()

    stocks = set()
    for page_num in range(pdf_file.getNumPages()):
        text = pdf_file.getPage(page_num).extractText()
        stocks_in_page = stock_pattern.findall(text)
        labeled_stocks = label_stocks(text, stocks_in_page)
        stocks.update(labeled_stocks)

    return stocks
all_indices_mentioned = extract_indices_mentioned(titles)
data['Indices_Mentioned'] = all_indices_mentioned

# ===================pdf 에서 내용 종목 코드 추출 End ===================
## ===================종목코드 라벨링 End ===================

# 종목명을 추출하고 데이터프레임에 추가합니다.
stocks_mentioned = []

with ThreadPoolExecutor(max_workers=5) as executor:
    stocks_mentioned = list(tqdm(executor.map(process_pdf, pdf_links), total=len(pdf_links)))

data['Stocks'] = stocks_mentioned
data.to_excel("s_and_p_500_data_IA.xlsx", index=False)  # Index Added
"""
# %% ③ Extracting info from pdfs  #################################################### 
# %% ③ Tabula -1 案
"""
"""
 # - PDF → Excel 化 + 표 出
"""
import requests
import pandas as pd
import os
from tqdm import tqdm
from pdf2image import convert_from_path, convert_from_bytes
from PyPDF2 import PdfFileReader
import tabula
from io import BytesIO

# 사용하려는 PDF URL 목록에 해당하는 코드를 사용하십시오.
data = pd.read_excel("s_and_p_500_data.xlsx")
pdf_links = data['PDF Link']

def extract_table_from_pdf(pdf_url, failed_pdfs):
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error while downloading PDF: {pdf_url}")
        print(e)
        failed_pdfs[pdf_url] = "download_error"
        return [pd.DataFrame()]

    with BytesIO(response.content) as pdf_data:
        try:
            dfs = tabula.read_pdf(pdf_data, pages="all", multiple_tables=True, stream=True, lattice = True)
            # """
            # # ○ tabula.read_pdf
            # #  - Extract table from pdf 
            # #  - stream vs Lattice : Horizontal Vs Grid 
            # """
"""
        except Exception as e:
            print(f"Error while extracting tables from PDF: {pdf_url}")
            print(e)
            failed_pdfs[pdf_url] = "extraction_error"
            dfs = [pd.DataFrame()]

    return dfs

def process_table(df, pdf_url):
    # PDF 링크를 새 열로 추가합니다.
    df['PDF Link'] = pdf_url
    # 여기에서 추가로 표를 처리하고 정리할 수 있습니다.
    return df

failed_pdfs = {}
final_df = pd.DataFrame()

for pdf_url in tqdm(pdf_links):
    tables = extract_table_from_pdf(pdf_url, failed_pdfs)

    for table in tables:
        processed_table = process_table(table, pdf_url)
        final_df = final_df.append(processed_table, ignore_index=True)

print("Failed PDFs:")
for pdf, error_type in failed_pdfs.items():
    print(f"PDF: {pdf}, Error Type: {error_type}")

print("Final DataFrame:")
print(final_df)
"""
# %% ③ Tabula -2 案 : Multiprocessing
"""
import requests
import pandas as pd
import os
from tqdm import tqdm
from io import BytesIO
import tabula
from multiprocessing import Pool, cpu_count

# 사용하려는 PDF URL 목록에 해당하는 코드를 사용하십시오.
data = pd.read_excel("s_and_p_500_data.xlsx")
pdf_links = data['PDF Link']

def extract_table_from_pdf(pdf_url):
    failed_pdfs = {}
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error while downloading PDF: {pdf_url}")
        print(e)
        failed_pdfs[pdf_url] = "download_error"
        return pd.DataFrame(), failed_pdfs

    with BytesIO(response.content) as pdf_data:
        try:
            dfs = tabula.read_pdf(pdf_data, pages="all", multiple_tables=True, stream=False, lattice=True)
        except Exception as e:
            print(f"Error while extracting tables from PDF: {pdf_url}")
            print(e)
            failed_pdfs[pdf_url] = "extraction_error"
            dfs = [pd.DataFrame()]

    return dfs, failed_pdfs

def process_table(df, pdf_url):
    df['PDF Link'] = pdf_url
    return df

def process_pdfs(pdf_links):
    pdf_links_chunks = [pdf_links[i:i+cpu_count()] for i in range(0, len(pdf_links), cpu_count())]

    final_dfs = []
    failed_pdfs = {}
    with Pool(cpu_count()) as p:
        for pdf_links_chunk in pdf_links_chunks:
            results = p.map(extract_table_from_pdf, pdf_links_chunk)
            for pdf_url, (tables, errors) in zip(pdf_links_chunk, results):
                for table in tables:
                    processed_table = process_table(table, pdf_url)
                    final_dfs.append(processed_table)
                failed_pdfs.update(errors)

    return final_dfs, failed_pdfs

if __name__ == "__main__":
    final_dfs, failed_pdfs = process_pdfs(pdf_links)
    final_df = pd.concat(final_dfs, axis=0, ignore_index=True)
    
    print("Failed PDFs:")
    for pdf, error_type in failed_pdfs.items():
        print(f"PDF: {pdf}, Error Type: {error_type}")

    print("Final DataFrame:")
    print(final_df)
"""
# %% ③ Tabula -3 案 : Multiprocessing - Threads
import pandas as pd
import requests
from io import BytesIO
import tabula
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# data = pd.read_excel("s_and_p_500_data.xlsx")
data = pd.read_excel("s_and_p_500_data_IA.xlsx") # IA & Category
pdf_links = data['PDF Link'][:50]

def extract_table_from_pdf(pdf_url):
    failed_pdfs = {}
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error while downloading PDF: {pdf_url}")
        print(e)
        failed_pdfs[pdf_url] = "download_error"
        return pd.DataFrame(), failed_pdfs

    with BytesIO(response.content) as pdf_data:
        try:
            dfs = tabula.read_pdf(pdf_data, pages="all", multiple_tables=True, stream=True, lattice=True)
        except Exception as e:
            print(f"Error while extracting tables from PDF: {pdf_url}")
            print(e)
            failed_pdfs[pdf_url] = "extraction_error"
            dfs = [pd.DataFrame()]

    return dfs, failed_pdfs

def process_table(df, pdf_url):
    df['PDF Link'] = pdf_url
    return df

def process_pdfs(pdf_links):
    final_dfs = []
    failed_pdfs = {}

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(extract_table_from_pdf, pdf_url): pdf_url for pdf_url in pdf_links}
        
        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing PDFs"):
            pdf_url = futures[future]
            try:
                tables, errors = future.result()
                for table in tables:
                    processed_table = process_table(table, pdf_url)
                    final_dfs.append(processed_table)
                failed_pdfs.update(errors)
            except Exception as e:
                print(f"Error occurred while processing PDF: {pdf_url}")
                print(e)

    return final_dfs, failed_pdfs

if __name__ == "__main__":
    final_dfs, failed_pdfs = process_pdfs(pdf_links)
    final_df = pd.concat(final_dfs, axis=0, ignore_index=True)
    
    print("Failed PDFs:")
    for pdf, error_type in failed_pdfs.items():
        print(f"PDF: {pdf}, Error Type: {error_type}")

    print("Final DataFrame:")
    print(final_df)
    # final_df.to_excel("s_and_p_500_data_PDFtable.xlsx", index=False)  # Index Added
    final_df.to_excel("s_and_p_500_data_PDFtable_tabula(Sample).xlsx", index=False)  # Index Added

# %% ③ Tabula -4 案 : 特)split table by last row 
"""
 - Column 명이 날라가기는 하나 순서대로 Row 내용이 잘 출력되는 것으로 보임 (열 이름 추출 및 재구성 要)
"""
import pandas as pd
import requests
from io import BytesIO
import tabula
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

data = pd.read_excel("s_and_p_500_data_IA.xlsx")  # IA & Category
pdf_links = data['PDF Link'][:50]

def split_table_by_last_row(df):
    last_row = df.iloc[-1]

    column_starts = []
    for idx, value in enumerate(last_row):
        if pd.notnull(value):
            column_starts.append(idx)

    new_df = pd.DataFrame()
    for idx, col_start in enumerate(column_starts):
        if idx < len(column_starts) - 1:
            new_df[f'Column {idx + 1}'] = df.iloc[:, col_start:column_starts[idx + 1]].fillna('').apply(' '.join, axis=1)
        else:
            new_df[f'Column {idx + 1}'] = df.iloc[:, col_start:].fillna('').apply(' '.join, axis=1)

    return new_df

def extract_table_from_pdf(pdf_url):
    failed_pdfs = {}
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error while downloading PDF: {pdf_url}")
        print(e)
        failed_pdfs[pdf_url] = "download_error"
        return pd.DataFrame(), failed_pdfs

    with BytesIO(response.content) as pdf_data:
        try:
            dfs = tabula.read_pdf(pdf_data, pages="all", multiple_tables=True, lattice=True, stream=True)
            dfs = [df.replace('\n', ' ', regex=True) for df in dfs]
        except Exception as e:
            print(f"Error while extracting tables from PDF: {pdf_url}")
            print(e)
            failed_pdfs[pdf_url] = "extraction_error"
            dfs = [pd.DataFrame()]

    return dfs, failed_pdfs

def process_table(df, pdf_url):
    df = split_table_by_last_row(df)
    df['PDF Link'] = pdf_url
    return df

def process_pdfs(pdf_links):
    final_dfs = []
    failed_pdfs = {}

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(extract_table_from_pdf, pdf_url): pdf_url for pdf_url in pdf_links}

        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing PDFs"):
            pdf_url = futures[future]
            try:
                tables, errors = future.result()
                for table in tables:
                    processed_table = process_table(table, pdf_url)
                    final_dfs.append(processed_table)
                failed_pdfs.update(errors)
            except Exception as e:
                print(f"Error occurred while processing PDF: {pdf_url}")
                print(e)

    return final_dfs, failed_pdfs

if __name__ == "__main__":
    final_dfs, failed_pdfs = process_pdfs(pdf_links)
    final_df = pd.concat(final_dfs, axis=0, ignore_index=True)

    print("Failed PDFs:")
    for pdf, error_type in failed_pdfs.items():
        print(f"PDF: {pdf}, Error Type: {error_type}")

    print("Final DataFrame:")
    print(final_df)
    final_df.to_excel("s_and_p_500_data_PDFtable_tabula(Sample).xlsx", index=False)  # Index Added
    
# %% ③ Tabula -5 案 : 재 수정 
import pandas as pd
import requests
from io import BytesIO
import tabula
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

data = pd.read_excel("s_and_p_500_data_IA.xlsx")  # IA & Category
pdf_links = data['PDF Link'][:50]

def split_table_by_last_row(df):
    last_row = df.iloc[-1]

    column_starts = []
    for idx, value in enumerate(last_row):
        if pd.notnull(value):
            column_starts.append(idx)

    new_df = pd.DataFrame()
    for idx, col_start in enumerate(column_starts):
        if idx < len(column_starts) - 1:
            new_df[f'Column {idx + 1}'] = df.iloc[:, col_start:column_starts[idx + 1]].fillna('').apply(' '.join, axis=1)
        else:
            new_df[f'Column {idx + 1}'] = df.iloc[:, col_start:].fillna('').apply(' '.join, axis=1)

    return new_df

def extract_table_from_pdf(pdf_url):
    failed_pdfs = {}
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error while downloading PDF: {pdf_url}")
        print(e)
        failed_pdfs[pdf_url] = "download_error"
        return pd.DataFrame(), failed_pdfs

    with BytesIO(response.content) as pdf_data:
        try:
            dfs = tabula.read_pdf(pdf_data, pages="all", multiple_tables=True, lattice=True, stream=True)
            dfs = [df.replace('\n', ' ', regex=True) for df in dfs]
        except Exception as e:
            print(f"Error while extracting tables from PDF: {pdf_url}")
            print(e)
            failed_pdfs[pdf_url] = "extraction_error"
            dfs = [pd.DataFrame()]

        # Print extracted tables
        print(f"Extracted tables from PDF: {pdf_url}")
        for i, df in enumerate(dfs):
            print(f"Table {i + 1}:")
            print(df)

    return dfs, failed_pdfs

def process_table(df, pdf_url):
    df = split_table_by_last_row(df)
    df['PDF Link'] = pdf_url
    return df

def process_pdfs(pdf_links):
    final_dfs = []
    failed_pdfs = {}

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(extract_table_from_pdf, pdf_url): pdf_url for pdf_url in pdf_links}

        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing PDFs"):
            pdf_url = futures[future]
            try:
                tables, errors = future.result()
                for table in tables:
                    processed_table = process_table(table, pdf_url)
                    final_dfs.append(processed_table)
                failed_pdfs.update(errors)
            except Exception as e:
                print(f"Error occurred while processing PDF: {pdf_url}")
                print(e)

    return final_dfs, failed_pdfs

if __name__ == "__main__":
    final_dfs, failed_pdfs = process_pdfs(pdf_links)
    final_df = pd.concat(final_dfs, axis=0, ignore_index=True)

    print("Failed PDFs:")
    for pdf, error_type in failed_pdfs.items():
        print(f"PDF: {pdf}, Error Type: {error_type}")

    print("Final DataFrame:")
    print(final_df)
    final_df.to_excel("s_and_p_500_data_PDFtable_tabula(Sample).xlsx", index=False)  # Index Added

# %% ③ Tabula -6 案 : 중복된 열 허용 + 디버깅 로그 추가 
import pandas as pd
import requests
from io import BytesIO
import tabula
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

data = pd.read_excel("s_and_p_500_data_IA.xlsx")  # IA & Category
pdf_links = data['PDF Link'][:50]

def create_multiindex_columns(df):
    multiindex_columns = pd.MultiIndex.from_arrays(df.iloc[:2].values)
    df = df.iloc[2:].reset_index(drop=True)
    df.columns = multiindex_columns
    return df

def extract_table_from_pdf(pdf_url):
    failed_pdfs = {}
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error while downloading PDF: {pdf_url}")
        print(e)
        failed_pdfs[pdf_url] = "download_error"
        return pd.DataFrame(), failed_pdfs

    with BytesIO(response.content) as pdf_data:
        try:
            dfs = tabula.read_pdf(pdf_data, pages="all", multiple_tables=True, lattice=True)  # Option adjusted
            dfs = [df.replace('\n', ' ', regex=True) for df in dfs]
        except Exception as e:
            print(f"Error while extracting tables from PDF: {pdf_url}")
            print(e)
            failed_pdfs[pdf_url] = "extraction_error"
            dfs = [pd.DataFrame()]

    return dfs, failed_pdfs

def process_table(df, pdf_url):
    # Data preprocessing
    if len(df) > 1:
        # Check if the table has a multi-level header and apply it
        if all(df.iloc[:2].applymap(lambda x: isinstance(x, str))):
            df = create_multiindex_columns(df)

        # Check if the first row contains valid column names
        elif not any(["Unnamed" in str(col) for col in df.columns]):
            # If not, shift the data from the wrongly named columns to the correct ones
            for col in df.columns:
                if "Unnamed" in col:
                    correct_col = df.columns[df.columns.get_loc(col) - 1]
                    df[correct_col] = df[correct_col].fillna(df[col])
                    df = df.drop(col, axis=1)

            # Reset the index
            df = df.reset_index(drop=True)
        else:
            # Rename duplicate columns
            df.columns = pd.Series(df.columns).apply(lambda x: x if not x.startswith("Unnamed") else x + "_dup")
    else:
        # Single-level header with one level
        if isinstance(df.columns, pd.MultiIndex) and len(df.columns.levels) == 1:
            df.columns = df.columns.droplevel()

    df['PDF Link'] = pdf_url
    return df




def process_pdfs(pdf_links):
    final_dfs = []
    failed_pdfs = {}

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(extract_table_from_pdf, pdf_url): pdf_url for pdf_url in pdf_links}

        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing PDFs"):
            pdf_url = futures[future]
            try:
                tables, errors = future.result()
                for table in tables:
                    processed_table = process_table(table, pdf_url)
                    if not processed_table.empty:
                        final_dfs.append(processed_table)
                failed_pdfs.update(errors)
            except Exception as e:
                print(f"Error occurred while processing PDF: {pdf_url}")
                print(e)

    return final_dfs, failed_pdfs

if __name__ == "__main__":
    final_dfs, failed_pdfs = process_pdfs(pdf_links)
    if final_dfs:
        final_df = pd.concat(final_dfs, axis=0, ignore_index=True)
        print("Final DataFrame:")
        print(final_df)
        final_df.to_excel("s_and_p_500_data_PDFtable_tabula(Sample).xlsx", index=False)  # Index Added
    else:
        print("No data to concatenate.")

    print("Failed PDFs:")
    for pdf, error_type in failed_pdfs.items():
        print(f"PDF: {pdf}, Error Type: {error_type}")
# %% Amend Columns
import difflib

def correct_column_name(column_name, reference_names, threshold=0.8):
    matches = difflib.get_close_matches(column_name, reference_names, n=1, cutoff=threshold)
    if matches:
        return matches[0]
    else:
        return column_name

def process_table(df, pdf_url):
    # Data preprocessing
    df = df.dropna(axis=1, how='all')
    df = df.dropna(axis=0, how='all')

    if isinstance(df.columns, pd.MultiIndex) and len(df.columns.levels) == 1:
        df.columns = df.columns.droplevel()

    # Correct column names
    reference_names = ['Effective Date', 'Action']
    df.columns = [correct_column_name(col, reference_names) for col in df.columns]

    df['PDF Link'] = pdf_url
    return df

# %% ③-4-1 案 : camelot
import pandas as pd
import requests
from io import BytesIO
import fitz  # PyMuPDF
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import tempfile
import os
import camelot

data = pd.read_excel("s_and_p_500_data_IA.xlsx")  # IA & Category
pdf_links = data['PDF Link']


def extract_table_with_camelot(pdf_data):
    try:
        with open('temp.pdf', 'wb') as f:
            f.write(pdf_data)

        tables = camelot.read_pdf('temp.pdf', pages='1', flavor='stream')

        dfs = []
        for table in tables:
            df = table.df
            # Update column names with the first row and remove the first row
            df.columns = df.iloc[0]
            df = df.iloc[1:].reset_index(drop=True)
            dfs.append(df)

    except Exception as e:
        print(f"Error while extracting tables with Camelot: {e}")
        dfs = [pd.DataFrame()]

    return dfs


def extract_table_from_pdf(pdf_url):
    failed_pdfs = {}
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error while downloading PDF: {pdf_url}")
        print(e)
        failed_pdfs[pdf_url] = "download_error"
        return pd.DataFrame(), failed_pdfs

    dfs = extract_table_with_camelot(response.content)

    return dfs, failed_pdfs

def process_table(df, pdf_url):
    df['PDF Link'] = pdf_url
    return df

def process_pdfs(pdf_links):
    final_dfs = []
    failed_pdfs = {}

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(extract_table_from_pdf, pdf_url): pdf_url for pdf_url in pdf_links}

        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing PDFs"):
            pdf_url = futures[future]
            try:
                tables, errors = future.result()
                for table in tables:
                    processed_table = process_table(table, pdf_url)
                    final_dfs.append(processed_table)
                failed_pdfs.update(errors)
            except Exception as e:
                print(f"Error occurred while processing PDF: {pdf_url}")
                print(e)

    return final_dfs, failed_pdfs

if __name__ == "__main__":
    final_dfs, failed_pdfs = process_pdfs(pdf_links)
    final_df = pd.concat(final_dfs, axis=0, ignore_index=True)

    print("Failed PDFs:")
    for pdf, error_type in failed_pdfs.items():
        print(f"PDF: {pdf}, Error Type: {error_type}")

    print("Final DataFrame:")
    print(final_df)
    final_df.to_excel("s_and_p_500_data_PDFtable_temp.xlsx", index=False)  # Index Added

# %% ③-4-2 案 : camelot + PDF Merge Amended
import pandas as pd
import requests
from io import BytesIO
import fitz  # PyMuPDF
import warnings
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import tempfile
import os
import camelot

data = pd.read_excel("s_and_p_500_data_IA.xlsx")  # IA & Category
pdf_links = data['PDF Link'][0:30]

def extract_table_with_camelot(pdf_data):
    tables = []  # Initialize the 'tables' variable
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = os.path.join(temp_dir, 'temp.pdf')
            with open(temp_file_path, 'wb') as f:
                f.write(pdf_data)

            # Try extracting tables using the 'lattice' flavor
            tables = camelot.read_pdf(temp_file_path, pages='all', flavor='lattice')

            # If no tables were found, try the 'stream' flavor
            if len(tables) == 0:
                tables = camelot.read_pdf(temp_file_path, pages='all', flavor='stream')

            dfs = []
            for table in tables:
                df = table.df
                # Update column names with the first row and remove the first row
                df.columns = df.iloc[0]
                df = df.iloc[1:].reset_index(drop=True)
                dfs.append(df)

    except Exception as e:
        print(f"Error while extracting tables with Camelot: {e}")
        dfs = [pd.DataFrame()]

    return [df.reset_index(drop=True) for df in dfs], (len(tables) == 0)  # Add an indicator of whether tables were found


def extract_table_from_pdf(pdf_url):
    failed_pdfs = {}
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error while downloading PDF: {pdf_url}")
        print(e)
        failed_pdfs[pdf_url] = "download_error"
        return [(pd.DataFrame(), False)], failed_pdfs  # Return a list of tuples

    dfs, failed = extract_table_with_camelot(response.content)
    return [(df, failed) for df in dfs], failed_pdfs  # Return a list of tuples


def merge_duplicate_columns(df):
    new_df = df.copy()
    column_groups = df.columns.to_series().groupby(df.columns).groups
    for name, columns in column_groups.items():
        if len(columns) > 1:
            columns_to_merge = new_df[columns]
            new_df[name] = columns_to_merge.apply(lambda x: x.dropna().iloc[0] if x.dropna().size > 0 else None, axis=1)
            new_df = new_df.drop(columns=columns[1:])
    return new_df

def process_table(df, pdf_url):
    df = df.reset_index(drop=True)
    df = merge_duplicate_columns(df)
    df['PDF Link'] = pdf_url
    return df

def process_pdfs(pdf_links):
    final_dfs = []
    failed_pdfs = {}
    failed_to_extract = []

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(extract_table_from_pdf, pdf_url): pdf_url for pdf_url in pdf_links}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing PDFs"):
            pdf_url = futures[future]
            try:
                tables, errors = future.result()
                found_tables = False  # Add a flag to check if any tables were found
                for df, failed in tables:  # Use 'df' instead of 'table'
                    if not df.empty:
                        processed_table = process_table(df, pdf_url)
                        final_dfs.append(processed_table)
                        found_tables = True  # Set the flag to True if a table was found
                if not found_tables:  # If no tables were found, add the PDF link to the list
                    failed_to_extract.append(pdf_url)
                failed_pdfs.update(errors)
            except Exception as e:
                print(f"Error occurred while processing PDF: {pdf_url}")
                print(e)

    return final_dfs, failed_pdfs, failed_to_extract

if __name__ == "__main__":
    final_dfs, failed_pdfs, failed_to_extract = process_pdfs(pdf_links)
    final_df = pd.concat(final_dfs, axis=0, ignore_index=True)

    print("Failed PDFs:")
    for pdf, error_type in failed_pdfs.items():
        print(f"PDF: {pdf}, Error Type: {error_type}")

    print("Failed to extract tables from the following PDFs:")
    for pdf in failed_to_extract:
        print(pdf)

    print("Final DataFrame:")
    print(final_df)
    final_df.to_excel("s_and_p_500_data_PDFtable_temp.xlsx", index=False)  # Index Added

# %% ③-4-3 案 : camelot + PDF Merge Amended + popplerqt5
import pandas as pd
import requests
from io import BytesIO
import fitz  # PyMuPDF
import warnings
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import tempfile
import os
import camelot
import cv2
import numpy as np
from PyPDF4 import PdfFileReader, PdfFileWriter

data = pd.read_excel("s_and_p_500_data_IA.xlsx")  # IA & Category
pdf_links = data['PDF Link'][0:30]


def repair_pdf(pdf_data):
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = os.path.join(temp_dir, 'temp.pdf')
            with open(temp_file_path, 'wb') as f:
                f.write(pdf_data)
            input_pdf = PdfFileReader(temp_file_path)
            output_pdf = PdfFileWriter()
            for i in range(len(input_pdf.pages)):
                output_pdf.addPage(input_pdf.getPage(i))

            with tempfile.TemporaryFile() as repaired_pdf:
                output_pdf.write(repaired_pdf)
                repaired_pdf.seek(0)
                pdf_data = repaired_pdf.read()
    except Exception as e:
        print(f"Error while repairing PDF: {e}")

    return pdf_data

def has_black_background(image, threshold=0.5):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    black_pixels = np.sum(gray < 128)
    total_pixels = gray.size
    black_ratio = black_pixels / total_pixels
    return black_ratio > threshold

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    inverted = 255 - binary
    return inverted

def pdf_to_images(pdf_data):
    with tempfile.NamedTemporaryFile(suffix=".pdf") as pdf_file:
        pdf_file.write(pdf_data)
        pdf_file.flush()
        doc = fitz.open(pdf_file.name)
        images = []
        for page in doc:
            pix = page.get_pixmap()
            img = cv2.imdecode(np.frombuffer(pix.getImageData(), np.uint8), cv2.IMREAD_COLOR)
            images.append(img)
    return images

def extract_table_with_camelot(pdf_data):
    tables = []
    try:
        images = pdf_to_images(pdf_data)
        preprocessed_images = []
        for image in images:
            if has_black_background(image):
                preprocessed_image = preprocess_image(image)
                preprocessed_images.append(preprocessed_image)
            else:
                preprocessed_images.append(image)

        with tempfile.TemporaryDirectory() as temp_dir:
            preprocessed_pdf_path = os.path.join(temp_dir, "preprocessed.pdf")
            doc = fitz.open()
            for img in preprocessed_images:
                pixmap = fitz.Pixmap(fitz.csRGB, img.shape[0], img.shape[1], img.tobytes())
                page = doc.new_page(width=pixmap.width, height=pixmap.height)
                page.insert_image(page.rect, pixmap=pixmap)
            doc.save(preprocessed_pdf_path)
            tables = camelot.read_pdf(preprocessed_pdf_path, pages='all', flavor='lattice')
            if len(tables) == 0:
                tables = camelot.read_pdf(preprocessed_pdf_path, pages='all', flavor='stream')
            dfs = []
            for table in tables:
                df = table.df
                df.columns = df.iloc[0]
                df = df.iloc[1:].reset_index(drop=True)
                dfs.append(df)
    except Exception as e:
        print(f"Error while extracting tables with Camelot: {e}")
        dfs = [pd.DataFrame()]
    return [df.reset_index(drop=True) for df in dfs], (len(tables) == 0)  # Add an indicator of whether tables were found

def extract_table_from_pdf(pdf_url):
    failed_pdfs = {}
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error while downloading PDF: {pdf_url}")
        print(e)
        failed_pdfs[pdf_url] = "download_error"
        return [pd.DataFrame()], failed_pdfs  # Return a list of DataFrames

    pdf_data = response.content
    pdf_data = repair_pdf(pdf_data)  # Try to repair the PDF
    dfs, failed = extract_table_with_camelot(pdf_data)
    return dfs, failed_pdfs  # Return a list of DataFrames

warnings.filterwarnings("ignore", category=UserWarning)

pdf_dfs = []
failed_pdfs = {}

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(extract_table_from_pdf, pdf_link) for pdf_link in pdf_links]
    for future in tqdm(as_completed(futures), total=len(futures)):
        dfs, failed = future.result()
        pdf_dfs.extend(dfs)
        failed_pdfs.update(failed)

if failed_pdfs:
    print("\nFailed PDFs:")
    for pdf_url, error in failed_pdfs.items():
        print(f"{pdf_url}: {error}")

df_all = pd.concat(pdf_dfs, ignore_index=True)

# Save the final DataFrame
df_all.to_excel("output.xlsx", index=False)
print("\nOutput saved as 'output.xlsx'.")


# %% ③-5 案 : Multi PDF Extractor 
import pandas as pd
import requests
from io import BytesIO
import tabula
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import tempfile
import subprocess
import fitz  # PyMuPDF

data = pd.read_excel("s_and_p_500_data_IA.xlsx")  # IA & Category
pdf_links = data['PDF Link']

def extract_table_with_pymupdf(pdf_data):
    try:
        doc = fitz.open("pdf", pdf_data)
        page = doc.load_page(0)
        tables = page.get_tables()
        dfs = [pd.DataFrame(table[1:], columns=table[0]) for table in tables]
    except Exception as e:
        print(f"Error while extracting tables with PyMuPDF: {e}")
        dfs = [pd.DataFrame()]
    return dfs

def extract_table_from_pdf(pdf_url):
    failed_pdfs = {}
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error while downloading PDF: {pdf_url}")
        print(e)
        failed_pdfs[pdf_url] = "download_error"
        return pd.DataFrame(), failed_pdfs

    with BytesIO(response.content) as pdf_data:
        try:
            dfs = tabula.read_pdf(pdf_data, pages="all", multiple_tables=True, stream=False, lattice=True)
        except subprocess.CalledProcessError as e:
            print(f"Error while extracting tables from PDF: {pdf_url}")
            print("File format not supported")
            failed_pdfs[pdf_url] = "unsupported_format"
            dfs = extract_table_with_pymupdf(response.content)
        except Exception as e:
            print(f"Error while extracting tables from PDF: {pdf_url}")
            print(e)
            failed_pdfs[pdf_url] = "extraction_error"
            dfs = extract_table_with_pymupdf(response.content)

    return dfs, failed_pdfs

def process_table(df, pdf_url):
    df['PDF Link'] = pdf_url
    return df

def process_pdfs(pdf_links):
    final_dfs = []
    failed_pdfs = {}

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(extract_table_from_pdf, pdf_url): pdf_url for pdf_url in pdf_links}

        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing PDFs"):
            pdf_url = futures[future]
            try:
                tables, errors = future.result()
                for table in tables:
                    processed_table = process_table(table, pdf_url)
                    final_dfs.append(processed_table)
                failed_pdfs.update(errors)
            except Exception as e:
                print(f"Error occurred while processing PDF: {pdf_url}")
                print(e)

    return final_dfs, failed_pdfs

if __name__ == "__main__":
    final_dfs, failed_pdfs = process_pdfs(pdf_links)
    final_df = pd.concat(final_dfs, axis=0, ignore_index=True)

    print("Failed PDFs:")
    for pdf, error_type in failed_pdfs.items():
        print(f"PDF: {pdf}, Error Type: {error_type}")

    print("Final DataFrame:")
    print(final_df)
    final_df.to_excel("s_and_p_500_data_PDFtable.xlsx", index=False)  # Index Added

# %% ④ Refactoring
# %% ④-0 Export
import pandas as pd
data = pd.read_excel("s_and_p_500_data_IA.xlsx")
final_df = pd.read_excel("s_and_p_500_data_PDFtable.xlsx")

merged_df = pd.merge(final_df, data, on='PDF Link', how='inner')
merged_df.to_excel("s_and_p_500_data_merged.xlsx", index=False)  # Index Added
# %% ④-1 import
merged_df = pd.read_excel("s_and_p_500_data_merged.xlsx")
merged_df_col = merged_df.columns
# %% ④-2 Extracting 1案
import re
def extract_related_words(text):
    words_to_extract = ['add', 'adds', 'drop', 'drops', 'added', 'dropped', 'ticker', 'company', 'action', 'effective_date', 'index_name']
    extracted_words = []
    
    for word in words_to_extract:
        pattern = re.compile(r'\b{}\b'.format(word), re.IGNORECASE)
        matches = pattern.findall(text)
        
        if matches:
            extracted_words.extend(matches)

    return extracted_words

texts_list = merged_df_col.astype(str).tolist()
texts = ",".join(texts_list)
extracted_words = extract_related_words(texts)
print(extracted_words)

# %% ④-2 Extracting 2案
import re
import difflib

def extract_related_words(text, words_to_extract):
    extracted_words = []
    
    for word in words_to_extract:
        pattern = re.compile(r'\b{}\b'.format(word), re.IGNORECASE)
        matches = pattern.findall(text)
        
        if matches:
            extracted_words.extend(matches)

    return extracted_words

# 원래 단어 목록
words_to_extract = ['add', 'adds', 'drop', 'drops', 'added', 'dropped', 'ticker', 'company', 'action', 'effective_date', 'index_name']


# 유사한 단어를 원래 단어 목록에 추가

texts_list = merged_df_col.astype(str).tolist()

similar_words = []
for word in words_to_extract:
    similar_words.extend(difflib.get_close_matches(word, texts_list, n=5, cutoff=0.6))

words_to_extract.extend(similar_words)

texts = ",".join(texts_list)
extracted_words = set(extract_related_words(texts, words_to_extract))
print(extracted_words)

# %% Only wanted columns 
filtered_df = merged_df.dropna(subset=['Propose', 'GROUP', 'drop', 'election', 'icke', \
                                       'Index name.1', 'ndex Nam', 'ADD', 'INDEX NAME', 'ompany Nam\
                                           ', 'Index Name', 'Effective Date', 'ction', 'Drops', 'Drop', 'Company Nam', 'Ticker.1', 'ADDS', 'Sanctioned', 'DROP', 'ffective', 'Adds', 'Index name', 'group', 'Ticker', 'DROPS', 'Index Name.1', 'Effective Date.1', 'Effective Dat', 'Added', 'Effective Dates1', 'effective date', 'Group', 'roposed', 'added', 'ompany', 'proposed', 'ffective Date', 'ndex Name', 'Action', 'ompany Name', 'Company', 'Proposed', 'Ticke', 'alculation', 'icker', 'company', 'action'], how = 'all')

# %% ④ visualization #################################################### 
import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt
import requests

# <1> Data collection
def collect_announcements():
    # Read the provided data
    data = pd.read_excel("s_and_p_500_data.xlsx")
    return data

# <2> Classify titles
def classify_titles(data):
    titles = data['Title']
    data['Category'] = ''

    categories_keywords = {
        'inclusion_exclusion': ['join', 'set to', 'constituent change', 'enter', 'added', 'removed', 'reconstitution', 'treatment'],
        'rebalancing': ['rebalancing', 'rebalance'],
        'price_index': ['case-shiller', 'home price'],
        'methodology_change': ['modification', 'consultation']
    }

    for idx, title in enumerate(titles):
        classified = []

        # Classify titles based on keywords
        for category, keywords in categories_keywords.items():
            for keyword in keywords:
                if keyword.lower() in title.lower():
                    classified.append(category)
                    break

        data.loc[idx, 'Category'] = ', '.join(classified)

    return data

# <3> Create time series data
def create_timeseries_data(data):
    data['Date'] = pd.to_datetime(data['Date'])
    time_series_data = data[['Date', 'Category']]
    time_series_data.set_index('Date', inplace=True)

    # Count category occurrences on each date
    time_series_data = time_series_data.groupby(['Date', 'Category']).size().unstack(fill_value=0)

    # Cumulative sum to get the historical view
    time_series_data = time_series_data.cumsum()

    return time_series_data

# Main function
def main():
    announcements_df = collect_announcements()
    classified_announcements = classify_titles(announcements_df)
    timeseries_data = create_timeseries_data(classified_announcements)

    # Save the time series data to a CSV file
    timeseries_data.to_csv('historical_sp_changes_timeseries.csv')

    # Visualize the time series data
    timeseries_data.plot(figsize=(12, 8))
    plt.xlabel('Date')
    plt.ylabel('Cumulative Changes')
    plt.title('Historical S&P Changes')
    plt.legend(title='Categories', loc='upper left')
    plt.grid()
    plt.savefig('historical_sp_changes_timeseries.png')
    plt.show()

if __name__ == "__main__":
    main()