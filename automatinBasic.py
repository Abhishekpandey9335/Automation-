from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def google_search_example():
    # 1. Create a browser instance (Chrome here; make sure chromedriver is installed)
    driver = webdriver.Chrome()   # or webdriver.Firefox()

    try:
        # 2. Open a website
        driver.get("https://www.google.com")

        # 3. Find the search box (by name='q') and type a query
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("selenium python tutorial")
        search_box.send_keys(Keys.RETURN)

        # 4. Wait until results are loaded and get result titles
        wait = WebDriverWait(driver, 10)
        results = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3"))
        )

        # 5. Print text of first few results
        for i, r in enumerate(results[:5], start=1):
            print(f"{i}. {r.text}")

    finally:
        # 6. Close the browser
        driver.quit()

if __name__ == "__main__":
    google_search_example()
