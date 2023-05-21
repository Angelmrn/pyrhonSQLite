import sqlite3

conexion = sqlite3.connect('Ejemplo.db')
c = conexion.cursor()
c.execute('''CREATE TABLE acciones (fechas text, Operacion text, Simbolo text, Cantidad real, Precio real)''')

c.execute("INSERT INTO acciones VALUES ('24/nov/2016', 'compra', 'INV', 100, 15.43)")


conexion.commit()
conexion.close()
