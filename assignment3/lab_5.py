# Importing required libraries

# pip install selenium




import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as rc
# Setting up the webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Navigating to the Amazon.ca homepage
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.w3schools.com/")
time.sleep(3)
wait = WebDriverWait(driver, 10)
button = wait.until(rc.element_to_be_clickable((By.XPATH, "//*[@id='pagetop']/div[3]/a[1]")))
button.click()
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
logininput = driver.find_element(By.CSS_SELECTOR, "#modalusername")
logininput.send_keys("nbains9911@gmail.com")
passwordinput = driver.find_element(By.CSS_SELECTOR, "#current-password")
passwordinput.send_keys("Emran*1999")
time.sleep(5)

Loginbutton = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div:nth-child(4) > div.LoginModal_modal__1Yybs.LoginModal_show__F6L8A.LoginModal_full_page__PoJE0 > div > div.LoginModal_cta_bottom_box__wU1AF > div.LoginModal_cta_bottom_box_button_login__5Fbwv > button")
Loginbutton.click()

time.sleep(6)




driver.close()

# Selecting a laptop from the search results



time.sleep(3)








# Waiting for the cart to update
time.sleep(5)



# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
