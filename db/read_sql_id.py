
from utils.read_sql import Connect_mysql
from utils.read_yaml import Read_Yaml
read_ya=Read_Yaml()
class Read_Sql_ID():
    def read_id(self,sql):
        id_v=read_ya.read_dict('config','mysql_login_data.yaml')
        connect_sql=Connect_mysql(host=id_v['host'],user=id_v['user'],password=id_v['password'],db=id_v['db'],port=id_v['port'])
        return connect_sql.select_sql(sql)

if __name__ == '__main__':
    read_sqlid=Read_Sql_ID()
    print(read_sqlid.read_id('select * from sys_user where id in (select max(id) from sys_user)')[0][0])

