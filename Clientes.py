from Conection import *

class CClientes:
    
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