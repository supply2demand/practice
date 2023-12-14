from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd
import openpyxl

# Excel 파일을 불러 리스트로 변환
filename = '원하는 엑셀 이름.xlsx' # 파이썬 파일과 같은 폴더에 엑셀을 넣고 작업해주세요
cstmr = pd.read_excel(filename,sheet_name= 0)
cst_bsno = cstmr.iloc[2:,6].dropna() # excel 내에서 시작할 사업자 번호
bsno = cst_bsno.tolist()
cst_cmp = cstmr.iloc[2:,5].dropna()# excel 내에서 시작할 상호명
company = cst_cmp.tolist()

#driver 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument("--start-fullscreen")
options.add_argument("--headless")
#options.add_argument('--disable-gpu')
options.add_experimental_option("detach", True)
options.page_load_strategy = 'normal'
options.add_argument(r"--user-data-dir=C:\\Users\\AppData\\Local\\Google\\Chrome\\User Data")#로컬 크롬 프로필사용
options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(options= options)

# 홈택스 페이지로 시작
driver.get("https://www.hometax.go.kr/websquare/websquare.html?w2xPath=/ui/pp/index_pp.xml") 


#홈택스 ID와 비밀번호 로그인
driver.find_element(By.XPATH,"//*[@id='textbox915']").click()
time.sleep(3)
iframe = driver.find_element(By.CSS_SELECTOR, "#txppIframe") # 페이지 안의 페이지 iframe 찾아서 선택
driver.switch_to.frame(iframe)
driver.find_element(By.CSS_SELECTOR,"#anchor15").click()
driver.find_element(By.CSS_SELECTOR,"#iptUserId").send_keys('ID 입력칸') # ID
driver.find_element(By.CSS_SELECTOR,"#iptUserPw").send_keys('비밀번호 입력칸') #비밀번호
driver.find_element(By.CSS_SELECTOR,"#anchor25").click()
time.sleep(5)


# 공인인증서 화면 선택후, 비밀번호 입력
iframe = driver.find_element(By.CSS_SELECTOR, '#dscert')
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, '//*[@id="row0dataTable"]/td[1]/a/span').click() # 인증서 선택
password = '공인인증서 비밀번호 입력칸' #인증서와 비밀번호 
driver.find_element(By.ID, 'input_cert_pw').send_keys(password)
driver.find_element(By.ID, 'btn_confirm_iframe').click()
driver.implicitly_wait(3)
#로그인 완료


#홈페이지에서 메뉴 선택 func
def MainTo(dst):    #css 값을 dst에 넣으면 해당 메뉴로 선택
    time.sleep(5)
    driver.switch_to.default_content()  #메인 프레임 다시 선택
    driver.find_element(By.CSS_SELECTOR, '#hdTxt548').click()
    time.sleep(3)
    iframe = driver.find_element(By.CSS_SELECTOR, "#txppIframe") # 페이지 안의 페이지 iframe 찾아서 선택
    driver.switch_to.frame(iframe)
    driver.find_element(By.CSS_SELECTOR, dst).click() 



# 부가가치세 신고자료 통합조회 func
def 부가가치세():
    MainTo('#span_a_4801060000')
    driver.implicitly_wait(2)
    D = lambda x : driver.execute_script('return document.body.parentNode.scroll'+x) #자바스크립트 명령을 통해 화면 크기 조절
    driver.set_window_size(D('Width'), D('Height'))
    time.sleep(5)
    iframe = driver.find_element(By.CSS_SELECTOR, "#txppIframe") # 페이지 안의 페이지 iframe 찾아서 선택
    driver.switch_to.frame(iframe)
    for i in range(len(bsno)):       
        time.sleep(5)
        driver.find_element(By.ID, "inputBsno").send_keys(bsno[i])
        driver.find_element(By.CSS_SELECTOR, "#trigger113").click()
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   '연구중')

            alert = driver.switch_to.alert
            alert.accept()
            print( f'{company[i]}'+' 면세사업자 확인 필요')
        except:
            print("except 출력")      
        time.sleep(5)
        driver.save_screenshot(' 부가가치세 통합 '+f'{company[i]}'+'.png')
        driver.find_element(By.ID, "inputBsno").clear()
        

 

부가가치세()
print("작업 성공적으로 마침")
driver.close()

