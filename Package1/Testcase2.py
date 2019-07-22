import unittest
from selenium import webdriver

class SearchEnginestest(unittest.TestCase):
    def test_Google(self):
        self.driver=webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("title of page:"+self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("title of page:" + self.driver.title)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()