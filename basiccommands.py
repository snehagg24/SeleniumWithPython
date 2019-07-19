import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title) #return title of page

print(driver.current_url) #return url of page

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

#driver.close() #currently focussed browser

driver.quit() #close all browser