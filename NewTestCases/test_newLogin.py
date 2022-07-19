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
        #self.driver = webdriver.chrome()
        # Window management hacks because I'm using OS X. On Windows or Linux you could just specify these as a ChromeOption
        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()

    def test_pLogin(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        print("Title of the page is : ", driver.title)
        #username = usrname
        #paswrd = pwd
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        title = driver.title
        #self.assertTrue(title="Swag Labs")
        self.assertEqual("Swag Labs",title,"Webpage title not found!")
        if title == "Swag Labs":
            print("Login Success !!")
        else:
            print("Login Failed..")
        driver.save_screenshot('C://Screenshots/Listdisplay_afterlogin.png')
        driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
        driver.implicitly_wait(4)
        driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click() # clicking logout
        driver.save_screenshot('C://Screenshots/Afterlogout.png')
        title1 = driver.title
        self.assertEqual("Swag Labs", title1, "Webpage title not found!")
        time.sleep(4)
    @unittest.skip("Skipping")
    def test_Nlogin1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        print("Title of the page is : ", driver.title)
        driver.implicitly_wait(5)
        usrname = "standard_user"
        pwd = "secretsauce"
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(usrname)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys(pwd)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        meg = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        error = meg.is_displayed()
        # print("error is : ",error)
        if error is True:
            print("Wrong Password ,Negative case Passed!")
        else:
            print("Wrong Password,Negative case failed...")
        time.sleep(3)
        driver.save_screenshot('C://Screenshots/wrong_login.png')

    @unittest.skip("Skipping")
    def test_Nlogin2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        print("Title of the page is : ", driver.title)
        driver.implicitly_wait(5)
        usrname = "standarduser"
        pwd = "secret_sauce"
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(usrname)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys(pwd)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        meg = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        error = meg.is_displayed()
        # print("error is : ",error)

        if error is True:
            print("Wrong Username ,Negative case Passed!")
        else:
            print("Wrong Username,Negative case failed...")

    @unittest.skip("Skipping")
    def test_NLogin3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        print("Title of the page is : ", driver.title)
        driver.implicitly_wait(5)
        usrname = "standard_user"
        pwd = ""
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(usrname)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys(pwd)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        meg = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        error = meg.is_displayed()
        # print("error is : ",error)

        if error is True:
            print("Empty password ,Negative case Passed!")
        else:
            print("Empty password,Negative case failed...")

    @unittest.skip("Skipping")
    def test_NLogin4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        print("Title of the page is : ", driver.title)
        driver.implicitly_wait(5)
        usrname = "standarduser"
        pwd = "secretsauce"
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(usrname)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys(pwd)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        meg = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        error = meg.is_displayed()
        # print("error is : ",error)

        if error is True:
            print("Wrong Username&Password ,Negative case Passed!")
        else:
            print("Wrong Username&Password,Negative case failed...")

    def test_NLogin5(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/")
        print("Title of the page is : ", driver.title)
        driver.implicitly_wait(5)
        usrname = ""
        pwd = "secret_sauce"
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(usrname)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys(pwd)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        meg = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        error = meg.is_displayed()
        # print("error is : ",error)

        if error is True:
            print("Empty Username ,Negative case Passed!")
        else:
            print("Empty Username,Negative case failed...")

    @classmethod
    def tearDown(self):
        time.sleep(3)
        # Close the browser.
        # Note close() will close the current tab, if its the last tab it will close the browser. To close the browser entirely use quit()
        self.driver.quit()
# Boilerplate code to start the unit tests
if __name__ == "__main__":
    unittest.main()