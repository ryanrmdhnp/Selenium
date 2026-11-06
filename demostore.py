from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

# Akses URL
driver.get('https://demostore.supersqa.com/')

driver.implicitly_wait(0.5)

# Scroll bawah
driver.execute_script("window.scrollBy(0,200)")

# Buka detail produk
albumwoo = driver.find_element(by=By.CLASS_NAME, value='woocommerce-loop-product__title')
albumwoo.click()
time.sleep(3)

# Ubah quantity
qty = driver.find_element(By.NAME, 'quantity')
qty.clear()
qty.send_keys("2")
time.sleep(3)

# Add to cart
atc = driver.find_element(By.NAME, 'add-to-cart')
atc.click()
time.sleep(3)

# Check cart
view_cart = driver.find_element(By.LINK_TEXT,'View cart')
view_cart.click()
time.sleep(3)

# Add quantity product on cart
add_qty = driver.find_element(By.XPATH,'//*[@id="post-7"]/div/div/div[4]/div/div/div[2]/table/tbody/tr/td[2]/div/div[3]/div/button[2]')
add_qty.click()
time.sleep(3)

# Remove product on cart
remove = driver.find_element(By.CLASS_NAME,'wc-block-cart-item__remove-link')
remove.click()
time.sleep(3)

# Expected Condition to show text cart is empty
empty = wait.until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'wp-block-woocommerce-empty-cart-block'),
        "Your cart is currently empty!"
    )
)

# Go to home page
home = driver.find_element(By.LINK_TEXT, 'Home')
home.click()
time.sleep(3)

# Filtering
filter = Select(driver.find_element(By.CLASS_NAME, 'orderby'))
filter.select_by_value('rating')
time.sleep(3)

# Searching
search = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
search.send_keys("logo")
search.send_keys(Keys.ENTER)
time.sleep(3)

# Add to cart product from home page
atc_home = driver.find_element(By.XPATH, '//*[@id="main"]/ul/li[1]/a[2]')
atc_home.click()
time.sleep(3)

# Expected condition to show price on cart
price = wait.until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'cart-contents'),
        "18.00"
    )
)