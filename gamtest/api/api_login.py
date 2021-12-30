# 导包
import requests


# 创建登录接口类
class ApiLogin(object):
    # 创建登录函数
    def api_login(self,url,username, password):
        headers = {"content-type": "application/json;charset=UTF-8"}
        data = {"username": username,"password": password}
        # url = "http://account.aliyun.test"
        url = url

        r = requests.post(url=url, json=data, headers=headers)
        return r
        assert r.status_code==200
        print(r.content)




if __name__ == '__main__':
    a = ApiLogin.api_login(self="", username="test_scy@aliyun.com", password="taobao1234")
    print(a)
