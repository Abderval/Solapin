
import csv
import os
# -*- coding: utf-8 -*-

@service.run
def index():
    return "ouoiuoiu Web2PY"

@service.json
def json():
    nacionalidades = db().select(db.Nacionalidad.ALL).as_list()

    return dict(nacionalidades=nacionalidades)# return dict(areas=areas)

@request.restful()
def api():
    response.view = 'generic.json'



    def GET(*args, **vars):
        Persona=db().select(db.Persona.ALL).as_list()
        Vehiculo=db().select(db.Vehiculo.ALL).as_list()
        sub_area=db().select(db.sub_area.ALL).as_list()
        Tipo_Persona= db().select(db.Tipo_Persona.ALL).as_list()
        nacionalidad = db().select(db.Nacionalidad.ALL).as_list()
        area = db().select(db.Area.ALL).as_list()
        Tipo_Vehiculo=db().select(db.Tipo_Vehiculo.ALL).as_list()


        return dict(Tipo_Persona=Tipo_Persona,nacionalidad=nacionalidad,area=area,Tipo_Vehiculo=Tipo_Vehiculo,Persona=Persona,Vehiculo=Vehiculo,sub_area=sub_area)

    def POST(*args, **vars):

        # if the post is correct only first item is needed




        #def upload():
         #   import cStringIO
          #  data=request.body.read()
           # f=cStringIO.StringIO(data)
            #current_filename='bla.bla' # how to you know the file extension if
            #you do not pass the name?
            #new_filename=db.mytable.picture.store(f,current_filename)
            # do something with new_filename and data


        # actualizacion_movil = vars["fecha_ultima_act"]

        # Comparo la ultima actualizacion del movil con la actual en la bd

        #actualizacion_w2p = db(db.actualizacion).select().last().fecha

        # ultima sincronizacion del movil
        #fecha_ultima_sincro = vars["fecha_ultima_sincro"]

        # Verifico que no esten actualizando la bd
        #actualizacion_en_progreso = db.verificar_actualizacion(1).actualizando

        # verifico que la bd del movil este actualizada
        #no_actualizar = fecha_ultima_sincro > str(actualizacion_w2p)
        try:
           #personas=[]
           #vars recibe el json enviado por post de la aplicacion android
            #return dict(db.Persona.validate_and_insert(**vars))
            #response.headers['multipart/form-data']
            #response.headers['uploaded_file']
            #filepath = os.path.join(vars["uploaded_file"] , 'uploads')
            #response.stream(open(filepath, 'rb'))
            #result=request.post_vars
            planificador.queue_task('insertar_actualizacion', timeout = 120,pvars=dict(vars=vars))
              # En caso de que necesite actualizar
            #if not no_actualizar:
            personas = db().select(db.Persona.ALL).as_list()

        except Exception:
            return dict(devuelvo=Exception.message)

        return dict(personas=personas)



    return locals()


@request.restful()
def login():
    response.view = 'generic.json'

    def POST(*args, **vars):
        username = vars["username"]
        password = vars["password"]
        user = auth.login_bare(username, password)

        if user:
            #retorna este valor para o Android no response
            aceptado = True
        else:
            aceptado = False

        return aceptado

    return locals()


def call():
    session.forget()
    return service()