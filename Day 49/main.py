'''

 ____  ____  _     _____    ____  _     _        _____  _    _____   ____  ____  ____  _________  ____  _
/  _ \/  _ \/ \  //__ __\  /  __\/ \ /\/ \  /|  /__ __\/ \ //  __/  /  __\/  __\/  _ \/  __/  __\/  _ \/ \__/|
| | \|| / \|| |\ || / \    |  \/|| | ||| |\ ||    / \  | |_||  \    |  \/||  \/|| / \|| |  |  \/|| / \|| |\/||
| |_/|| \_/|| | \|| | |    |    /| \_/|| | \||    | |  | | ||  /_   |  __/|    /| \_/|| |_//    /| |-||| |  ||
\____/\____/\_/  \| \_/    \_/\_\\____/\_/  \|    \_/  \_/ \\____\  \_/   \_/\_\\____/\____\_/\_\\_/ \|\_/  \|


'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By

ACCOUNT_EMAIL = "maarcusreniero@gmail.com"
ACCOUNT_PASSWORD = "l_maarcus@170603"
PHONE_NUMBER = "+917299954472"

s = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(2)

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)


time.sleep(5)

job_list = driver.find_elements(By.CSS_SELECTOR, ".job_container--clickable")

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_elements(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_elements(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE_NUMBER)

        submit_button = driver.find_elements(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

