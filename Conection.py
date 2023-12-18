import mysql.connector

class CConexion:
    
    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root',password='eLeanor22',
                                               host='127.0.0.1',
                                               database='pontocodb',
                                               port='3306')
            print("conexion correcta")
            
            return conexion
            
            
        except mysql.connector.Error as error:
            print("Error al conectarte en la base de datos {}".format(error))
            
            return conexion
        
    ConexionBaseDeDatos()