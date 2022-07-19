import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest

class Testshopping(unittest.TestCase):
    @classmethod
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()

        # Define chrome option configurations here ...

        # Create driver, pass it the path to the chromedriver file and the special configurations you want to run
        self.driver = webdriver.Chrome(
            executable_path='C:\seleniumdrivers\chromedriver.exe',
            chrome_options=chrome_options)
        # self.driver = webdriver.chrome()
        # Window management hacks because I'm using OS X. On Windows or Linux you could just specify these as a ChromeOption
        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()
        usr = "standard_user"
        pwd = "secret_sauce"
        self.driver.get("https://www.saucedemo.com/")
        print("Title of the page is : ", self.driver.title)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(usr)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(pwd)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        title = self.driver.title
        if title == "Swag Labs":
            print("Login Success !!")
        else:
            print("Login Failed..")

    def test_additem(self):
        item = self.driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div").text
        print(item)
        item1 = "Sauce Labs Bolt T-Shirt"
        # item_avail = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").text
        # print("Status: ", item_avail)
        if item == item1:
            item_avail = self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").text
            print("Status: ", item_avail)
            print(item1, " is available")
            # item_noavail = driver.find_element(By.XPATH,"//*[@id='remove-sauce-labs-bolt-t-shirt']").text
            # print("Status: ", item_noavail)
            if item_avail == "ADD TO CART":
                self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
                print("Sauce Labs Bolt T-Shirt is added in the cart")
                time.sleep(3)
                self.driver.implicitly_wait(5)
                # driver.find_element(By.XPATH,"//*[@id='hopping_cart_container']/a/span").click()
                self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a/span").click()
                print("Clicked on the cart icon")
                cart = self.driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span").text
                # print("Title of the page is : ",cart)
                if cart == "YOUR CART":
                    print("you are in the cart page")
                    itemname = self.driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div").text
                    if itemname == "Sauce Labs Bolt T-Shirt":
                        print(itemname, "Item is available in the cart")
                    else:
                        print(itemname, "not available in the cart")

                else:
                    print("You are not in the cart page...")

            else:
                print("Sauce Labs Bolt T-Shirt is already in the cart")
        else:
            print("Item not found, Text case failed!")

    def test_removeitem(self):
        self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(2)
        print("Added Sauce labs bike light to the cart")
        self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        print("Added Saucelabs fleece jacket to the cart")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()
        print("Added Saucelabs onesie to the cart")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
        print("Clicked on the cart")
        time.sleep(3)
        cart = self.driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span").text
        if cart == "YOUR CART":
            items = set()  # define set to add all the items in the cart page
            print("You are in the cart page")
            item1 = self.driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div").text
            print("Found ",item1)
            items.add(item1)
            item2 = self.driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text
            print("Found ",item2)
            items.add(item2)
            item3 = self.driver.find_element(By.XPATH, "//*[@id='item_2_title_link']/div").text
            print("Found ",item3)
            items.add(item3)
            for item in items:
                if item == "Sauce Labs Onesie":
                    self.driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-onesie']").click()
                    print("Removed Sauce Labs Onesie")
                # else:
                #   print("Unable to find Sauce Labs Onesie ")
        else:
            print("you are not in the cart page")

    def test_continueshopping(self):
        self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(2)
        print("Added Sauce labs bike light to the cart")
        self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        print("Added Saucelabs fleece jacket to the cart")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()
        print("Added Saucelabs onesie to the cart")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
        print("Clicked on the cart")
        time.sleep(3)
        cart = self.driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span").text
        if cart == "YOUR CART":
            print("You are in the cart page")
            self.driver.find_element(By.XPATH, "//*[@id='continue-shopping']").click()
            print("Clicked on continue shopping button")
            time.sleep(3)
            title1 = self.driver.title
            print("Title of the page is : ", title1)
            assert title1 == "Swag Labs"
            # if assert title1 == "Swag Labs":
            #   print("You are back in the shopping list page")
            # else:
            #   print("You are not in shopping page")
        else:
            print("you are not in the cart page")

    @classmethod
    def tearDown(self):
        time.sleep(3)
        # Close the browser.
        # Note close() will close the current tab, if its the last tab it will close the browser. To close the browser entirely use quit()
        self.driver.quit()


# Boilerplate code to start the unit tests
if __name__ == "__main__":
    unittest.main()
