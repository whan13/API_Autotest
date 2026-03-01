
"""读写或写入内容到文件"""
from db.read_sql_id import Read_Sql_ID
from common.public_path import read_path

read_sql=Read_Sql_ID()
class Read_Write_File():
    def write_file(self):
        id_value=read_sql.read_id('select * from sys_user where id in (select max(id) from sys_user)')[0][0]
        # print(id_value)
        with open(read_path('config','user_id.txt'),'w',encoding='utf-8') as file_w:
            file_w.write(str(id_value))

    def read_file(self):
        with open(read_path('config','user_id.txt'),'r',encoding='utf-8') as file_r:
            user_id=file_r.read()
            return user_id

if __name__ == '__main__':
    r_w_file=Read_Write_File()
    r_w_file.write_file()
    print(r_w_file.read_file())

