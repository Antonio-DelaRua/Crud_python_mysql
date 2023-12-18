from Conection import *

class CClientes:
    
    def mostrarClientes():
        try:
         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         cursor.execute("select * from clientes;")
         miResultado = cursor.fetchall()
         cone.commit()
         cone.close()
         return miResultado
         
        
            
            
        except mysql.connector.Error as error:
            print("error de Mostrar datos {}".format(error))
            
        
        
        
        
        
        
    
    def ingresarClientes(dni,nombres,apellidos,telefono,cargo):
        try:
         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         sql ="insert into clientes values(%s,%s,%s,%s,%s);"
         valores = (dni,nombres,apellidos,telefono,cargo)
         cursor.execute(sql,valores)
         cone.commit()
         print(cursor.rowcount,"Registro ingresado")
         cone.close()
         
        
            
            
        except mysql.connector.Error as error:
            print("error de ingreso de datos {}".format(error))
            
            
    def modificarClientes(dni, nombres, apellidos, telefono, cargo):
     try:
        cone = CConexion.ConexionBaseDeDatos()
        cursor = cone.cursor()
        sql = "UPDATE clientes SET nombres = %s, apellidos = %s, telefono = %s, cargo = %s WHERE dni = %s"
        valores = (nombres, apellidos, telefono, cargo, dni)
        cursor.execute(sql, valores)
        cone.commit()
        print(cursor.rowcount, "Registro actualizado")
        cone.close()

     except mysql.connector.Error as error:
        print("Error de actualización de datos: {}".format(error))
        
        
    def eliminarClientes(dni):
     try:
        cone = CConexion.ConexionBaseDeDatos()
        cursor = cone.cursor()
        sql = "DELETE FROM clientes WHERE dni = %s;"
        valores = (dni,)
        cursor.execute(sql, valores)
        cone.commit()
        print(cursor.rowcount, "Registro eliminado")
        cone.close()

     except mysql.connector.Error as error:
        print("Error de eliminacion de datos: {}".format(error))