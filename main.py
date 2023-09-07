import psycopg2

conexao = psycopg2.connect(database="postgres",
    host="localhost",
    user="postgres",
    password="512834",
    port="5432"
)

print(conexao.info)