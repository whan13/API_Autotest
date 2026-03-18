import pytest
import os
import json
from db.db_operation import db
from common.method import MyRequests
from common.public_path import base_path
from utils.read_excel import Read_Excel
from common.read_write_file import Read_Write_File
from utils.logger import trace_log
req=MyRequests()#实例化发起请求的类
read_ex=Read_Excel()#实例化读取excel的类
r_w_file=Read_Write_File()

class Test_Cms:
    user_id = None

    @pytest.fixture(autouse=True, scope="class")
    def clean_db_data(self):
        yield
        # 2. 现在这里就可以正常调用了
        if self.user_id:
            # 执行删除并获取受影响行数
            res = db.delete_user(self.user_id) 
            if res > 0:
                print(f"[Teardown] 数据库清理成功，删除了 ID: {self.user_id}")
            else:
                print(f"[Teardown] 数据库中已无 ID: {self.user_id}，无需清理")

    #在类方法上方写一行 @trace_log，它就会自动帮你记录每一个接口的请求和响应信息。这对于排查测试失败的原因（Traceback）极其有用
    @trace_log
    def test_login(self):
        resp=req.post(url=read_ex.get_url(1),data=read_ex.get_body(1))
        print(resp.json())
        # print(type(json.loads(read_ex.get_except(1))))
        assert resp.json()['code'] == json.loads(read_ex.get_except(1))['code']
        return resp.json()

    @trace_log
    def test_add(self):
        resp = req.post(url=read_ex.get_url(2), data=read_ex.get_body(2))
        print(resp.json())
        r_w_file.write_file()#把新添加用户的ID从数据库读取出来，然后写入user_id.txt文件
        return resp.json()

    @trace_log
    def test_check(self):
        resp = req.post(url=read_ex.get_url(3), data=read_ex.get_body(3))
        print(resp.json())
        global id_value
        id_value=resp.json()['model']['userList'][0]['id']
        return resp.json()

    @trace_log
    def test_delete(self):
        id_value=r_w_file.read_file()#读取txt文件里最近添加的用户id
        body={'ids':id_value}
        resp = req.post(url=read_ex.get_url(4), data=body)
        print(resp.json())
        print(f"我要删的ID确实是: {id_value}")
        return resp.json()

    # @trace_log
    # def test_delete(self):
    #     id_value = r_w_file.read_file() # 读取 txt 里的 ID
    #     body = {'ids': id_value}
    #     print(f"--- 准备删除的 ID 是: {id_value} ---") # 加这一行
    #     resp = req.post(url=read_ex.get_url(4), data=body)
    #     return resp.json()
    


    # #-------优化return，数据传递
    # # 定义类变量，用于在不同测试用例间传递数据
    # user_id = None 

    # @trace_log
    # def test_login(self):
    #     resp = req.post(url=read_ex.get_url(1), data=read_ex.get_body(1))
    #     res_json = resp.json()
    #     print(res_json)
    #     # 断言
    #     # assert res_json['code'] == json.loads(read_ex.get_except(1))['code']
    #     assert str(res_json['code']) == str(json.loads(read_ex.get_except(1))['code'])

    # @trace_log
    # def test_add(self):
    #     resp = req.post(url=read_ex.get_url(2), data=read_ex.get_body(2))
    #     res_json = resp.json()
    #     print(res_json)
        
    #     # 1. 增加断言确保添加成功
    #     # assert res_json['code'] == 200 
    #     assert int(res_json['code']) == 200
        
    #     # 2. 依然可以写入文件（如果你的框架需要持久化数据）
    #     r_w_file.write_file() 
    #     # 3. 也可以存入类变量供下方使用
    #     # Test_Cms.user_id = 某解析出来的ID 

    # @trace_log
    # def test_check(self):
    #     resp = req.post(url=read_ex.get_url(3), data=read_ex.get_body(3))
    #     res_json = resp.json()
        
    #     # 优化：避免使用 global，直接解析并断言
    #     # assert res_json['code'] == 200
    #     assert int(res_json['code']) == 200
    #     assert len(res_json['model']['userList']) > 0
        
    #     # 如果需要给 test_delete 用，存入类变量
    #     Test_Cms.user_id = res_json['model']['userList'][0]['id']

    # @trace_log
    # def test_delete(self):
    #     # 优先从类变量获取，如果没有再从文件读取（双重保险）
    #     id_to_del = Test_Cms.user_id or r_w_file.read_file()
        
    #     if not id_to_del:
    #         pytest.skip("没有获取到要删除的 ID，跳过此用例")
            
    #     body = {'ids': id_to_del}
    #     print(f"--- 准备删除的 ID 是: {id_to_del} ---")
        
    #     resp = req.post(url=read_ex.get_url(4), data=body)
    #     # 增加删除结果的断言
    #     # assert resp.json()['code'] == 200
    #     assert int(resp.json()['code']) == 200

    # @trace_log
    # def test_delete(self):
    #     id_value = r_w_file.read_file()
    #     body = {'ids': id_value}
    #     resp = req.post(url=read_ex.get_url(4), data=body)
        
    #     # 手动删除数据库数据，实现真正的“清理”
    #     from utils.read_sql import Connect_mysql
    #     db = Connect_mysql('127.0.0.1', 'root', 'root', 'cms_db', 3306)
    #     db.cursor.execute(f"DELETE FROM sys_user WHERE id = {id_value}")
    #     db.db_connect.commit() # 必须 commit，否则数据库不会生效！
    #     print(f"数据库中的 ID:{id_value} 已物理删除")
        
    #     return resp.json()


if __name__ == '__main__':
    # pytest.main(['-vs','test_login_add_check_delete.py'])
    pytest.main(['-vs', 'test_login_add_check_delete.py', '--alluredir', '../report/result'])
    os.system('allure serve ../report/result')

#生成报告的两种方法
    # pytest.main(['-vs','test_login_add_check_del.py','--alluredir','../report/result'])
    # import subprocess
    # subprocess.call('allure generate ../'
    #                 'report/result/ -o ../report/html --clean',shell=True)
    # subprocess.call('allure open -h 127.0.0.1 -p 8881 ../report/html',shell=True)

    # '''
    #         --alluredir：指定测试报告的生成路径；
    #     --clean-alluredir：如果已经存在报告，那就先清空，然后再生成新的测试报告；
    #         '''
    
