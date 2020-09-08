import login
import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import json
logging.basicConfig(filename='automation.log', level=logging.DEBUG)

driver = config.driver_config("./chromedriver", "https://www.linkedin.com/")
login.login("your phone number", "your pasword of linkedin", driver)
block_xpath = "//div[@id='ember57']"
posts_xpath = "//div[@class='feed-shared-update-v2 feed-shared-update-v2--minimal-padding full-height relative artdeco-card ember-view']"
post_block =driver
driver.implicitly_wait(30)
try:
    post_block = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, posts_xpath))
    )
except Exception as e:
    print(e)

all_post_cards = post_block.find_elements_by_xpath(
    '//div[@class="occludable-update ember-view"]')
print("Total posts", len(all_post_cards))
data = []
for post in all_post_cards:
    data.append(post.text)

if data:
    print("total data", len(data))
    with open("post.json", 'w') as file:
        json.dump(data, file, indent=4)
driver.close()
