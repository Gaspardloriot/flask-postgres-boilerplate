from sqlalchemy import create_engine
import psycopg2
import pandas as pd

engine = create_engine('postgresql://gitpod@localhost/postgres')
print('reading df')
df = pd.read_excel('./tc1_alpha_filtered.xlsx')
print('df to excel')
df.to_sql('test',engine)
print('done')