from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

page_number = 1
total_books = 0

products_data = []

try:

    driver.get("https://books.toscrape.com/")

    while True:
        books = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//article[@class='product_pod']")
            )
        )

        total_books += len(books)
        print(
            f"Page {page_number}: "
            f"{len(books)} books | "
            f"Total: {total_books}"
        )

        next_buttons = driver.find_elements(By.XPATH, "//li[@class='next']/a")

        if not next_buttons:
            break

        current_page = driver.current_url

        next_buttons[0].click()

        wait.until(EC.url_changes(current_page))

        page_number += 1

    print("\nExtraction completed!")
    print("Pages visited:", page_number)
    print("Total books:", total_books)
    # print("First page:", driver.current_url)

    # next_button = driver.find_element(By.XPATH, "//li[@class='next']/a")

    # next_button.click()

    # print("Second page:", driver.current_url)

    # books = driver.find_elements(By.XPATH, "//article[@class='product_pod']")

    # print("Books found:", len(books))

    input("Press Enter to close the browser...")

    # for book in books:
    #     book_name = book.find_element(By.XPATH,".//h3/a").get_attribute("title")

    #     price_text = book.find_element(By.XPATH, ".//p[@class='price_color']").text

    #     book_price = float(price_text.replace("£", ""))

    #     availability = book.find_element(By.XPATH,".//p[contains(@class, 'availability')]").text.strip()

    #     rating_text = book.find_element(By.XPATH, ".//p[contains(@class, 'star-rating')]").get_attribute('class')
    #     rating_word = rating_text.split()[-1]
    #     book_rating = rating_map[rating_word]

    #     products_data.append({
    #         "name": book_name,
    #         "price": book_price,
    #         "avalability": availability,
    #         "rating": book_rating
    #     })

finally:
    driver.quit()

# df_products = pd.DataFrame(products_data)

# print(df_products)

# print("Total products:", len(df_products))
# print("\nColumn types:")
# print(df_products.dtypes)

