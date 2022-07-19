
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest


class TestLogin(unittest.TestCase):
    @classmethod
    def setUp(self):
        # Define a variable to hold all the configurations we want
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

    def test_datadrivenlogin(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        print("Title of the page is : ", driver.title)
        driver.implicitly_wait(5)
        #filepath = "C://login_saucelabs.xlsx"
        filepath = "C://Users/nagav/OneDrive/Documents/Book1.xlsx"

        rows = xlutils.getRowscount(filepath, 'Sheet1')
        cols = xlutils.getColumncount(filepath, 'Sheet1')
        for r in range(2, rows + 1):
            usrname = xlutils.readData(filepath, 'Sheet1', r, 1)
            pswrd = xlutils.readData(filepath, 'Sheet1', r, 2)
            time.sleep(3)
            driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(usrname)
            time.sleep(3)
            driver.find_element(By.XPATH, "//*[@id='password']").send_keys(pswrd)
            driver.find_element(By.XPATH, "//*[@id='login-button']").click()
            msg = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
            error = msg.is_displayed()
            if error is True:
                print("Test Passed")
                xlutils.writeDate(filepath, 'Sheet1', r, 3, "Test Passed")
            else:
                print("Test Failed")
                xlutils.writeDate(filepath, 'Sheet1', r, 3, "Test Failed")
            time.sleep(3)
            driver.find_element(By.XPATH, "//*[@id='user-name']").clear()
            driver.find_element(By.XPATH, "//*[@id='password']").clear()
            time.sleep(3)
        driver.quit()



if __name__ == "__main__":
    unittest.main()
