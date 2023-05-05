# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver
# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import requests

KAKAO_TOKEN = "rHEYhdwL2SSutxlW7zoExxa6aOa0koOKLK4b9nVlCj10EQAAAYfsnzl9"

def send_to_kakao():
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    header = {'Authorization': 'Bearer ' + KAKAO_TOKEN}
    post = {
        "object_type": "text",
        "text": "https://ticket.11st.co.kr/Product/Detail?id=267448&prdNo=5626407961",
        "link": {
            "web_url": "https://ticket.11st.co.kr/Product/Detail?id=267448&prdNo=5626407961",
            "mobile_web_url": "https://ticket.m.11st.co.kr/Product/Detail?id=267448&prdNo=5626407961"
        },
        "button_title": "바로 가기"
    }
    data = {"template_object": json.dumps(post)}
    return requests.post(url, headers=header, data=data)

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
    if (content.text != "2023. 05. 20 (토) 19:00 - 매진"):
        send_to_kakao()
    time.sleep(30)