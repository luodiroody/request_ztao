#coding:utf-8
import requests
from common import loginclass
class Postmessage ():
    s=requests.session()
    login=loginclass.Login(s=s,username='admin',pwd='123456')
    rec=login.login_func()
    print(rec)
    #发帖
    def New_postmessage(self):
        url="http://127.0.0.1/zentao/bug-create-1-0-moduleID=0.html"
        headers={
            "Connection":"keep-alive",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryQ2NQmhJocPQEpSpe"
        }
        data={
            "Content-Disposition: form-data; name='assignedTo'":"",
            "Content-Disposition: form-data; name='browser'":"",
            "Content-Disposition: form-data; name='case'":"0",
            "Content-Disposition: form-data; name='caseVersion'":"0",
            "Content-Disposition: form-data; name='color":"",
            "Content-Disposition: form-data; name='files[]'":"",
            "Content-Disposition:form-data; name='keywords'":"002",
            "Content-Disposition:form-data; name='labels[]'":"test02",
            "Content-Disposition:form-data;name='mailto[]'":"admin",
            "Content-Disposition:form-data;name='module'":"0",
            "Content-Disposition:form-data;name='openedBuild[]'":"truck",
            "Content-Disposition: form-data;name='os'":"",
            "Content-Disposition: form-data;name='pri'":"0",
            "Content-Disposition: form-data;name='product'":"1",
            "Content-Disposition: form-data;name='project'":"",
            "Content-Disposition: form-data;name='result'":"0",
            "Content-Disposition: form-data; name='severity'":"3",
            "Content-Disposition: form-data; name='steps'":"<p>[步骤]打开01</p><p>[结果]打开02</p><p>[期望]关闭03</p>",
            "Content-Disposition: form-data; name='story'":"0",
            "Content-Disposition: form-data; name='task'":"0",
            "Content-Disposition: form-data; name='testtask'":"0",
            "Content-Disposition: form-data; name='title'":"2019090402",
            "Content-Disposition: form-data; name='type'":"codeerror",
            "Content-Disposition: form-data; name='uid'":"5d6fd0e7908955"
        }
        res=self.s.post(url=url,data=data,verify=False)
        return  res
if __name__=="__main__":
    post=Postmessage()
    res=post.New_postmessage()
    print(res.content.decode(encoding="utf-8"))
    #删帖

    #编辑

    #查询

