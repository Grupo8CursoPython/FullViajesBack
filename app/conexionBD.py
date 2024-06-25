
#Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

       
def connectionBD():
    mydb = mysql.connector.connect(
        host ="xxxxxxxx",
        user ="xxxxx",
        passwd ="xxxxxxx",
        database = "xxxxxxx"
        )
    if mydb:
        print ("Conexion exitosa a BD")
        return mydb
    else:
        print("Error en la conexion a BD")
