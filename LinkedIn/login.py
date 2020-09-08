from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig(filename='login.log',level=logging.DEBUG)

def login(username, password, driver, username_xpath = '//*[@id="session_key"]', password_xpath = '//*[@id="session_password"]', submit_btn_xpath = '/html/body/main/section[1]/div[2]/form/button', wait_seconds = 2):
    """
    username = mobile number or email id
    """
    try:
        WebDriverWait(driver, wait_seconds).until(
            EC.presence_of_element_located((By.XPATH, username_xpath))
            ).send_keys(username) 
        WebDriverWait(driver, wait_seconds).until(
            EC.presence_of_element_located((By.XPATH, password_xpath))
            ).send_keys(password)
        WebDriverWait(driver, wait_seconds).until(
            EC.presence_of_element_located((By.XPATH, submit_btn_xpath))
            ).click()
        return True
    except Exception as e:
        logging.error(e)
        return False