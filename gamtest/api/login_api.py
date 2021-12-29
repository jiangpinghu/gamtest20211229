#导包
import requests

#创建登录接口类
class LoginApi():
    #创建登录函数
    def longin_api(self):

        headers = {"CotentType":"application/json"}
        data = {"usename":"test_scy@aliyun.com ",
                "password":"taobao1234"}
        url = "http://account.aliyun.test/login/login.htm"

        rsp = requests.post(url=url,data=data,headers=headers)

        print(rsp)