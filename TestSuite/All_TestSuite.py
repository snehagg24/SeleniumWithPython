import unittest
from Package1.Testcase1 import Test
from Package1.Testcase2 import SearchEnginestest
from Package2.Testcase3 import AppTesting

#Get all tests
tc1=unittest.TestLoader().loadTestsFromTestCase(Test)
tc2=unittest.TestLoader().loadTestsFromTestCase(SearchEnginestest)
tc3=unittest.TestLoader().loadTestsFromTestCase(AppTesting)

#create test suite
ts1=unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner().run(ts1)

ts2=unittest.TestSuite([tc3])

unittest.TextTestRunner().run(ts2)

