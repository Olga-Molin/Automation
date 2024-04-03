# зайти на лабиринт
# найти книги по слову Python
# собрать все карточки товаров
# вывести в консоль инфор: название + автор + цена


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# зайти на лабиринт
driver.get("https://www.labirint.ru")

# найти книги по слову Python
search_field = "#search-field"
serch_input = driver.find_element(By.CSS_SELECTOR, search_field)
serch_input.send_keys("Python")
serch_input.send_keys(Keys.RETURN)

# собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

print(len(books))

# вывести в консоль инфор: название + автор + цена

for book in books:
       print(book.text)

sleep(50)