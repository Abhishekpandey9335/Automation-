from selenium import webdriver
import time
# inisiate Chrome browser
driver = webdriver.Chrome()
# nvigate to google

driver.get("https://google.com")

time.sleep(3)# wait 3 sec.
#navigate to youtube
driver.get("https://www.youtube.com/")
time.sleep(3)# wait 3 sec.
#navigate to a vedio
driver.get("https://www.youtube.com/watch?v=zrLbligLWlU&list=RDzrLbligLWlU&start_radio=1")
# go back to youtube
time.sleep(3)# wait 3 sec.
driver.back()
# fir se dusri vedio open krne ke liye
time.sleep(3)# wait 3 sec.
driver.forward()
time.sleep(3)# wait 3 sec.
driver.refresh()
time.sleep(5)# wait 3 sec.
driver.quit()
