import sqlite3
import pandas as pd

conn = sqlite3.connect('db_personas.db')
query = """SELECT * FROM personas"""

df = pd.read_sql_query(query, conn)
conn.close()

print(df)