from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest

def test_removeitem():
    driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    print("Title of the page is : ", driver.title)
    driver.implicitly_wait(5)
    usrname = "standard_user"
    pwd = "secret_sauce"
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(usrname)
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys(pwd)
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='login-button']").click()
    title = driver.title
    if title == "Swag Labs":
        print("Login Success !!")
    else:
        print("Login Failed..")
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-bike-light']").click()
    time.sleep(2)
    print("Added Sauce labs bike light to the cart")
    driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
    print("Added Saucelabs fleece jacket to the cart")
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-onesie']").click()
    print("Added Saucelabs onesie to the cart")
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a").click()
    print("Clicked on the cart")
    time.sleep(3)
    cart=driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span").text
    if cart == "YOUR CART":
        items = set() # define set to add all the items in the cart page
        print("You are in the cart page")
        item1 = driver.find_element(By.XPATH,"//*[@id='item_5_title_link']/div").text
        print(item1)
        items.add(item1)
        item2 = driver.find_element(By.XPATH,"//*[@id='item_0_title_link']/div").text
        print(item2)
        items.add(item2)
        item3 = driver.find_element(By.XPATH, "//*[@id='item_2_title_link']/div").text
        print(item3)
        items.add(item3)
        for item in items:
            if item == "Sauce Labs Onesie":
                driver.find_element(By.XPATH,"//*[@id='remove-sauce-labs-onesie']").click()
                print("Removed Sauce Labs Onesie")
            #else:
             #   print("Unable to find Sauce Labs Onesie ")
    else:
        print("you are not in the cart page")
    time.sleep(5)
    driver.quit()

