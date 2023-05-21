import sqlite3

conexion = sqlite3.connect('Ejemplo.db')
c = conexion.cursor()

op = ('venta',)

for row in c.execute('SELECT *FROM acciones WHERE Operacion =?', op):
    print(row)

conexion.close()