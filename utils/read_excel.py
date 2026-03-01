# -*- coding: utf-8 -*-
"""
@Time:2021/8/23 11:14
@Auth: wanghan
@QQ :346606022
@WeChat :wanghan960501
"""
import xlrd
from common.public_path import read_path
from utils.read_yaml import Read_Yaml
read_ya=Read_Yaml()#实例化读取yaml文件的类

"""读取Excel表格的数据"""

class Read_Excel():
    def __init__(self):
        self.case_id=0
        self.url=2
        self.method=3
        self.data=4
        self.case_except=5

    def get_sheet(self):
        self.sheet=xlrd.open_workbook(read_path('data','Data.xlsx'))
        self.sheet_value=self.sheet.sheet_by_index(0)
        return self.sheet_value#获取页签

    def get_value(self,rows,cols):
        """获取单元格"""
        return self.get_sheet().cell_value(rows,cols)

    def get_case_id(self,row):
        """获取单元格"""
        return self.get_value(row,self.case_id)

    def get_url(self,row):
        """获取url"""
        return self.get_value(row,self.url)

    def get_method(self,row):
        """获取请求方法"""
        return self.get_value(row,self.method)

    def get_data(self,row):
        """获取请求参数位置"""
        return self.get_value(row,self.data)

    def get_body(self,row):
        """通过get_data映射获取---请求参数body"""
        # print(read_ya.read_dict('data','data.yaml')['case_001_login'])
        return (read_ya.read_dict('data','data.yaml')[self.get_data(row)])

    def get_except(self,row):
        """获取预期结果"""
        return self.get_value(row,self.case_except)


if __name__ == '__main__':
    read_e=Read_Excel()
    # read_e.get_sheet()
    # print(read_e.get_url(1))
    # print(read_e.get_method(1))
    print(read_e.get_body(1))