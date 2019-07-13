from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
# from openpyxl import Workbook
import openpyxl as excel


def readContacts(fileName):
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']
    for cell in range(len(firstCol)):
        contact = str(firstCol[cell].value)
        contact = "\"" + contact + "\""
        lst.append(contact)
    return lst

targets = readContacts("contacts.xlsx")
print(targets)
browser = int(input("Enter 1 for Chrome or 2 for FireFox and press enter:"))
driver = None
#for chrome
if browser == 1:
    driver = webdriver.Chrome('/home/chandan/Desktop/chromedriver')
elif browser ==2:
    driver = webdriver.Firefox(executable_path="./geckodriver")

#link to open a site
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 10)
wait5 = WebDriverWait(driver, 5)
input("Scan the QR Code and press enter:")
count = 0
success = 0
sNo = 1
failList = []
# Iterate over selected contacts
for target in targets:
            print(sNo, ". Target is: " + target)
            sNo+=1
            try:
                # Select the target
                x_arg = '//span[contains(@title,' + target + ')]'
                try:
                    wait5.until(EC.presence_of_element_located((
                        By.XPATH, x_arg
                    )))
                except:
                    # If contact not found, then search for it
                    searBoxPath = '//*[@class="jN-F5"]'
                    wait5.until(EC.presence_of_element_located((
                        By.CLASS_NAME, "jN-F5"
                    )))
                    inputSearchBox = driver.find_element_by_class_name("jN-F5")
                    time.sleep(0.5)

                    # click the search button
                    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div/button').click()
                    time.sleep(1)
                    inputSearchBox.clear()
                    inputSearchBox.send_keys(target[1:len(target) - 1])
                    print('Target Searched')
                    # Increase the time if searching a contact is taking a long time
                    time.sleep(4)

                # Select the target
                driver.find_element_by_xpath(x_arg).click()
                print("Target Successfully Selected")
                time.sleep(2)

                # Select the Input Box
                inp_xpath = "//div[@contenteditable='true']"
                input_box = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath)))
                time.sleep(1)

                # Send message
                # taeget is your target Name and msgToSend is you message
                input_box.send_keys("Hello, " + target + "."+ Keys.SHIFT + Keys.ENTER + msgToSend[count][3] + Keys.SPACE) # + Keys.ENTER (Uncomment it if your msg doesnt contain '\n')
                # Link Preview Time, Reduce this time, if internet connection is Good
                time.sleep(2)
                input_box.send_keys(Keys.ENTER)
                print("Successfully Send Message to : "+ target + '\n')
                success+=1
                time.sleep(0.5)

            except:
                # If target Not found Add it to the failed List
                print("Cannot find Target: " + target)
                failList.append(target)
                pass

print("\nSuccessfully Sent to: ", success)
print("Failed to Sent to: ", len(failList))
print(failList)
print('\n\n')
count+=1
driver.quit()
driver.close()

