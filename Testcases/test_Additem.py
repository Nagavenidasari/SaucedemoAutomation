from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def test_Additem():
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
        print("Login Failed..")
#item = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[1]/a/div").text
    item = driver.find_element(By.XPATH,"//*[@id='item_1_title_link']/div").text
    print(item)
    item1 = "Sauce Labs Bolt T-Shirt"
#item_avail = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").text
#print("Status: ", item_avail)
    if item == item1:
        item_avail=driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").text
        print("Status: ",item_avail)
        print(item1," is available")
    #item_noavail = driver.find_element(By.XPATH,"//*[@id='remove-sauce-labs-bolt-t-shirt']").text
    #print("Status: ", item_noavail)
        if item_avail == "ADD TO CART":
            driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
            print("Sauce Labs Bolt T-Shirt is added in the cart")
            time.sleep(3)
            driver.implicitly_wait(5)
        #driver.find_element(By.XPATH,"//*[@id='hopping_cart_container']/a/span").click()
            driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a/span").click()
            print("Clicked on the cart icon")
            cart=driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span").text
            #print("Title of the page is : ",cart)
            if cart == "YOUR CART":
                print("you are in the cart page")
                itemname = driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div").text
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

    time.sleep(5)
    driver.quit()
