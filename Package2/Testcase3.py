import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("test_search")

    @unittest.skip("Because it is not yet ready")
    def test_advancesearch(self):
        print("test_advancesearch")

    @unittest.skipIf(1==1,"reason")
    def test_prepaidrecharge(self):
        print("test_prepaidrecharge")

    def test_postpaidrecharge(self):
        print("test_postpaidrecharge")

    def test_loginbygmail(self):
        print("test_loginbygmail")

    def test_loginbytwitter(self):
        print("test_loginbytwitter")

if __name__ == '__main__':
    unittest.main()
