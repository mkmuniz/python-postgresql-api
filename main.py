import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import os 
from dotenv import load_dotenv, dotenv_values

load_dotenv()

conexao = psycopg2.connect(os.getenv('DATABASE_NAME'),
    host=os.getenv('DATABASE_HOST'),
    user=os.getenv('DATABASE_USER'),
    password=os.getenv('DATABASE_PASSWORD'),
    port=os.getenv('DATABASE_PORT')
)

cursor = conexao.cursor()
cursor.execute('SELECT * FROM users')

dados = cursor.fetchall()
colunas = []

for col in cursor.description:
    colunas.append(col[0])

df_users = pd.DataFrame(data = dados, columns = colunas)

plt.bar(df_users['column_name'], df_users['column_name'])
plt.show()

plt.pie(df_users['column_name'], labels=df_users['column_name'])
plt.show()
