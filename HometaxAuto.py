from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options= options)
browser.get("https://www.hometax.go.kr/websquare/websquare.html?w2xPath=/ui/pp/index_pp.xml")
time.sleep(5)
browser.find_element(By.CLASS_NAME,"w2textbox").click()
