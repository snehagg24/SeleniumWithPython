from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)

driver.get("http://www.pavantestingtools.com/")

print(driver.title)

driver.back()

print(driver.title)

driver.forward()

print(driver.title)