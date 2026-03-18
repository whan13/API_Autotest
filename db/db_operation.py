import pymysql

class DBOperation:
    def __init__(self):
        # 这里的配置建议以后抽离到 config.ini 中
        self.config = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "root",
            "database": "cms_db",
            "charset": "utf8mb4",
            "autocommit": True  # 自动提交，删除操作必须开启或手动 commit
        }
        self.conn = None
        self.cursor = None

    def connect(self):
        """建立连接"""
        self.conn = pymysql.connect(**self.config)
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def delete_user(self, user_id):
        """
        根据 ID 删除用户
        :param user_id: 用户 ID
        :return: 受影响的行数 (int)
        """
        if not user_id:
            return 0
            
        sql = "DELETE FROM users WHERE id = %s"
        try:
            self.connect()
            rows = self.cursor.execute(sql, (user_id,))
            print(f"[DB] 执行删除 SQL: {sql} % {user_id}, 影响行数: {rows}")
            return rows
        except Exception as e:
            print(f"[DB] 删除失败: {e}")
            return 0
        finally:
            self.close()

    def close(self):
        """关闭连接"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

# 在模块末尾实例化，这样其他文件 import db 就能直接用
db = DBOperation()