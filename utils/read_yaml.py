from common.public_path import read_path
import yaml


class Read_Yaml():
    def read_list(self,filedir,filename):
        """读取有yaml文件为列表格式"""
        with open(read_path(filedir,filename),'r',encoding='utf-8') as file_r:
            return list(yaml.safe_load_all(file_r))
        
    def read_dict(self,filedir,filename):
        """读取yaml文件为字典格式"""
        with open(read_path(filedir,filename),'r',encoding='utf-8') as file_r:
            return yaml.safe_load(file_r)
            
if __name__ == '__main__':
    read_y = Read_Yaml()
    # print(read_y.read_list('data','login.data'))
    print(read_y.read_dict('data','data.yaml')['case_001_login'])

