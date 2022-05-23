import pandas as pd
from sqlalchemy import create_engine


if __name__ =='__main__':
    mysql_username = 'root'
    mysql_password = 'loveclub123'
    # 填写真实数库ip
    mysql_ip = 'mysql.hila-development.svc.cluster.local'
    port = 3306
    data_base='m_user'
    baseSql = 'select * from t_wallet_record_'
    alist = []
    engine = create_engine(
        'mysql+pymysql://{}:{}@{}:{}/{}'.format(mysql_username, mysql_password, mysql_ip, port, data_base))
    for i in range(100):
        b=str(f'{i:02}')
        sql=baseSql+b
        df = pd.read_sql_query(sql,engine)
        alist.append(df)
        print(sql)

    df = pd.concat(alist, sort=False)
    print(df)