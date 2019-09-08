#coding:utf-8
import requests,unittest
from common.loginclass import Login
class Login_test(unittest.TestCase):
    '''登录测试'''
    def setUp(self):
        self.s=requests.session()
    def test_pass(self):
        login=Login(s=self.s,username="admin",pwd="123456")
        respos=login.login_func()
        result=login.is_login_susses(respos)
        self.assertTrue(result)
    def test_fail(self):
        login=Login(s=self.s,username="admin111",pwd="123456")
        respos=login.login_func()
        result=login.is_login_susses(respos)
        self.assertFalse(result)
    def tearDown(self):
        self.s.cookies.clear_expired_cookies()
if __name__=="__main__":
    unittest.main()