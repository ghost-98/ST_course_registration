########## 내 강의 시간표 확인 함수 ##########

from selenium.webdriver.common.by import By


def check_my_lecture(driver):
    # 요일-숫자 매핑 딕셔너리
    day_dict = {"월": 0, "화": 1, "수": 2, "목": 3, "금": 4, "토": 5, "일": 6}

    # 내 강의 정보 수집
    lecture_row = driver.find_element(By.ID, "grd_SugangMain").find_elements(By.CLASS_NAME, "ui-widget-content.jqgrow.ui-row-ltr")
    lecture_list = []

    for row in lecture_row:
        try:
            lecture_name = row.find_element(By.CSS_SELECTOR, '[aria-describedby="grd_SugangMain_SUBJ_KNM"]').text
            # professor = row.find_element(By.CSS_SELECTOR, '[aria-describedby="grd_SugangMain_PROF_NM"]').text
            lecture_time = row.find_element(By.CSS_SELECTOR, '[aria-describedby="grd_SugangMain_DOTW_TM"]').text

            day = lecture_time[0]
            start_time = lecture_time[2]

            lecture_list.append([day, start_time, f"{lecture_name}({lecture_time})"])
        except Exception as e:
            print(f"데이터 추출 중 오류 발생: {e}")

    # 내 강의 요일, 시간에 맞게 정렬 ?
    sorted_lecture_list = sorted(lecture_list, key=lambda x: (day_dict[x[0]], x[1]))
    sorted_lecture_dict = {"월": [], "화": [], "수": [], "목": [], "금": []}

    for lecture in sorted_lecture_list:
        sorted_lecture_dict[lecture[0]].append(lecture[2])

    # 내 강의 시간표 출력
    print("===================================")
    for day, lectures in sorted_lecture_dict.items():
        print(f"{day}: {lectures}")
    print("===================================")