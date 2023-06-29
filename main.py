import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service(executable_path="D:/all project/pythonProject/silenium/chromedriver.exe")
driver = webdriver.Chrome(service=s)

try:
    driver.maximize_window()
    driver.get('https://vk.com')
    time.sleep(5)

    email_input = driver.find_element(By.ID, 'index_email')
    email_input.clear()
    email_input.send_keys('79885001670')
    email_input.send_keys(Keys.ENTER)
    time.sleep(5)

    pass_btn = driver.find_element_by_css_selector('vkc__PureButton__button vkc__Link__link vkc__Link__primary vkc__Bottom__switchToPassword')
    pass_btn.click()
    # password_input = driver.find_element(By.CLASS_NAME, 'vkc__PureButton__button vkc__Link__link vkc__Link__primary vkc__Bottom__switchToPassword')
    # password_input.clear()
    # password_input.send_keys(Keys.ENTER)
    time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

