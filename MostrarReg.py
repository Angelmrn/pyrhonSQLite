import sqlite3
conexion = sqlite3.connect('EjemploBDD.db')

c = conexion.cursor()
c.execute("SELECT *FROM acciones")

registros = c.fetchall()

for acciones in registros:
    print(registros)


conexion.close()