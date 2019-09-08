#coding:utf-8
'''注意：类中函数间可以依赖于参数的传递进行调用，数据处理，可以断开靠变量进行连接，不一定要全部完整靠self进行连接'''
'''变量属性，全局变量与类下的属性，类定义的也可以是调用的模块r.request.seesion()'''
import requests
import re
import unittest
class Login():
    '''登录函数'''
    url="http://127.0.0.1/zentao/user-login.html"
    header={
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }
    def __init__(self,s,username,pwd):
        self.s=s
        self.username=username
        self.pwd=pwd
    def login_func(self):
        data01={
            "account":self.username,
            "keepLogin[]":"on",
            "password":self.pwd,
            "referer":"http://127.0.0.1/zentao/my/"
        }
        r=self.s.post(url=self.url,headers=self.header,data=data01,verify=False)
        res=r.content.decode(encoding="utf-8")
        return res
    def is_login_susses(self,res):
        if "parent.location" in res:
            return True
        else:
            return False
if __name__=="__main__":
    s=requests.session()
    login=Login(s,'admin11','123456')
    res=login.login_func()
    print(res)
    reult=login.is_login_susses(res)
    print(reult)