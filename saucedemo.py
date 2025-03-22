from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

title = driver.title

driver.implicitly_wait(0.5)

# Login
username = driver.find_element(by=By.ID, value="user-name").send_keys("standard_user")
password = driver.find_element(by=By.ID, value="password").send_keys("secret_sauce")
time.sleep(1)
submit_button = driver.find_element(by=By.ID, value="login-button").click()
time.sleep(1)

# Membuka detail produk
backpack = driver.find_element(by=By.CSS_SELECTOR, value="#item_4_title_link > div").click()
time.sleep(1)

# Menambahkan produk ke cart
addcart = driver.find_element(by=By.ID, value="add-to-cart").click()
time.sleep(1)

# Menghapus dari cart
removeproduct = driver.find_element(by=By.ID, value="remove").click()
addcart = driver.find_element(by=By.ID, value="add-to-cart").click()
time.sleep(1)

# Membuka cart
cart = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_link").click()
time.sleep(1)

# Masuk halaman checkout
checkout = driver.find_element(by=By.ID, value="checkout").click()
time.sleep(1)

# Input informasi checkout
firstname = driver.find_element(by=By.ID, value="first-name").send_keys("Ryan")
lastname = driver.find_element(by=By.ID, value="last-name").send_keys("Ramadhani")
zip = driver.find_element(by=By.ID, value="postal-code").send_keys(12345)
time.sleep(1)
continue_button = driver.find_element(by=By.ID, value="continue").click()
time.sleep(1)
finish_button = driver.find_element(by=By.ID, value="finish").click()
time.sleep(1)
back_home_button = driver.find_element(by=By.ID, value="back-to-products").click()
time.sleep(1)

# Filter
filter = Select(driver.find_element(by=By.CLASS_NAME, value="product_sort_container"))
time.sleep(1)
filter.select_by_value("lohi")

# Add to cart from list product
addcart_bike = driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-bike-light").click()
time.sleep(1)

# Membuka cart
cart = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_link").click()
time.sleep(1)

# Remove product from cart
remove_product_cart = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_link").click()
time.sleep(1)

# Masuk halaman checkout
checkout = driver.find_element(by=By.ID, value="checkout").click()
time.sleep(1)

# Cancel
cancel = driver.find_element(by=By.ID, value="cancel").click()
continue_shopping = driver.find_element(by=By.ID, value="continue-shopping").click()
time.sleep(1)

# Open menu
menu = driver.find_element(by=By.ID, value="react-burger-menu-btn").click()
time.sleep(1)

# Logout
menu = driver.find_element(by=By.ID, value="logout_sidebar_link").click()
time.sleep(1)

# message = driver.find_element(by=By.ID, value="message")
# text = message.text