import sqlite3

conexion = sqlite3.connect('Ejemplo.db')
c = conexion.cursor()
c.execute('''CREATE TABLE acciones (fechas text, Operacion text, Simbolo text, Cantidad real, Precio real)''')

c.execute("INSERT INTO acciones VALUES ('25/nov/2016', 'compra', 'INV', 100, 15.43)")
c.execute("INSERT INTO acciones VALUES ('03/dic/2016', 'venta', 'INV', 96, 14.30)")
c.execute("INSERT INTO acciones VALUES ('20/dic/2016', 'venta', 'INV', 120, 10.50)")
c.execute("INSERT INTO acciones VALUES ('10/ene/2017', 'compra', 'INV', 100, 5.43)")
c.execute("INSERT INTO acciones VALUES ('27/ene/2017', 'venta', 'INV', 30, 20.03)")

conexion.commit()
conexion.close()