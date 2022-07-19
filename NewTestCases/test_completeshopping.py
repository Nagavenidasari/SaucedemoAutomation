import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import time

class TestComplete(unittest.TestCase):
    @classmethod
    def setUp(self) :
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

    def test_completeshopping(self):
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
            self.driver.implicitly_wait(3)

            self.driver.find_element(By.XPATH,"//*[@id='checkout']").click() #clicking on checkout
            time.sleep(3)
            print("You are in entering customer details page")
            self.driver.find_element(By.XPATH,"//*[@id='first-name']").send_keys("Superman")
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='last-name']").send_keys("Nova")
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='postal-code']").send_keys("98776")
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='continue']").click()
            time.sleep(3)
            #scrolling to the finish button
            self.driver.execute_script("arguments[0].scrollIntoView()",self.driver.find_element(By.XPATH,"//*[@id='finish']"))
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='finish']").click() #clicked on finish
            print("You are in checkout page")
            self.driver.execute_script("arguments[0].scrollIntoView()",
                                       self.driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span"))
            print("You are in the Order complete page")
            c1 = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span").text
            self.assertEqual("CHECKOUT: COMPLETE!",c1,"Checkout complete not displayed.")
            c2 = self.driver.find_element(By.XPATH,"//*[@id='checkout_complete_container']/h2").text
            self.assertEqual("THANK YOU FOR YOUR ORDER",c2,"Thanks order is not displayed")
            #assert c2,"THANK YOU FOR YOUR ORDER"
            self.driver.save_screenshot("C:/Screenshots/Ordercomplete.png")
        else:
            print("You are not in the cart page")

    @classmethod
    def tearDown(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='logout_sidebar_link']").click()
        # Close the browser.
        time.sleep(3)
        # Note close() will close the current tab, if its the last tab it will close the browser. To close the browser entirely use quit()
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
