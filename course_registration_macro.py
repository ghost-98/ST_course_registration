########## 여러 과목 수강 신청 ##########

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
import subprocess  # cmd 띄우기


# 요일별 강의 조회에서 강의 찾는 함수 (반복문 안에서 동작하는 함수 : 반복자 i를 매개변수)
def search_lecture(driver, Lectures, i):
    department_dropdown = Select(driver.find_element(By.ID, "cbo_dayLessLess"))
    # 사용자의 입력을 포함하는 단어 선택
    for department in department_dropdown.options:
        if Lectures[i][0] in department.text:  # 사용자 입력이 포함된 단과대 검색
            department.click()
            break

    day_dropdown = Select(driver.find_element(By.ID, "cbo_dayLessDays"))
    # 사용자의 입력을 포함하는 단어 선택
    for day in day_dropdown.options:
        if Lectures[i][1] in day.text:
            day.click()
            break

    driver.find_element(By.ID, "edt_dayLessSubjKnm").send_keys(Lectures[i][2])
    driver.find_element(By.ID, "btn_dayLessSearch").click()


def register_lectures(driver):
    # 현재 수강 중인 강의 수
    lecture_table = driver.find_element(By.ID, "grd_SugangMain")
    origin_lecture_count = len(lecture_table.find_elements(By.CLASS_NAME, "ui-widget-content.ui-row-ltr"))

    # 자동 수강 신청 원하는 과목들 정보 입력
    num = int(input("수강신청할 과목 개수를 입력하세요 : "))
    Lectures = []

    print("\n")
    for i in range(num):  # 강의의 단과대, 요일, 과목명을 입력받아서 리스트에 추가
        print("===========================================")
        lecture = [input(f"({i + 1}번째 과목) 단과대를 입력하세요 : "),
                   input(f"({i + 1}번째 과목) 요일을 입력하세요 : "),
                   input(f"({i + 1}번째 과목) 과목명을 입력하세요 : ")]
        Lectures.append(lecture)

    # 강의 검색 결과 출력 및 강의 시간대 입력 받기
    for i in range(len(Lectures)):
        # 과목 검색 함수
        search_lecture(driver, Lectures, i)

        # 강의 검색 결과 추출
        searched_rows = driver.find_element(By.ID, "grd_dayLess").find_elements(By.CLASS_NAME, "ui-widget-content.jqgrow.ui-row-ltr")
        lecture_search_list = []

        # 강의명 검색값 삭제
        driver.find_element(By.ID, "edt_dayLessSubjKnm").clear()

        for row in searched_rows:
            try:
                lecture_code = row.find_element(By.CSS_SELECTOR, '[aria-describedby="grd_dayLess_SUBJ_CD"]').text
                lecture_name = row.find_element(By.CSS_SELECTOR, '[aria-describedby="grd_dayLess_SUBJ_KNM"]').text
                professor = row.find_element(By.CSS_SELECTOR, '[aria-describedby="grd_dayLess_PROF_NM"]').text
                lecture_time = row.find_element(By.CSS_SELECTOR, '[aria-describedby="grd_dayLess_DOTW_TM"]').text
                lecture_number = row.find_element(By.CSS_SELECTOR, '[aria-describedby="grd_dayLess_LECT_NUMB"]').text

                lecture_search_list.append({
                    "강의 번호": lecture_number,
                    "과목 코드": lecture_code,
                    "과목명": lecture_name,
                    "교수": professor,
                    "강의 시간": lecture_time
                })
            except Exception as e:
                print(f"데이터 추출 중 오류 발생: {e}")

        # 강의 목록 정렬해서 출력
        print("\n=== 강의 목록 ===")
        for idx, lec in enumerate(lecture_search_list):
            print(f"{idx+1}번 : [강의 번호: {lec['강의 번호']}] [강의명: {lec['과목명']}] [교수명: {lec['교수']}] [강의 시간: {lec['강의 시간']}]")

        # 번호 선택 받고 저장 버튼 누르기
        lecture_choice = int(input("수강할 강의 번호를 입력하세요 : "))
        Lectures[i].append(lecture_choice)

        time.sleep(0.5)

    print("\n=========================================")
    print("수강을 원하는 강의들 정보 입력이 완료 되었습니다.")
    print("=========================================\n")
    time.sleep(3)
    print("===========================")
    print("수강신청 매크로를 시작하겠습니다.")
    print("===========================\n")
    time.sleep(3)

    # 특정 버튼 누르면 프로그램 종료되게
    print("프로그램을 종료 하고 싶으면 아무 키나 눌러주세요...")

    # 수강 신청 클릭 매크로
    while(len(Lectures)):  # 모두 성공 시 종료
        for i in range(len(Lectures)):
            # 과목 검색 함수
            search_lecture(driver, Lectures, i)

            # 저장(수강 신청) 버튼 클릭
            subject_table = driver.find_element(By.ID, "grd_dayLess")
            save_button = subject_table.find_element(By.ID, f"{Lectures[i][3]}").find_element(By.CSS_SELECTOR, '[value="저장"]')
            save_button.click()
            # 중복 팝업 뜰거나 / 교과목 저장되거나
            driver.switch_to.alert.accept()
            # 과목명 검색값 삭제
            driver.find_element(By.ID, "edt_dayLessSubjKnm").clear()

            time.sleep(2)

            ## 수강 성공시 처리 및 새로운 터미널 열어서 알림
            my_lecture_table = driver.find_element(By.ID, "grd_SugangMain")
            current_lecture_count = len(my_lecture_table.find_elements(By.CLASS_NAME, "ui-widget-content.ui-row-ltr"))

            if (origin_lecture_count != current_lecture_count):
                origin_lecture_count = current_lecture_count
                subprocess.run(f'start cmd /k echo {Lectures[i][2]} 수강신청을 성공했습니다!!!', shell=True)
                del Lectures[i]

            left_subjects = [x[2] for x in Lectures ]
            print(f"남은 과목 : {len(Lectures)}개 / {left_subjects}")


            # 키보드 입력으로 종료
            # 클릭이 너무 빨라서 팝업 열리고 닫는 속도보다 빠름, 그래서 잘못된 인덱싱으로 오류나서 종료될 떄가 있음
            # 검색어 입력시 유도리 있게