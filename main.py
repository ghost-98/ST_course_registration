from selenium import webdriver
from selenium.webdriver.common.by import By

import time, sys

from course_registration_macro import register_lectures
from save_course_cart_macro import save_course_cart
from check_my_lecture import check_my_lecture


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


##### 시간문제 같은 문제해결을 !!! : 처음엔 어떻게 시간을 가져오는지 몰랐음(이건 공부), 아는 지식 활용해 문제 해결.
### 기술 : python, selenium
### 기반 : 윈도우, python3.10, selenium라이브러리 환경 작동
### 동작 흐름
### 기획 의도
### 사용 방안
# 1번(1) : 수강페이지 열릴때 선착순
# 1번(2) : 이후 다수의 과목 한페이지에서 저장하고 싶을때 (장바구니에 과목 있는 유저들 대상)
# 2번(1) : 수강페이지 열릴때 선착순 - ?
# 2번(2) : 이후 원하는 과목들 수강 매크로
# 3번 : 현재 내가 수강한 강의들을 요일, 시간별로 정렬해서 확인 가능

### 공부한 부분
# selenium(언어 플랫폼 무관)이라는 브라우저 자동화 도구를 알 수 있게됨 (브라우저 드라이버, html 요소 조작 메서드, html 요소 찾기 메서드, 브라우저 조작 메서드, 키보드 / 마우스 이벤트, js실행)
# 크롬 브라우저의 개발자 도구 보는 방법과 활용
# html, css, js에 대한 약간의 이해와 웹사이트 구조 / 웹사이트의 기술스택
## 느낀점 : 설계의 중요성

### 개선점
# 0. 서버 시간 가져와서 기반한 서비스 (장바구니는 필수) --- 핵심!!!!!!!!!!
# 1. 캡차 우회 or 로그인 이후 화면에서 서비스 가능하게
# 2. 최대한 동작 시간 줄이기 (시스템적으로)
# 3. 다양한 환경의 시스템에서 동작 가능하게 설계 (속도가 느린 환경에서도 동작하게 - time.sleep 사용자제 / 웹이 새로고침되는 것 최대한 자제)
# ++ 새로고침이 길 경우 time.sleep으로는 이후 요청들이 다 씹힌다
# 4. 모바일이나 웹 혹은 데스크톱 앱 플랫폼 개발 + 백그라운드 동작 및 비동기 프로그래밍 : 뒤로가기 기능, 로그인 이후 기능 왔다갔다
# 5. 비밀번호 입력 시 값이 보이는거 보안 개선
# 6. 2번 기능 아무 키나 누르면 프로그램 종료 하는것
# 7. 2번 기능 while 문 중간에 스스로 꺼지는 것
# 8. 예외처리!!!!!
# -> 지금은 웹브라우저 컨트롤하여 빨리 요청보내는건데, 직접 사이트에 신청에 해당하는 http 요청 보내는 것은? (개발자 도구 이용)

### 아쉬운 점
# 1. 프로그래밍 언어에 대한 이해 부족 + 예외처리 부족 / 변수명, 변수선언 위치...
# 2. 로직 설계 능력 부족
# 3. 주먹 구구식 개발, 설계 충분히 하지 않은 것 / 쓰는 라이브러리나 기술에 대한 충분한 공부x
# 4. 사전에 기획과 설계, 쓸 기술 선정등 확실히 준비
# 5. html, css, js 지식 부족

