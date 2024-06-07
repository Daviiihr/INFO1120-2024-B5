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

def generar_multiples_contratos(df: pd.DataFrame, start: int, end: int):
    sub_df = df.iloc[start:end]
    contratos = []
    for i in range(start, end):
        contrato = dt.singular_data_to_contract(df, i)
        contratos.append(contrato)
    return contratos

start = int(input('Ingrese el id de la primera persona: '))
end = int(input('Ingrese el id de la última persona: '))
word_contrato = dt.singular_data_to_contract(df, int(persona_id)-1)
contratos = generar_multiples_contratos(df, start, end, word_contrato)
for contrato in contratos:
    print(contrato)