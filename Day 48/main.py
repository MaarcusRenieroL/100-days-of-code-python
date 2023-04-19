from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.python.org/")
search_box = driver.find_element(By.NAME, "q")
print(search_box)
print(driver.find_element(By.CLASS_NAME, "python-logo").size)
link=driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a')
print(link.text)

driver.quit()
