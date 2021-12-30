#导包
import unittest
from gamtest.api.api_login import ApiLogin


#新建测试类

class TestLogin(unittest.TestCase):

    def test_login(self):

        url = "http://account.aliyun.test"
        username = "test_scy@aliyun.com"
        password = "taobao1234"

        s = ApiLogin().api_login(url,username,password)

        print("查看相应结果："s.content)

        self.assertEquals("ok",s.json()['massage'])

        self.assertEquals(200,s.status_code)



