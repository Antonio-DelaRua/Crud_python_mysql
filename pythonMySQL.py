
import tkinter as tk


#importar los modulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox


class FormularioClientes :
    
    def Formulario():
        try:
            base = Tk()
            base.geometry("1600x300")
            base.title("ARL PONTOCO")
            
            groupBox = LabelFrame(base, text="Datos Del Personal", padx=5,pady=5)
            groupBox.grid(row=0,column=0,padx=10,pady=10)
            
            labelDni=Label(groupBox,text="DNI:",width=13, font=("arial",12)).grid(row=0,column=0)
            TextBoxDni = Entry(groupBox)
            TextBoxDni.grid(row=0,column=1)
            
            labelNombre=Label(groupBox,text="Nombre:",width=13, font=("arial",12)).grid(row=1,column=0)
            TextBoxNombre = Entry(groupBox)
            TextBoxNombre.grid(row=1,column=1)
            
            labelApellidos=Label(groupBox,text="Apellidos:",width=13, font=("arial",12)).grid(row=2,column=0)
            TextBoxApellidos = Entry(groupBox)
            TextBoxApellidos.grid(row=2,column=1)
            
            labelTelefono=Label(groupBox,text="Telefono:",width=13, font=("arial",12)).grid(row=3,column=0)
            TextBoxTelefono = Entry(groupBox)
            TextBoxTelefono.grid(row=3,column=1)
            
            labelCargo=Label(groupBox,text="Cargo:",width=13, font=("arial",12)).grid(row=4,column=0)
            seleccionCargo = tk.StringVar()
            combo = ttk.Combobox(groupBox,values=["Peon","Oficial","encargado","thefuckingBOSS"],textvariable=seleccionCargo)
            combo.grid(row=4,column=1)
            seleccionCargo.set("Peon")
            
            Button(groupBox,text="Guardar", width=10).grid(row=5,column=0)
            Button(groupBox,text="Modificar", width=10).grid(row=5,column=1)
            Button(groupBox,text="Eliminar", width=10).grid(row=5,column=2)
            
            groupBox = LabelFrame(base,text="Lista de trabajadores", padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            
            #Crear un Treeview
            
            #Configurar las columnas
            
            tree = ttk.Treeview(groupBox,columns=("DNI","Nombres","apellidos","telefonos","Cargo"), show='headings',height=5,)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1",text="DNI")
            
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2",text="Nombres")
            
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3",text="Apellidos")
            
            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4",text="Telefonos")
            
            tree.column("# 5", anchor=CENTER)
            tree.heading("# 5",text="Cargo")
            
            
            
            
            
            
            tree.pack()
            
            
            
            
            base.mainloop()
        
        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))


    Formulario()        