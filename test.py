
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
        # vars["personas"][0]["nombre"]
        personas = vars["personas"]

        listado = [i["hijos"] for i in personas]

        return dict(devuelvo=listado)

    return locals()

def call():
    session.forget()
    return service()