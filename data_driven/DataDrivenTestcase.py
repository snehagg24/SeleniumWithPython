import data_driven.XLUtils
from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

path="C:\\Users\sneha_kanekar\PycharmProjects\SeleniumwithPython\TestData.xlsx"

rows=data_driven.XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username=data_driven.XLUtils.readData(path,'Sheet1',r,1)
    password=data_driven.XLUtils.readData(path,'Sheet1',r,2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("login").click()

    if driver.title == "Find a Flight: Mercury Tours:":
        print("test is passed")
        data_driven.XLUtils.writeData(path,"Sheet1",r,3,"test passed")
    else:
        print("test is failed")
        data_driven.XLUtils.writeData(path,"Sheet1",r,3,"test failed")

    driver.find_element_by_link_text("Home").click()

driver.close()