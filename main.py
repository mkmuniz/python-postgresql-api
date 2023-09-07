import psycopg2
import pandas as pd

conexao = psycopg2.connect(database="postgres",
    host="localhost",
    user="postgres",
    password="512834",
    port="5432"
)

cursor = conexao.cursor()
cursor.execute('SELECT * FROM users')

dados = cursor.fetchall()
colunas = []

for col in cursor.description:
    colunas.append(col[0])

df_users = pd.DataFrame(data = dados, columns = colunas)

print(df_users)
