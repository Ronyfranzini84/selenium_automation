
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from pathlib import Path
import logging
from scraper import navigate_page, save_excel

# Create the logs folder
logs_folder = Path(__file__).resolve().parent / "logs"
logs_folder.mkdir(parents=True, exist_ok=True)

# Configure Logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Define the message format
formatter =  logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

# Save logs to a file
file_handler = logging.FileHandler(logs_folder / "selenium.log",
                encoding="utf-8")

file_handler.setFormatter(formatter)

# Show logs in the terminal
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Configure logger outputs
logger.handlers.clear()
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logging.info("Starting Selenium automation")

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

logging.info(
    f"Extraction completed | Total books: {len(df_products)}"
)

print(df_products.head(20))