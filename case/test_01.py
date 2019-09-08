#coding:utf-8
import unittest
class Testcase (unittest.TestCase):
    u'''第一次测试脚本发布'''
    def setUp(self):
        print('this is setUp')
    def test_a(self):
        u'''hhhhhhhhhh'''
        a=1
        b=2
        c=a+b
        self.assertEqual(c,3)
    def test_001(self):
        aa=3
        bb=4
        dd=aa+bb
        self.assertEqual(dd,8)
    def tearDown(self):
        print('over')
if __name__ =="__main__":
    unittest.main()
    #suite=unittest.TestSuite()
    #suite.addTest(Testcase("test_001"))
    #testcase=[Testcase("test_a")]
    #suite.addTests(testcase)
    #run=unittest.TextTestRunner()
    #run.run(suite)