from selenium import webdriver
from selenium.webdriver.common.by import By

import time, sys

from code.course_registration_macro import register_lectures
from save_course_cart_macro import save_course_cart
from code.check_my_lecture import check_my_lecture


print("==================")
print("수강신청 매크로입니다")
print("==================\n\n")

###### 수강신청 사이트 로그인 후 메인 화면 이동 ######

# 수강신청 사이트 로그인 정보 입력
user_id = input("아이디를 입력하세요 : ")
user_pwd = input("비밀번호를 입력하세요: ")

# 크롬 브라우저 실행 (드라이버는 selenium 내장)
driver = webdriver.Chrome()
url = 'https://for-s.seoultech.ac.kr/view/login.jsp'
driver.get(url)  # 웹사이트 열기

# 페이지 로딩, 환경마다 다름
time.sleep(1)

# 로그인
site_id = driver.find_element(By.ID, "USER_ID")
site_pwd = driver.find_element(By.ID, "PWD")

site_id.send_keys(user_id)
site_pwd.send_keys(user_pwd)

driver.find_element(By.ID, "btn_Login").click()

# CAPTCHA
CAPTCHA_num = input("CAPTCHA 숫자를 입력하세요: ")
driver.find_element(By.ID, "CAPTCHA").send_keys(CAPTCHA_num)

driver.find_element(By.CLASS_NAME, "btn-layerClose").click()
time.sleep(0.5)

# 수강신청 페이지 모달(팝업) x클릭
driver.find_element(By.CSS_SELECTOR, "button.ui-dialog-titlebar-close").click()

# 수강신청 페이지로 이동
driver.find_element(By.CSS_SELECTOR, "a[data-lang='common_sugang']").click()


###### 원하는 기능 선택 1~3 ######
print("=======================")
# 수강신청의 기능 탭
search_tab = driver.find_element(By.ID, "lst_TabMenu")
func_choice = int(input("1 : 장바구니 저장\n"
                        "2 : 여러 과목 수강 신청\n"
                        "3 : 내 시간표 확인\n"
                        "--------------------------\n"
                        "원하는 기능을 선택해주세요 : "))

# 원하는 기능 선택 (match-case : python 3.10이상 지원)
match func_choice:
    case 1:  # 장바구니 저장
        # search_tab.find_element(By.CSS_SELECTOR, 'div[data-lang="tab_basket"]').click()
        save_course_cart(driver)

    case 2:  # 여러 과목 수강 신청
        search_tab.find_element(By.CSS_SELECTOR, 'div[data-lang="tab_dayLess"]').click()
        driver.switch_to.alert.accept()  # 팝업 제거
        register_lectures(driver)

    case 3:  # 내 강의 요일, 시간별 확인
        search_tab.find_element(By.CSS_SELECTOR, 'div[data-lang="tab_dayLess"]').click()
        driver.switch_to.alert.accept()  # 팝업 제거
        check_my_lecture(driver)

time.sleep(1)
print("프로그램 종료")
# 브라우저 닫기
driver.quit()
# 프로그램 종료
sys.exit(0)  # 정상 종료 (0: 성공)



