from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #Chrome이 자동으로 꺼지는 것을 막음
browser = webdriver.Chrome(options= options)
browser.get("https://naver.com") #해당 사이트를 시작으로 브라우저 실행
browser.find_element(By.ID,"query").send_keys("검색어") # 검색창 선택후, 검색 key 입력
browser.find_element(By.ID,"search-btn").click()  #검색 버튼 클릭
