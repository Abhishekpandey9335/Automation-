#import webDriver module from selenium Package
from selenium import webdriver

# instant webdriver and launch Chrome browser
driver = webdriver.Chrome()

# open google.com on web page
driver.get("https://www.google.com")
# close the browser window
driver.quit()