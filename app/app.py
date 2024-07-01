from flask import Flask, render_template, request, redirect, url_for, jsonify
from controller.controllerDestino import *


#Para subir archivo tipo foto al servidor
import os
from werkzeug.utils import secure_filename 


#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app

msg  =''
tipo =''


#Creando mi decorador para el home, el cual retornara la Lista de Destinos
@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('public/layout.html', miData = listaDestinos())

#RUTAS
@app.route('/registrar-destino', methods=['GET','POST'])
def addDestino():
    return render_template('public/acciones/add.html')


 
#Registrando nuevo Destibo
@app.route('/destino', methods=['POST'])
def formAddDestino():
    if request.method == 'POST':
        titulo               = request.form['titulo']
        descripcion          = request.form['descripcion']
        plan                 = request.form['plan']
        preciofull           = request.form['preciofull']
        preciodes            = request.form['preciodes']
        favorito             = request.form['favorito']
        
        
        if(request.files['foto'] !=''):
            file     = request.files['foto'] #recibiendo el archivo
            nuevoNombreFile = recibeFoto(file) #Llamado la funcion que procesa la imagen
            resultData = registrarDestino(titulo, descripcion, plan, preciofull, preciodes, favorito, nuevoNombreFile)
            if(resultData ==1):
                return render_template('public/layout.html', miData = listaDestinos(), msg='El Registro fue un éxito', tipo=1)
            else:
                return render_template('public/layout.html', msg = 'Metodo HTTP incorrecto', tipo=1)   
        else:
            return render_template('public/layout.html', msg = 'Debe cargar una foto', tipo=1)
            


@app.route('/form-update-destino/<string:id>', methods=['GET','POST'])
def formViewUpdate(id):
    if request.method == 'GET':
        resultData = updateDestino(id)
        if resultData:
            return render_template('public/acciones/update.html',  dataInfo = resultData)
        else:
            return render_template('public/layout.html', miData = listaDestinos(), msg='No existe el Destino', tipo= 1)
    else:
        return render_template('public/layout.html', miData = listaDestinos(), msg = 'Metodo HTTP incorrecto', tipo=1)          
 
   
  
@app.route('/ver-detalles-del-destino/<int:idDestino>', methods=['GET', 'POST'])
def viewDetalleDestino(idDestino):
    msg =''
    if request.method == 'GET':
        resultData = detallesdelDestino(idDestino) #Funcion que almacena los detalles del Destino
        
        if resultData:
            return render_template('public/acciones/view.html', infoDestino = resultData, msg='Detalles del Destino', tipo=1)
        else:
            return render_template('public/acciones/layout.html', msg='No existe el Destino', tipo=1)
    return redirect(url_for('inicio'))
    

@app.route('/actualizar-destino/<string:idDestino>', methods=['POST'])
def  formActualizarDestino(idDestino):
    if request.method == 'POST':
        titulo           = request.form['titulo']
        descripcion      = request.form['descripcion']
        plan             = request.form['plan']
        preciofull       = request.form['preciofull']
        preciodes        = request.form['preciodes']
        favorito         = request.form['favorito']
        
        #Script para recibir el archivo (foto)
        if(request.files['foto']):
            file     = request.files['foto']
            fotoForm = recibeFoto(file)
            resultData = recibeActualizarDestino(titulo, descripcion, plan, preciofull, preciodes, favorito, fotoForm, idDestino)
        else:
            fotoDestino  ='sin_foto.jpg'
            resultData = recibeActualizarDestino(titulo, descripcion, plan, preciofull, preciodes, favorito, fotoDestino, idDestino)

        if(resultData ==1):
            return render_template('public/layout.html', miData = listaDestinos(), msg='Datos del Destino actualizados', tipo=1)
        else:
            msg ='No se actualizo el registro'
            return render_template('public/layout.html', miData = listaDestinos(), msg='No se pudo actualizar', tipo=1)


#Eliminar Destino
@app.route('/borrar-destino', methods=['GET', 'POST'])
def formViewBorrarDestino():
    if request.method == 'POST':
        idDestino       = request.form['id']
        nombreFoto      = request.form['nombreFoto']
        resultData      = eliminarDestino(idDestino, nombreFoto)

        if resultData ==1:
            #Nota: retorno solo un json y no una vista para evitar refescar la vista
            return jsonify([1])
            #return jsonify(["respuesta", 1])
        else: 
            return jsonify([0])




def eliminarDestino(idDestino='', nombreFoto=''):
        
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
    cur              = conexion_MySQLdb.cursor(dictionary=True)
    
    cur.execute('DELETE FROM destinos WHERE id=%s', (idDestino,))
    conexion_MySQLdb.commit()
    resultado_eliminar = cur.rowcount #retorna 1 o 0
    #print(resultado_eliminar)
    
    basepath = os.path.dirname (__file__) #C:\xampp\htdocs\localhost\Crud-con-FLASK-PYTHON-y-MySQL\app
    url_File = os.path.join (basepath, 'static/assets/fotos_destinos', nombreFoto)
    os.remove(url_File) #Borrar foto desde la carpeta
    #os.unlink(url_File) #Otra forma de borrar archivos en una carpeta
    
    return resultado_eliminar



def recibeFoto(file):
    print(file)
    basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
    filename = secure_filename(file.filename) #Nombre original del archivo

    #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
    extension           = os.path.splitext(filename)[1]
    nuevoNombreFile     = stringAleatorio() + extension
    #print(nuevoNombreFile)
        
    upload_path = os.path.join (basepath, 'static/assets/fotos_destinos', nuevoNombreFile) 
    file.save(upload_path)

    return nuevoNombreFile

       
  
  
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicio'))
    

    
if __name__ == "__main__":
    app.run(debug=True, port=8000)