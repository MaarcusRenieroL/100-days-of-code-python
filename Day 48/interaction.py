from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
total_no_of_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
all_portals = driver.find_element(By.LINK_TEXT, "All portals")
search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)


first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
email = input("Enter your mail id : ")

driver.get("http://secure-retreat-92358.herokuapp.com/")

firstName_fill = driver.find_element(By.NAME, "fName")
lastName_fill = driver.find_element(By.NAME, "lName")
email_fill = driver.find_element(By.NAME, "email")

firstName_fill.send_keys(first_name)
lastName_fill.send_keys(last_name)
email_fill.send_keys(email)

send_button = driver.find_element(By.CSS_SELECTOR, "form button")
send_button.click()
