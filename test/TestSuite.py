import HTMLTestReportCN
from TestFunc import *

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFunc))
    with open(u'测试结果.html', 'wb') as f:
        runner = HTMLTestReportCN.HTMLTestRunner(stream=f,
                                                 title=u'公司测试报告',
                                                 description=u'Authentication',
                                                 verbosity=2
                                                 )
        runner.run(suite)
    f.close()
