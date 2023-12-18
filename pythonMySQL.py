
import tkinter as tk


#importar los modulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Clientes import *

from Conection import *


class FormularioClientes :
    
    global base
    base =None
    
    global TextBoxDni
    TextBoxDni =None
    
    global TextBoxNombres
    TextBoxNombres =None
    
    global TextBoxApellidos
    TextBoxApellidos =None
    
    global TextBoxTelefono
    TextBoxTelefono =None
    
    global combo
    combo =None
    
    global groupBox
    groupBox = None
    
    global tree
    tree =None
    
    
    
    
def Formulario():
       
        global TextBoxDni
        global TextBoxNombres
        global TextBoxApellidos
        global TextBoxTelefono
        global combo
        global base
        global groupBox
        global tree
        
        
        
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
            TextBoxNombres = Entry(groupBox)
            TextBoxNombres.grid(row=1,column=1)
            
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
            
            Button(groupBox,text="Guardar", width=10,command=guardarRegistros).grid(row=5,column=0)
            Button(groupBox,text="Modificar", width=10,command=modificarRegistros).grid(row=5,column=1)
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
            
            
            #Agregar los datos a la tabla
            #Mostrar la tabla
            
            for row in CClientes.mostrarClientes():
                tree.insert("","end",values=row)
            
            #ejecutar la funcion de hacer click y mostrar el resultado en los entry
            
            tree.bind("<<TreeviewSelect>>",seleccionarRegistro)
            
            
            tree.pack()
            
            
            
            
            base.mainloop()
        
        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))


def guardarRegistros():
        
        global TextBoxDni,TextBoxNombres,TextBoxApellidos,TextBoxTelefono,combo,groupBox
        
        try:
            if TextBoxDni is None or TextBoxNombres is None or TextBoxApellidos is None or combo is None:
                print("los widget no estan inicializados")
                return
            
            dni = TextBoxDni.get()
            nombres = TextBoxNombres.get()
            apellidos = TextBoxApellidos.get()
            telefono = TextBoxTelefono.get()
            cargo = combo.get()
            
            CClientes.ingresarClientes(dni,nombres,apellidos,telefono,cargo)
            messagebox.showinfo("Información","Los datos fueron guardados")
            
            actualizarTreeView()
            
            TextBoxDni.delete(0,END)
            TextBoxNombres.delete(0,END)
            TextBoxApellidos.delete(0,END)
            TextBoxTelefono.delete(0,END)
        except ValueError as error:
            print("Error al ingresar los datos{}".format(error))
           
def actualizarTreeView():
    global tree
    
    
    try:
        #borrar todos los elementos actuales del treeview
        tree.delete(*tree.get_children())
        
        #obtener los datos que queremos mostrar
        datos = CClientes.mostrarClientes()
        
        #insertar los nuevos datos en el treeview
        for row in CClientes.mostrarClientes():
            tree.insert("","end",values=row)
    except ValueError as error:
        print("Error al actualizar la tabla {}".format(error))
                    


def seleccionarRegistro(event):
    try:
        itemseleccionado = tree.focus()
        
        if itemseleccionado:
            #obtener los valores por columnas
            values = tree.item(itemseleccionado)['values']
            
            TextBoxDni.delete(0,END)
            TextBoxDni.insert(0,values[0])
            
            TextBoxNombres.delete(0,END)
            TextBoxNombres.insert(0,values[1])
            
            TextBoxApellidos.delete(0,END)
            TextBoxApellidos.insert(0,values[2])
            
            TextBoxTelefono.delete(0,END)
            TextBoxTelefono.insert(0,values[3])
            
            combo.set(values[4])

    except ValueError as error:
        print("Error al seleccionar el registro {}".format(error))



def modificarRegistros():
        
        global TextBoxDni,TextBoxNombres,TextBoxApellidos,TextBoxTelefono,combo,groupBox
        
        try:
            if TextBoxDni is None or TextBoxNombres is None or TextBoxApellidos is None or combo is None:
                print("los widget no estan inicializados")
                return
            
            dni = TextBoxDni.get()
            nombres = TextBoxNombres.get()
            apellidos = TextBoxApellidos.get()
            telefono = TextBoxTelefono.get()
            cargo = combo.get()
            
            CClientes.modificarClientes(dni,nombres,apellidos,telefono,cargo)
            messagebox.showinfo("Información","Los datos fueron guardados")
            
            actualizarTreeView()
            
            TextBoxDni.delete(0,END)
            TextBoxNombres.delete(0,END)
            TextBoxApellidos.delete(0,END)
            TextBoxTelefono.delete(0,END)
        except ValueError as error:
            print("Error al modificar los datos{}".format(error))

Formulario()        