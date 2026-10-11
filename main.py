
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from pathlib import Path
from scraper import navigate_page, save_excel

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:

    driver.get("https://books.toscrape.com/")

    products_data = navigate_page(driver, wait)
    
finally:
    driver.quit()

df_products = pd.DataFrame(products_data)

save_excel(
    dataframe=df_products,
    folder_path=Path.home() / "Downloads" / "books_selenium",
    file_name="books_selenium.xlsx"
)

print(df_products.head(20))