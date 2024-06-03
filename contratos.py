import sqlite3
import pandas as pd
from docx import Document

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

columnas = ['fecha_ingreso', 'residencia', 'rut', 'nombre_completo', 'nacionalidad','fecha_de_nacimiento', 'profesion', 'fecha_de_nacimiento', 'id_rol','Rol', 'Sueldo']
df = pd.DataFrame(records, columns=columnas)

def personas(df, persona_id):
    personas_dt = df.iloc[int(persona_id)-1]
    return personas_dt

persona_id = input('Ingrese el id de la persona: ')
personas_dt = personas(df, persona_id)
print(personas_dt)

def contratos(personas_datos):
    documento = Document()
    
    documento.add_heading('Contrato de Trabajo', level=1)
    documento.add_paragraph(f"Nombre: {personas_datos['nombre_completo'].values[0]}")
    documento.add_paragraph(f"profesion: {personas_datos['profesion'].values[0]}")
    documento.save('contrato.docx')

    contratos(personas_datos)