import pymysql

class Connect_mysql():
    def __init__(self,host,user,password,db,port):
        try:
            self.db_connect = pymysql.connect(host=host,user=user,password=password,db=db,port=port)
            self.cursor = self.db_connect.cursor()
        except Exception as e:
            print('连接数据库异常',e)

    def select_sql(self,sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print('查询异常',e)

        finally:
            self.cursor.close()
            self.db_connect.close()

if __name__ == '__main__':
    con_sql=Connect_mysql('127.0.0.1','root','root','cms_db',3306)
    print(con_sql.select_sql('select * from sys_user where id in (select max(id) from sys_user)'))
