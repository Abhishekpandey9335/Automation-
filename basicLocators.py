from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# inisiate Chrome browser
driver = webdriver.Chrome()
# nvigate to google

driver.get("https://google.com")

time.sleep(2)# wait 3 sec.

# navigate saucedemp website
driver.get("https://www.saucedemo.com/")
time.sleep(2)
#locate username
username = driver.find_element(By.ID,"user-name")
# locate Password
password=driver.find_element(By.ID,"password")
# enter username
username.send_keys("standard_user")
time.sleep(2)
#enter passwoerd
password.send_keys("secret_sauce")
time.sleep(2)
driver.quit()

