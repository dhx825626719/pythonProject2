import pymysql
import pandas as pd
from sshtunnel import SSHTunnelForwarder

def con_sql(db, sql):
    # 创建连接
    ssh_host = "129.226.192.68"  # 堡垒机ip地址或主机名
    ssh_port = 44445  # 堡垒机连接mysql服务器的端口号，一般都是22，必须是数字
    ssh_user = "root"  # 这是你在堡垒机上的用户名
    ssh_password = "Qwer1234%^&*"  # 这是你在堡垒机上的用户密码
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_password=ssh_password,
            remote_bind_address=('10.210.0.17', 3306)) as server:
        db = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user='hilaadmin', passwd='DTSA2F4fc5eAI28x',db='m_user', charset='utf8')
    # 创建游标
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # 执行结果转化为dataframe
    df = pd.DataFrame(list(result))
    # 关闭连接
    db.close()
    # 返回dataframe
    return df

db = 'm_user'
baseSql = 'select * from t_wallet_record_'
alist=[]

for i in range(100):
    b = str(f'{i:02}')
    sql = baseSql + b
    result = con_sql(db, sql)
    alist.append(result)
    print(sql)

df = pd.concat(alist, sort=False)
print(df)

