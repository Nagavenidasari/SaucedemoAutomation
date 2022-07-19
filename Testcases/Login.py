from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("https://www.saucedemo.com/")
print("Title of the page is : " , driver.title)
driver.implicitly_wait(5)
usrname = "standard_user"
pwd = "secret_sauce"
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys(usrname)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='password']").send_keys(pwd)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='login-button']").click()
title = driver.title
if title =="Swag Labs" :
    print("Login Success !!")
else:
    Print("Login Failed..")

driver.close()
driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("https://www.saucedemo.com/")
print("Title of the page is : " , driver.title)
driver.implicitly_wait(5)
usrname = "standard_user"
pwd = "secretsauce"
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys(usrname)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='password']").send_keys(pwd)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='login-button']").click()
meg = driver.find_element(By.XPATH , "//*[@id='login_button_container']/div/form/div[3]/h3")
error = meg.is_displayed()
#print("error is : ",error)

if error is True:
    print("Wrong Password ,Negative case Passed!")
else:
    print ("Wrong Password,Negative case failed...")

driver.close()

driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("https://www.saucedemo.com/")
print("Title of the page is : " , driver.title)
driver.implicitly_wait(5)
usrname = "standarduser"
pwd = "secret_sauce"
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys(usrname)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='password']").send_keys(pwd)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='login-button']").click()
meg = driver.find_element(By.XPATH , "//*[@id='login_button_container']/div/form/div[3]/h3")
error = meg.is_displayed()
#print("error is : ",error)

if error is True:
    print("Wrong Username ,Negative case Passed!")
else:
    print ("Wrong Username,Negative case failed...")

driver.close()

driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("https://www.saucedemo.com/")
print("Title of the page is : " , driver.title)
driver.implicitly_wait(5)
usrname = "standarduser"
pwd = "secretsauce"
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys(usrname)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='password']").send_keys(pwd)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='login-button']").click()
meg = driver.find_element(By.XPATH , "//*[@id='login_button_container']/div/form/div[3]/h3")
error = meg.is_displayed()
#print("error is : ",error)

if error is True:
    print("Wrong Username&Password ,Negative case Passed!")
else:
    print ("Wrong Username&Password,Negative case failed...")

driver.close()

driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("https://www.saucedemo.com/")
print("Title of the page is : " , driver.title)
driver.implicitly_wait(5)
usrname = ""
pwd = "secret_sauce"
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys(usrname)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='password']").send_keys(pwd)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='login-button']").click()
meg = driver.find_element(By.XPATH , "//*[@id='login_button_container']/div/form/div[3]/h3")
error = meg.is_displayed()
#print("error is : ",error)

if error is True:
    print("Empty Username ,Negative case Passed!")
else:
    print ("Empty Username,Negative case failed...")

driver.close()

driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("https://www.saucedemo.com/")
print("Title of the page is : " , driver.title)
driver.implicitly_wait(5)
usrname = "standard_user"
pwd = ""
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys(usrname)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='password']").send_keys(pwd)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='login-button']").click()
meg = driver.find_element(By.XPATH , "//*[@id='login_button_container']/div/form/div[3]/h3")
error = meg.is_displayed()
#print("error is : ",error)

if error is True:
    print("Empty password ,Negative case Passed!")
else:
    print ("Empty password,Negative case failed...")

driver.close()

driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("https://www.saucedemo.com/")
print("Title of the page is : " , driver.title)
driver.implicitly_wait(5)
usrname = ""
pwd = ""
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys(usrname)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='password']").send_keys(pwd)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='login-button']").click()
meg = driver.find_element(By.XPATH , "//*[@id='login_button_container']/div/form/div[3]/h3")
error = meg.is_displayed()
#print("error is : ",error)

if error is True:
    print("Empty Username&Password ,Negative case Passed!")
else:
    print ("Wrong Username&Password,Negative case failed...")

driver.close()