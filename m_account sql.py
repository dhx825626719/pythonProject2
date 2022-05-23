import pandas as pd
from sqlalchemy import create_engine


if __name__ =='__main__':
    mysql_username = 'root'
    mysql_password = 'loveclub123'
    # 填写真实数库ip
    mysql_ip = 'mysql.hila-development.svc.cluster.local'
    port = 3306
    data_base='m_user_'
    baseSql = 'select * from t_user_'
    alist = []
    for i in range(0x10):
        i=str(f'{i:x}')
        database=data_base+i
        print(database)
        engine = create_engine(
            'mysql+pymysql://{}:{}@{}:{}/{}'.format(mysql_username, mysql_password, mysql_ip, port, database))
        for a in range(0x10):
            a=str(f'{a:x}')
            b=i+a
            sql=baseSql+b
            df = pd.read_sql_query(sql,engine)
            alist.append(df)

    df = pd.concat(alist, sort=False)
    print(df)