

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig(filename='automation.log', level=logging.DEBUG)



def comment(driver):
    driver.find_elements_by_xpath('//button[@data-control-name="comment"]').click()
    return True