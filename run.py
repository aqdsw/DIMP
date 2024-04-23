import unittest
from testcases.test_pad import TestPad
import HTMLTestRunner_PY3
import config
import time


suite = unittest.TestLoader().loadTestsFromTestCase(TestPad)
with open(config.BASE_DIR + "/report/pad_report{}.html".format(time.strftime('%Y%m%d %H%M%S')),mode='wb') as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f)
    runner.run(suite)

