from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


try:
    # Open the first page
    driver.get("https://books.toscrape.com/")

    # Save the current tab
    original_tab = driver.current_window_handle

    print("First page:", driver.title)

    # Open a new tab
    driver.switch_to.new_window("tab")

    # Navigate to another page
    driver.get("https://www.example.com/")

    print("Second page:", driver.title)

    # Show all open tabs
    print("Open tabs:", len(driver.window_handles))

    # Close the second tab
    driver.close()

    # Return to the original tab
    driver.switch_to.window(original_tab)

    wait.until(EC.title_contains("Books"))

    print("Back to:", driver.title)

finally:
    driver.quit