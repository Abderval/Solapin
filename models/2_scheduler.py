__author__ = 'Rosario'
import time


# -*- coding: utf-8 -*-
"""
#################################################################
###Aqui se define el planificador de tareas
###La base de datos dbTask se usa por el planificador aparte de db
###para no cargar la app
###Para iniciar el planificador ejecutar el comando en la carpeta raiz de web2py:   python web2py.py -K Solapin
#################################################################
"""

def grava(foto):
    try:
        #aqui faz os imports necessários
        from PIL import Image

        import os
        import base64
        from io import BytesIO
        import os
        output=foto #recibe la foto en formato String base64
        img_tag = output.replace('\n', '')# guarda la string con formato base64
        img_tag +="="*((4-len(img_tag)%4)%4)# calculo para  eliminar los paddingg
        im=Image.open(BytesIO(base64.b64decode(img_tag)))#decodificar la

        #url=os.path.join(request.folder, 'static/temp')

        nombre="accept" 'vall3' ".jpg" # guarda la foto en la carpet
        im.save(nombre,'JPEG')#guarda la imagen en jpg
        retorno = open(nombre, 'rb')

    except IOError as erro:

        retorno="erro %s" % erro

    return retorno

# TODO: Arreglar nombre de area no coge las tildes
def tarea_insertar_actualizacion(vars):
    #output = StringIO.StringIO()
    if vars["personas"]:
        personas = vars["personas"]
        username = vars["username"]

        cont=0
        for persona in personas:
            ci = persona["ci"]
            foto = persona["foto64"]
            cont=cont+1
           # db((db.producto.id_tipos_productos == db.tipos_productos.id) & (db.tipos_productos.id==seleccionado))
            if db((db.Persona.foto64 == None) | (db.Persona.foto64 == "null")):  # si existe el ci inserto la foto
                # obtengo y guardo el responsable
                stream=grava(foto)

                db(db.Persona.ci==ci).update(foto64=foto)
                #db(db.Persona.ci==ci).update(foto=fotoJpg)
                if foto != "null":
                    db.act_persona.insert(ci=ci,foto=foto)
                    #db.act_persona.insert(ci=ci,foto=foto)

                    #db.Persona.update(foto=db.Persona.foto.store(stream, "Rosario"),foto64=stream.read())
                    db(db.Persona.ci==ci).update(foto=db.Persona.foto.store(stream, "Rosario.jpg"),foto64=stream.read())

                   # image_64_encode = base64.encodestring(stream.read())
                    db(db.Persona.ci==ci).update(foto64=foto)
                #     image_file=stream.read())


    db.commit()
    pass


from gluon.scheduler import Scheduler

planificador = Scheduler(dbTask, tasks=dict(insertar_actualizacion=tarea_insertar_actualizacion))


