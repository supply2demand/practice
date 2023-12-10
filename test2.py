from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options= options)
browser.get("https://naver.com")
browser.find_element(By.ID,"query").send_keys("도재승")
browser.find_element(By.ID,"search-btn").click()