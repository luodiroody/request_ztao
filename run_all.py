#coding:utf-8
import unittest
import time
import HTMLTestRunner
filename=time.strftime("%Y%m%d%H%M%S")
casePath="D:\interface_test\case"
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern="test*.py")
print(discover)
#runner = unittest.TextTestRunner()
#runner.run(discover)
reportPath="D:\\interface_test\\report\\"+filename+".html"
fp=open(reportPath,"wb")
runner=HTMLTestRunner.HTMLTestRunner(fp,verbosity=2,title=u"测试报告",description="20190831")
runner.run(discover)
fp.close()