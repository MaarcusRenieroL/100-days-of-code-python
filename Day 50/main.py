from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

s = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://tinder.onelink.me/9K8a/3d4abb81")
driver.maximize_window()

login_google = driver.find_element(By.LINK_TEXT, 'Log in with Google')
login_google.click()


