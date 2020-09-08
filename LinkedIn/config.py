from selenium import webdriver
import logging
logging.basicConfig(filename='config.log',level=logging.DEBUG)

def driver_config(path_of_driver, path_of_sites):
    try:
        driver = webdriver.Chrome(path_of_driver)
        driver.get(path_of_sites)
        return driver
    except Exception as e:
        logging.error(e)
    