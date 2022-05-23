import pymysql
import pandas as pd
from sshtunnel import SSHTunnelForwarder
import datetime


class MySqlSSH:
    def __init__(self,db):
        self.server = SSHTunnelForwarder(
            ("129.226.192.68", 44445),  # ssh IP和port
            ssh_password="Qwer1234%^&*",  # ssh 密码
            ssh_username="root",  # ssh账号
            local_bind_address=('127.0.0.1', 3306),  # 这里必须填127.0.0.1
            remote_bind_address=("10.210.0.17", 3306))  # 数据库所在的IP和端口
        # 启动服务
        self.server.start()
        host = "127.0.0.1"  # 必须为127.0.0.1
        user = "hilaadmin"
        password = "DTSA2F4fc5eAI28x"
        port = 3306
        self.mysql = pymysql.connect(host=host, user=user, password=password,db=db, port=port)
        self.cursor = self.mysql.cursor()

    def fetch_one(self, sql):
        # 执行SQL
        self.cursor.execute(sql)
        # 查看结果
        result = self.cursor.fetchone()
        return result

    def fetch_all(self, sql):
        # 执行SQL
        self.cursor.execute(sql)
        # 查看结果
        result = self.cursor.fetchall()
        return result

    def close(self):
        self.cursor.close()  # 关闭查询
        self.mysql.close()
        self.server.close()  # 关闭服务


if __name__ == '__main__':
    start = datetime.datetime.now()

    data_base='m_user_'
    baseSql = 'select * from t_user_'
    alist = []
    for i in  range (0x10):
        i=str(f'{i:x}')
        database=data_base+i
        print(database)
        My=MySqlSSH(database)
        for a in range(0x10):
            b = str(f'{a:x}')
            sql = baseSql + i + b
            result = pd.DataFrame(My.fetch_all(sql))
            alist.append(result)
            print(sql)
df = pd.concat(alist, sort=False)
print(df)
My.close()
end = datetime.datetime.now()
print(end - start)

