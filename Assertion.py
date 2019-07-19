import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        self.driver=webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        title=self.driver.title

        self.assertEqual("Google",title,"title not same")
        self.assertNotEqual("Google123", title, "title is same")

if __name__ == '__main__':
    unittest.main()