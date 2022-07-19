from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def openbrowser(browsername,username,pwd):
    #driver = None
    if browsername == 'Chrome':
        driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
        driver.get("https://www.saucedemo.com/")
        print("Title of the page is : ", driver.title)
        usrname = username
        paswrd = pwd
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(usrname)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys(paswrd)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        title = driver.title
        if title == "Swag Labs":
            print("Login Success !!")
        else:
            print("Login Failed..")
        driver.quit()
    elif browsername == 'Firefox':
        driver = webdriver.Firefox(executable_path="C:\seleniumdrivers\geckodriver.exe")
        driver.get("https://www.saucedemo.com/")
        print("Title of the page is : ", driver.title)
        #Login("standard_user", "secret_sauce")
        usrname = username
        paswrd = pwd
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(usrname)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys(paswrd)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        title = driver.title
        if title == "Swag Labs":
            print("Login Success !!")
        else:
            Print("Login Failed..")
        driver.quit()
    else:
        print("No browser specified....")

def openbrowserNlogin(browserName,uname,pwd):
    if browserName == 'Chrome':
        driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
        driver.get("https://www.saucedemo.com/")
        print("Title of the page is : ", driver.title)
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(uname)
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

        driver.quit()
    elif browserName == 'Firefox':
        driver = webdriver.Firefox(executable_path="C:\seleniumdrivers\geckodriver.exe")
        driver.get("https://www.saucedemo.com/")
        print("Title of the page is : ", driver.title)
        #Login("standard_user", "secret_sauce")
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(uname)
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

        driver.quit()
    else:
        print("No browser specified....")



def test_Positivelogin():
    openbrowser("Chrome","standard_user","secret_sauce")
    time.sleep(5)
   # openbrowser("Firefox", "standard_user", "secret_sauce")

def test_NLogin1():
    openbrowserNlogin("Chrome","standard_user","secretsauce")

def test_NLogin2():
    openbrowserNlogin("Chrome","standarduser","secret_sauce")

def test_NLogin3():
    openbrowserNlogin("Chrome", "standarduser", "secretsauce")

def test_NLogin4():
    openbrowserNlogin("Chrome", "", "secret_sauce")

def test_NLogin5():
    openbrowserNlogin("Chrome", "standard_user", "")

def test_NLogin6():
    openbrowserNlogin("Chrome", "", "")


