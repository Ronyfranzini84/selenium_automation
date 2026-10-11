from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path


rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def extract_products(driver):
    products_data = []

    books = driver.find_elements(
        By.XPATH,
        "//article[@class='product_pod']"
    )

    for book in books:
        book_name = book.find_element(By.XPATH,".//h3/a").get_attribute("title")

        price_text = book.find_element(By.XPATH, ".//p[@class='price_color']").text

        book_price = float(price_text.replace("£", ""))

        availability = book.find_element(By.XPATH,".//p[contains(@class, 'availability')]").text.strip()

        rating_text = book.find_element(By.XPATH, ".//p[contains(@class, 'star-rating')]").get_attribute('class')
        rating_word = rating_text.split()[-1]
        book_rating = rating_map[rating_word]
        
        products_data.append({
            "name": book_name,
            "price": book_price,
            "availability": availability,
            "rating": book_rating
        })
    return products_data

def navigate_page(driver, wait):
    all_products = []
    page_number = 1

    while True:
        books = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//article[@class='product_pod']")
            )
        )

        page_products = extract_products(driver)

        all_products.extend(page_products)
        

        print(
            f"Page {page_number} completed | "
            f"Total books: {len(all_products)}"
        )

        next_buttons = driver.find_elements(By.XPATH, "//li[@class='next']/a")
        
        if not next_buttons:
            break

        current_page = driver.current_url

        next_buttons[0].click()

        wait.until(EC.url_changes(current_page))

        page_number += 1
        
    return all_products

def save_excel(dataframe, folder_path, file_name):
    folder = Path(folder_path).expanduser()
    folder.mkdir(parents=True, exist_ok=True)

    file_path = folder / file_name
    dataframe.to_excel(file_path, index=False)
    print(f"Excel saved at: {file_path}")

    return file_path