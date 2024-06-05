import sqlite3
import pandas as pd
from docx import Document
import word_gen as wd
import data as dt
import os

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

columnas = ['fecha_ingreso', 'residencia', 'rut', 'nombre_completo', 'nacionalidad','fecha_de_nacimiento', 'profesion', 'id_salarios', 'id_rol','Rol', 'Sueldo']
df = pd.DataFrame(records, columns=columnas)

def personas(df, persona_id):
    personas_dt = df.iloc[int(persona_id)-1]
    return personas_dt

persona_id = input('Ingrese el id de la persona: ')
personas_dt = personas(df, persona_id)
print(personas_dt)
word_contrato = dt.singular_data_to_contract(df, int(persona_id)-1)
print(word_contrato)

word_contrato = Document()
nombre_completo = personas_dt['nombre_completo']
ruta_carpeta = 'contratos_carpeta'
nombre_archivo = f'{nombre_completo}.docx'
ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
word_contrato.save(ruta_completa)