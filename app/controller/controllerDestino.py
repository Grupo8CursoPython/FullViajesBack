from random import sample
from conexionBD import *  #Importando conexion BD
from mysql.connector import Error



#Creando una funcion para obtener la lista de Destinos
#def listaDestinos():
#    #creando mi instancia a la conexion de BD
#    conexion_MySQLdb = connectionBD()

#    cur = conexion_MySQLdb.cursor(dictionary=True)

#    querySQL = "SELECT * FROM destinos ORDER BY id DESC"
#    cur.execute(querySQL) 
#    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
#    totalBusqueda = len(resultadoBusqueda) #Total de busqueda para paginacion
#    cur.close() #Cerrando conexion SQL
#    conexion_MySQLdb.close() #cerrando conexion de la BD
#    return resultadoBusqueda

def listaDestinos():
    conexion_MySQLdb = connectionBD()
    
    if conexion_MySQLdb is None:
        print("No se pudo conectar a la base de datos")
        return []

    try:
        cur = conexion_MySQLdb.cursor(dictionary=True)
        querySQL = "SELECT * FROM destinos ORDER BY id DESC"
        cur.execute(querySQL)
        resultadoBusqueda = cur.fetchall()  # Obtener todos los registros
        return resultadoBusqueda
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return []
    finally:
        if conexion_MySQLdb.is_connected():
            cur.close()  # Cerrando cursor
            conexion_MySQLdb.close()  # Cerrando conexión

# Llamada a la función para verificar que funciona correctamente
destinos = listaDestinos()
print(destinos)


def updateDestino(id=''):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM destinos WHERE id = %s LIMIT 1", [id])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
    
    
def registrarDestino(titulo='', descripcion='', plan='', preciofull='', preciodes='', favorito='', nuevoNombreFile=''):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO destinos(titulo,descripcion, plan, preciofull, preciodes, favorito, foto) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        valores     = (titulo, descripcion, plan, preciofull, preciodes, favorito, nuevoNombreFile)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        ultimo_id        = cursor.lastrowid #retorna el id del ultimo registro
        return resultado_insert
 

def detallesdelDestino(idDestino):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        print = '%s'
        
        cursor.execute("SELECT * FROM destinos WHERE id ='%s'" % (idDestino,))
        resultadoQuery = cursor.fetchone()
        cursor.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        return resultadoQuery
    
def  recibeActualizarDestino(titulo, descripcion, plan, preciofull, preciodes, favorito, nuevoNombreFile, idDestino):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("""
            UPDATE destinos
            SET 
                titulo       = %s,
                descripcion  = %s,
                plan         = %s,
                preciofull   = %s,
                preciodes    = %s,
                favorito     = %s,
                foto         = %s
            WHERE id=%s
            """, (titulo,descripcion, plan, preciofull, preciodes, favorito, nuevoNombreFile,  idDestino))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update
 

#Crear un string aleatorio para renombrar la foto 
# y evitar que exista una foto con el mismo nombre
def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio