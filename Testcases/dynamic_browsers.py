from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browsername = ""
driver = None
if browsername == 'Chrome':
    driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
elif browsername == 'Firefox':
    driver=webdriver.Firefox(executable_path="C:\seleniumdrivers\geckodriver.exe")
else:
    print("No browser specified....")

try:
    if driver != None:
        driver.get("https://www.google.com/")
        driver.quit()
except NameError as n:
    print(n)

