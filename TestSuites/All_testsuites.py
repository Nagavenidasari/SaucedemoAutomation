import unittest
from NewTestCases.test_newLogin import TestLogin
from NewTestCases.test_add_remove_continue import Testshopping
from NewTestCases.test_completeshopping import TestComplete
from Testcases.test_pricelist import Testpricelist

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Testpricelist)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Testshopping)
tc4 = unittest.TestLoader().loadTestsFromTestCase(TestComplete)

sampletests = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner(verbosity=2).run(sampletests)

functionaltests = unittest.TestSuite([tc3,tc4])
unittest.TextTestRunner(verbosity=2).run(functionaltests)
