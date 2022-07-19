# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pathlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
#driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\seleniumdrivers\geckodriver.exe")
#driver = webdriver.Firefox(executablepath=str('C:\Users\nagav\PycharmProjects\SeleniumTest1\Drivers\geckodriver.exe'))
#driver = webdriver.firefox("C:/Users/nagav/PycharmProjects/SeleniumTest1/Drivers/geckodriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element_by_name("q").send_keys("LinkedIn Login")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
print(driver.title) # title of the page
print(driver.current_url) #url www.google.com
driver.close() # title of the page


#driver.find_element_by_partial_link_text("LinkedIn Login").click()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
