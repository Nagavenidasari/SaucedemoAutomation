from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest
import unittest
# pricelist of all the items in the page


class Testpricelist(unittest.TestCase):
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

    def test_pricelist1(self):

        pricelist = len(self.driver.find_elements(By.XPATH,"//*[@class='inventory_item_price']"))
        print("Number of items in the page :", pricelist)
        for i in range(1 , pricelist+1):
            print(self.driver.find_element(By.XPATH,"//*[@id='inventory_container']/div/div["+str(i)+"]/div[2]/div[2]/div").text)


# finding all the items and storing in a list

    # displaying all the items price list in the page


    @classmethod
    def tearDown(self):
        time.sleep(3)
        # Close the browser.
        # Note close() will close the current tab, if its the last tab it will close the browser. To close the browser entirely use quit()
        self.driver.quit()
# Boilerplate code to start the unit tests
if __name__ == "__main__":
    unittest.main()