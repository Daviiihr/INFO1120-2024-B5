import sqlite3
import pandas as pd

conn = sqlite3.connect('db_personas.db')
cursor = conn.cursor()
query = """
    SELECT * 
    FROM personas
    INNER JOIN salarios ON personas.id_rol = salarios.id_salarios
"""
cursor.execute(query)
records = cursor.fetchall()

df = pd.read_sql_query(query, conn)
conn.close()

columnas = ['Id_rol', 'nombre_completo', 'profesion', 'rut', 'residencia','fecha_ingreso', 'nacionalidad', 'fecha_de_nacimiento', 'id_salarios','Rol', 'Sueldo']
df = pd.DataFrame(records, columns=columnas)

print(df)