from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


#options.addExtensions(new File("C:\seleniumdrivers\chromedriver.exe"));

#ChromeDriver driver = new ChromeDriver(options);
#firefox browser
#driver = webdriver.Firefox(executable_path="C:\seleniumdrivers\geckodriver.exe")
driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")

#driver.get("https://www.linkedin.com") # launches linkedin.com
#print(driver.title) # print title of the page
#print(driver.current_url) # prints current url
#print(driver.page_source) # prints the html page source

#driver.find_element(By.NAME,"session_key").send_keys("nagavenik@gmail.com")
#print("User Name Entered")
#driver.find_element(By.NAME, "session_password").send_keys("sanara123")
#print("Password entered")
#driver.find_element_by_name("session_password").send_keys("Sanara753")
#time.sleep(5)
#driver.find_element_by_xpath("//*[@id='main-content']/section[1]/div/div/form/button").click()
driver.get("https://www.gmail.com")
print(driver.title)
time.sleep(2)
driver.find_element(By.ID,"identifierId").send_keys("nagavenitester")
print("Entered Username")
time.sleep(1)
driver.find_element(By.ID,"identifierNext").click()
print("Clicked on Next")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='whsOnd zHQkBf']").send_keys("Tester1234!")
#driver.find_element(By.ID,"//*[@id='password']").send_keys("Tester123!")
#driver.find_element(By.XPATH,"//*[@id='whsOnd zHQkBf']//html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys("Tester123!")
#driver.find_element(By.NAME,"password").send_keys("Tester123!")
#driver.find_element(By.CLASS_NAME,"whsOndzHQkBf").send_keys("Tester123!")html.CMgTXc body#yDmH0d.nyoS7c.SoDlKd.EIlDfe div.H2SoFe.LZgQXe.TFhTPc div#initialView.RAYh1e.LZgQXe.qmmlRd div.xkfVF div.Aa1VU div#view_container.JhUD8d.SQNfcc.vLGJgb div.zWl5kd div.DRS7Fe.bxPAYd.k6Zj8d div.pwWryf.bxPAYd div.Wxwduf.Us7fWe.JhUD8d div.WEQkZc div.bCAAsb form span section.aTzEhb div.CxRgyd div div.SdBahf.Fjk18 div.eEgeR div.DPChp div.Txuhic div.hDp5Db div#password.rFrNMe.ze9ebf.YKooDc.wIXLub.zKHdkd.sdJrJc div.aCsJod.oJeWuf div.aXBtI.Wic03c div.Xb9hP input.whsOnd.zHQkBf

print("Entered Password")
time.sleep(2)

driver.find_element(By.ID,"passwordNext").click()
print("Clicked on Next")
time.sleep(2)
driver.find_element(By.XPATH,"//img[@class='gb_Ba gbii']").click()
print("Clicked on 'N'")
driver.implicitly_wait(12)

driver.find_element(By.XPATH,"//div[text()='Sign out']").click()
#https://accounts.google.com/Logout?hl=en&amp;continue=https://mail.google.com&amp;service=mail&amp;timeStmp=1654790092&amp;secTok=.AG5fkS87Yv5VlKW4JyqB8xPK6Ot-3MKsjA&amp;ec=GAdAFw
#driver.find_element(By.XPATH,"//*[@href='https://accounts.google.com/Logout?hl=en&amp;continue=https://mail.google.com&amp;service=mail&amp;timeStmp=1654790092&amp;secTok=.AG5fkS87Yv5VlKW4JyqB8xPK6Ot-3MKsjA&amp;ec=GAdAFw']").click()
#driver.find_element(By.XPATH,"//*[@id='gb']/div[2]/div[3]/div[3]/iframe/html/body/div/c-wiz/div/div/div/div/div[2]/div[3]").click()
#driver.find_element(By.XPATH,"//div[@id='yDmH0d']//div[@class='EeWTFe']//span[@jsaction='click:vyP2Ce']//a[@class='jAcX2 ZWVAt R37Fhd']").click()
#//*[@id="gb"]/div[2]/div[3]/div[3]/iframe/html/body/div/c-wiz/div/div/div/div/div[2]/div[3]/span/a
#driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div/div/div[2]/div[3]/span/a/div").click()

#ele = driver.find_element(By.XPATH,"//*[@id='yDmH0d']/c-wiz/div/div/div/div/div[1]")
#print(ele.is_displayed())
#driver.find_element(By.XPATH,"/html/body/div/c-wiz/div/div/div/div/div[2]/div[3]/span/a").click()
#driver.find_element(By.XPATH,"//a[@class='jAcX2 ZWVAt R37Fhd']/div/a").click()
#driver.find_element(By.XPATH("/html/body/div/c-wiz/div/div/div/div/div[2]/div[3]/span")).click()
#driver.find_element(By.XPATH,"//*[@id='yDmH0d']/c-wiz/div/div/div/div/div[2]/div[3]").click()
#driver.find_element(By.XPATH,"/html/body/div/c-wiz/div/div/div/div/div[2]/div[3]/span/a/div").click()
#driver.find_element(By.CSS_SELECTOR,"#yDmH0d > c-wiz > div > div > div > div > div:nth-child(2) > div.EeWTFe > span > a > div").click()
#//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div[2]/div[3]/span/a
#/html/body/div/c-wiz/div/div/div/div/div[2]/div[3]
#driver.find_element(By.XPATH,"//*[@class='.jAcX2']/html/body/div/c-wiz/div/div/div/div/div[2]/div[3]/span/a").click()
#driver.find_element(By.XPATH,"//div[contains(text(),'Sign out')]").click()
#driver.find_element(By.XPATH,"//span[@jsaction='click:vyP2Ce']").click()
#driver.find_element(By.CSS_SELECTOR,".jAcX2 > div:nth-child(1)").click()
#driver.find_element(By.CSS_SELECTOR,".EeWTFe > span:nth-child(1)").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"'Sign out'").click()
#driver.find_element(By.XPATH,"//div[contains(@class,'EeWTFe')]").click()

#driver.find_element(By.CSS_SELECTOR,"'.jAcX2'").click()

#.jAcX2 > div:nth-child(1)
#/html/body/div/c-wiz/div/div/div/div/div[2]/div[3]
#/html/body/div/c-wiz/div/div/div/div/div[2]/div[3]/span
#.jAcX2

#.EeWTFe > span:nth-child(1)
#<a rel="noopener noreferrer" data-sol="" target="_top" jsname="L8VV9b" class="jAcX2 ZWVAt R37Fhd" href="https://accounts.google.com/Logout?hl=en&amp;continue=https://mail.google.com&amp;service=mail&amp;timeStmp=1654708365&amp;secTok=.AG5fkS9pCWzjfF5HMuMZvep6WqoDc8PJ3w&amp;ec=GAdAFw"><div class="wBFtm">Sign out</div></a>
print("Clicked Signout")
time.sleep(3)

#driver.find_element(By.ID,"identifierNext").click()
#driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]").click()
#driver.close()

#driver.find_element(By.XPATH,"/html/body/header/div/div/div/a[2]").click()


#driver.find_element(By.XPATH,"//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div/div/div[2]").click()
#time.sleep(10)
#driver.close() # closes the page