# 장바구니 저장하는 매크로
from selenium.webdriver.common.by import By


def save_course_cart(driver):
    driver.find_element(By.ID, "cb_grd_basket").click()
    driver.find_element(By.ID, "btn_basketSave").click()

    driver.switch_to.alert.accept()  # 팝업 : 수강 성공 or 실패 or 기간 아님
