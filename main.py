# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver
# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys
# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
from webdriver_manager.chrome import ChromeDriverManager
import datetime

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://ticket.11st.co.kr/Product/Detail?id=267448&prdNo=5626407961")

while True:
    driver.refresh()
    # 페이지가 완전히 로딩되도록 3초동안 기다림
    time.sleep(3)
    
    # 20일 클릭
    driver.find_element_by_css_selector("#divCalendar1 > table > tbody > tr:nth-child(3) > td:nth-child(7)").click()
    
    # 예약 현황
    content = driver.find_element_by_css_selector("#tabpanelBuy1 > div > div.c_ticket_timetable > ul > li > label > span")
    
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M")
    print(f'{current_time}: {content.text}')
    time.sleep(30)