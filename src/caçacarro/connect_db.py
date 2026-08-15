import os

import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()

def insert_marcas(marcas_de_carro):
    conn = psycopg2.connect(
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASS"],
        host=os.environ["POSTGRES_HOST"],
        port=os.environ["POSTGRES_PORT"]
        )

    cur = conn.cursor()

    table_name = "marcas"
    cur.execute(
    sql.SQL("INSERT INTO {} (marca) VALUES (%s)").format(sql.Identifier(table_name)),
    (marcas_de_carro,)
    )
    print("inserted ")
    conn.commit()

    cur.close()
    conn.close()

