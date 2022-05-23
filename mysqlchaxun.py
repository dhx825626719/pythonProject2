import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:loveclub123@mysql.hila-development.svc.cluster.local/m_user')

alist = []
baseSql='select * from t_wallet_record_'
for i in range(100):
    i=str(f'{i:02}')
    sql=baseSql+i
    df = pd.read_sql_query(sql, engine)
    alist.append(df)

df = pd.concat(alist, sort=False)
print(df)
df.to_sql('t_wallet_record_all', con=engine, if_exists='append', index=False)