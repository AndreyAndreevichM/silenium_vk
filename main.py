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

    email_input = driver.find_element(By.CLASS_NAME, 'VkIdForm__input')

    # email_input = driver.find_element(By.ID, 'index_email')
    email_input.clear()
    email_input.send_keys('79885001670')
    email_input.send_keys(Keys.ENTER)
    time.sleep(5)

    # // *[ @ id = "root"] / div / div / div / div / div[1] / div[2] / div / div / div / form / div[4] / div / button[2]
    # root > div > div > div > div > div.vkc__AuthRoot__root.vkuiSplitLayout__inner > div.vkc__AuthRoot__col.vkc__AuthRoot__contentCol.vkuiSplitCol > div > div > div > form > div.vkc__AuthSimpleScreen__bottom > div > button.vkc__PureButton__button.vkc__Link__link.vkc__Link__primary.vkc__Bottom__switchToPassword
    # password_input = driver.find_element(By.CLASS_NAME, 'vkc__PureButton__button vkc__Link__link vkc__Link__primary vkc__Bottom__switchToPassword')
    # password_input.clear()
    # password_input.send_keys(Keys.ENTER)

    # pass_btn = driver.find_element(By.CSS_SELECTOR,
    #                                '#root > div > div > div > div > div.vkc__AuthRoot__root.vkuiSplitLayout__inner > div.vkc__AuthRoot__col.vkc__AuthRoot__contentCol.vkuiSplitCol > div > div > div > form > div.vkc__AuthSimpleScreen__bottom > div > button.vkc__PureButton__button.vkc__Link__link.vkc__Link__primary.vkc__Bottom__switchToPassword')
    # pass_btn.click()
    # time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

