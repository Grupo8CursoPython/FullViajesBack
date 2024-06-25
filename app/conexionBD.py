
#Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

#def connectionBD():
#   mydb = mysql.connector.connect(
#       host ="http://127.0.0.1",
#       user ="izquierdow",
#        passwd ="Neopotenza9000*",
#        database = "ddbbback"
#        )
#   if mydb:
#        print ("Conexion exitosa a BD")
#        return mydb
#   else:
#        print("Error en la conexion a BD")
        
def connectionBD():
    mydb = mysql.connector.connect(
        host ="mysql-grupo8python.alwaysdata.net",
        user ="366420",
        passwd ="Curso8Python",
        database = "grupo8python_ddbb_ti02"
        )
    if mydb:
        print ("Conexion exitosa a BD")
        return mydb
    else:
        print("Error en la conexion a BD")

#Importando Libreria mysql.connector para conectar Python con MySQL
#import mysql.connector

#def connectionBD():
#    mydb = mysql.connector.connect(
#        host ="izquierdow.mysql.pythonanywhere-services.com",
#        user ="izquierdow",
#        passwd ="Neopotenza9000*",
#        database = "izquierdow$default"
#        )
#    if mydb:
#        print ("Conexion exitosa a BD")
#        return mydb
#    else:
#        print("Error en la conexion a BD")
