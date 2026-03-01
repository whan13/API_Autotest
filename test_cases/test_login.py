'''
参数化
'''
import os

import pytest
from utils.read_yaml import Read_Yaml
from common.method import MyRequests

r_yaml = Read_Yaml()
req = MyRequests()

class Test_Login():
    @pytest.mark.parametrize('data', r_yaml.read_list(filedir='data', filename='login_data.yaml'))
    def test_login_params(self,data):
        # print(data['url'])
        resp=req.post(url=data['url'],json=data['body'],headers=data['header'])
        print(resp.json())
        # 校验状态码和返回的消息内容
        assert resp.status_code == 200
        assert resp.json()['msg'] == data['expected']['msg']



if __name__ == '__main__':
    # pytest.main(['-vs','test_login.py'])
    pytest.main(['-vs', 'test_login.py', '--alluredir', '../report/result'])
    os.system('allure serve ../report/result')