from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="D:\Drivers\geckodriver-v0.24.0-win64\geckodriver.exe")
#driver=webdriver.Ie(executable_path="D:\Drivers\IEDriverServer_Win32_3.14.0\IEDriverServer.exe")

driver.get("https://github.com/")

print(driver.title) #title of page

print(driver.current_url) # return url of page

#print(driver.page_source) #return html code for page

driver.close() #close browser