import psycopg2

DB_NAME = "ezkjriuo"
DB_USER = "ezkjriuo"
DB_PASS = "hf1DQn1u37Uf7xcQ1lAk-MVa7FLdsheG"
DB_HOST = "hattie.db.elephantsql.com"
DB_PORT = "5432" #default port for postgres


conn = psycopg2.connect(database = DB_NAME,
                        user = DB_USER,
                        password = DB_PASS,
                        host = DB_HOST,
                        port = DB_PORT)

print("Database connected successfully")

cur = conn.cursor()

cur.execute("""
    SELECT
        ID, NAME, EMAIL
    FROM
        Employee
""")

rows = cur.fetchall()

for data in rows:
    print("ID : " + str(data[0]))
    print("Name : " + str(data[1]))
    print("Email : " + str(data[2]))


print("Data selected successfully")
conn.close()