from tkinter import *
from tkinter import ttk
import csv
import sqlite3


class datos:
    def __init__(self,raiz):
        #VARIABLES

        self.raiz = Tk()
        
        principal=ttk.Frame(raiz)
        principal.grid()
        principal=ttk.Frame(raiz)
        principal.grid()
        
        Nombre = StringVar()
        AParerno = StringVar()
        AMaterno = StringVar()
        Correo = StringVar()
        Movil = StringVar()
        estado = StringVar()
        raiz.title("Muestra Widgets")
    
        #ESTADOS
        self.estado = StringVar()
        comboEstados = ttk.Combobox(principal, textvariable=self.estado)
        comboEstados.grid(column=1, row= 10)
        comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan")

        #RADIOBUTTON
        self.ocupacion=StringVar()

        emple = ttk.Frame(principal, padding="10 10 10 10")
        emple.grid(column= 1, row= 2)

        Estudiante = ttk.Radiobutton(emple, text="Estudiante",value='Estudiante',variable=self.ocupacion).grid(column=5,row=1, sticky=(W))
        Empleado = ttk.Radiobutton(emple, text="Empleado", value='Empleado',variable=self.ocupacion).grid(column=5,row=2,pady=5, sticky=(W))
        Desempleado = ttk.Radiobutton(emple, text="Desempleado",value='Desempleado', variable=self.ocupacion).grid(column=5,row=3,pady=5, sticky=(W))
       

        #CHECKBOTTON
        self.afi=StringVar()
        self.afi2=StringVar()
        self.afi3=StringVar()

        Aficiones = ttk.Frame(principal, padding="10 10 30 30",relief="raised")
        Aficiones.grid(column=0, row=9, rowspan=5)
        Leer = ttk.Checkbutton(Aficiones, text="Leer", variable=self.afi)
        Leer.grid(column=0,row=0)
        Musica = ttk.Checkbutton(Aficiones, text="Musica", variable=self.afi2)
        Musica.grid(column=1,row=0)
        VideoJuegos = ttk.Checkbutton(Aficiones, text="VideoJuegos", variable=self.afi3)
        VideoJuegos.grid(column=2,row=0)


        #FRAME BOTONES
        botones = ttk.Frame(principal, padding="10 10 10 10")
        botones.grid(column=0, row=20)

        btnCancelar = ttk.Button(botones, text="Cancelar", command=self.Cerrar)
        btnCancelar.grid(column=1,row=1)

    
        self.Nombre=StringVar()
        self.AParerno=StringVar()
        self.AMaterno=StringVar()
        self.Correo=StringVar()
        self.Movil=StringVar()
        self.Leer=StringVar()
        self.Musica=StringVar()
        self.VideoJuegos=StringVar()

        Usuario = ttk.Frame(principal, padding="10 10 10 10", relief="raised")
        Usuario.grid(column=0, row=1,rowspan=5)

        Nombre = ttk.Entry(Usuario, width=30, textvariable=self.Nombre)
        Nombre.grid(column=1, row=0)

        AParerno = ttk.Entry(Usuario, width=30, textvariable=self.AParerno)
        AParerno.grid(column=1, row=1)
        AMaterno = ttk.Entry(Usuario, width=30, textvariable=self.AMaterno)
        AMaterno.grid(column=1, row=2)
        Correo = ttk.Entry(Usuario, width=30, textvariable=self.Correo)
        Correo.grid(column=1, row=3)
        Movil = ttk.Entry(Usuario, width=30, textvariable=self.Movil)
        Movil.grid(column=1, row=4)

        ttk.Label(Usuario, text="Nombre").grid(column=0, row=0, pady=20)
        ttk.Label(Usuario, text="A.Paterno").grid(column=0, row=1, pady=20)
        ttk.Label(Usuario, text="A.Materno").grid(column=0, row=2,pady=20)
        ttk.Label(Usuario, text="Correo").grid(column=0, row=3,pady=20)
        ttk.Label(Usuario, text="Movil").grid(column=0, row=4,pady=20)
        #BOTONES
        btnGuardar = ttk.Button(botones, text="Guardar", command=self.guardar).grid(column=0,row=1)
        btnmostrar=ttk.Button(botones,text="Ver datos",command=self.ver_datos).grid(column=0, row=2)
        btnBDD=ttk.Button(botones, text="BDD",command=self.baseDatos).grid(column=1,row=2)
    

        self.raiz.mainloop()
        
    def guardar(self):
            print("Boton GUARDAR presionado")
            nomUsuario = self.Nombre.get()
            apPaternoUsu = self.AParerno.get()
            apMaternoUsu = self.AMaterno.get() 
            correoUsuario = self.Correo.get()
            movilUsu = self.Movil.get()

            Aficiones = self.afi.get()
            Aficiones2=self.afi2.get()
            Aficiones3=self.afi3.get()
            Ocupaciones = self.ocupacion.get()
            Estado = self.estado.get()
    
           


            with open("info.csv", "a", newline="") as archivo:

            # Abrimos el archivo en modo escritura
                escritor = csv.writer(archivo)
            # Si el archivo está vacío escribimos la primera línea con los encabezados
                if archivo.tell() == 0:
                    escritor.writerow(['Nombre','A_paterno','A_materno','Correo','Movil','Leer','Musica','Videojuegos','Estado','Ocupacion'])
            # Escribimos los datos del formulario en una nueva línea
                escritor.writerow([nomUsuario, apPaternoUsu, apMaternoUsu, correoUsuario, movilUsu, Aficiones, Aficiones2, Aficiones3, Estado, Ocupaciones])
         

    def Cerrar(self):
         self.raiz.destroy
            
    def ver_datos(self):
        ventana = Toplevel(self.raiz)
        ventana.title("Datos almacenados")
        
        with open("info.csv", mode="r") as file:
            lector = csv.reader(file)

            # Creamos la tabla utilizando un LabelFrame y Labels
            table_frame = ttk.LabelFrame(ventana, text='Datos')
            table_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

            row_num = 0
            for row in lector:
                label_1 = ttk.Label(table_frame, text=row[0], width=20, borderwidth=1, relief='solid')
                label_1.grid(row=row_num, column=0)
                
                label_2 = ttk.Label(table_frame, text=row[1], width=20, borderwidth=1, relief='solid')
                label_2.grid(row=row_num, column=1)
                
                label_3 = ttk.Label(table_frame, text=row[2], width=20, borderwidth=1, relief='solid')
                label_3.grid(row=row_num, column=2)

                label_4 = ttk.Label(table_frame, text=row[3], width=20, borderwidth=1, relief='solid')
                label_4.grid(row=row_num, column=3)
                
                label_5 = ttk.Label(table_frame, text=row[4], width=20, borderwidth=1, relief='solid')
                label_5.grid(row=row_num, column=4)
                
                label_6 = ttk.Label(table_frame, text=row[5], width=20, borderwidth=1, relief='solid')
                label_6.grid(row=row_num, column=5)

                label_7 = ttk.Label(table_frame, text=row[6], width=20, borderwidth=1, relief='solid')
                label_7.grid(row=row_num, column=6)
                
                label_8 = ttk.Label(table_frame, text=row[7], width=20, borderwidth=1, relief='solid')
                label_8.grid(row=row_num, column=7)
                
                label_9 = ttk.Label(table_frame, text=row[8], width=20, borderwidth=1, relief='solid')
                label_9.grid(row=row_num, column=8)

                label_10 = ttk.Label(table_frame, text=row[9], width=20, borderwidth=1, relief='solid')
                label_10.grid(row=row_num, column=9)

                row_num += 1


    
    def baseDatos (self):
            conexion = sqlite3.connect('formulario.db')
            c= conexion.cursor()

            nomUsuario = self.Nombre.get()
            apPaternoUsu = self.AParerno.get()
            apMaternoUsu = self.AMaterno.get() 
            correoUsuario = self.Correo.get()
            movilUsu = self.Movil.get()
            #Aficiones
            Aficiones = self.afi.get()
            Aficiones2=self.afi2.get()
            Aficiones3=self.afi3.get()
            #Ocupaciones
            Ocupaciones = self.ocupacion.get()
            Estado = self.estado.get()

            lista=[(nomUsuario, apPaternoUsu, apMaternoUsu, correoUsuario, movilUsu, Aficiones, Aficiones2, Aficiones3, Ocupaciones, Estado)]

            c.executemany('INSERT INTO info VALUES (?,?,?,?,?,?,?,?,?,?)', lista)
            conexion.commit()
            for row in c.execute("SELECT * FROM info"):
                print("Datos ingresados a la BDD: ", row)

            conexion.close()
            

        