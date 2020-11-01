from selenium import *
from selenium import webdriver
import time


browser = webdriver.Firefox("/usr/local/bin/")
browser.maximize_window()
browser.get("https://maisons.bg/burgas/product/roma/")

acceptbut=browser.find_element_by_name("add-to-cart")

for i in range(3):
    acceptbut.click()
    acceptbut=browser.find_element_by_name("add-to-cart")

browser.get("https://maisons.bg/burgas/checkout/")
first_name=browser.find_element_by_name("billing_first_name").send_keys("name")
last_name=browser.find_element_by_name("billing_last_name").send_keys("lastname")
city=browser.find_element_by_name("billing_city").send_keys("city")
address=browser.find_element_by_name("billing_address_1").send_keys("address")
phone=browser.find_element_by_name("billing_phone").send_keys("number")
phone=browser.find_element_by_name("billing_email").send_keys("email@mail.bg")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
phone=browser.find_element_by_id("terms").click()
confirm=browser.find_element_by_name("woocommerce_checkout_place_order").click()