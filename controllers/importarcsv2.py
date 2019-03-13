__author__ = 'Rosario'
import csv

def importarcsv():


    #boton para cargar el fichero csv
    form = FORM(INPUT(_type='file',_name='csvfile'),INPUT(_type='submit',__value='Subir CSV',_class="btn btn-primary",))

    if form.process().accepted:

        file = request.vars.csvfile.file
        readCSV = csv.reader(file, delimiter=';')
    try:
        next(readCSV, None)
        for row in readCSV:
                #insertar las nacionalidades sin repetir
                nacionalidad = {'nacionalidad':row[3].strip(' ')}
                registro = db.Nacionalidad(**db.Nacionalidad._filter_fields(nacionalidad)) # Check for a match.
                nacionalid_id = registro.id if registro else db.Nacionalidad.insert(**db.Nacionalidad._filter_fields(nacionalidad))

                 #insertar los tipos de persona sin repetir

                tipoPersona = {'tipo':row[27].strip(' ')}
                registroTipo = db.Tipo_Persona(**db.Tipo_Persona._filter_fields(tipoPersona)) # Check for a match.
                tipoPersona_id = registroTipo.id if registroTipo else db.Tipo_Persona.insert(**db.Tipo_Persona._filter_fields(tipoPersona))

                  #insertar Area sin repetir
                area = {'area':row[4].strip(' ')}
                registroArea = db.Area(**db.Area._filter_fields(area)) # Check for a match.
                area_id = registroArea.id if registroArea else db.Area.insert(**db.Area._filter_fields(area))

                resultQueryNacionalidad = db().select(db.Nacionalidad.id, db.Nacionalidad.nacionalidad)
                resultQueryTipoPersona = db().select(db.Tipo_Persona.id, db.Tipo_Persona.tipo)
                resultQueryArea = db().select(db.Area.id, db.Area.area)

                idArea=None
                #busca el Area e sale cuando la encuentra
                for lineaA in resultQueryArea:
                    if area['area'].decode('latin_1').encode('utf_8')==lineaA.area:#.decode('latin_1').encode('utf_8')
                        idArea=lineaA.id
                        break

                idTipoPersona=None
                #busca el tipo de person e sale cuando la encuentra
                for lineaT in resultQueryTipoPersona:
                    if row[27]==lineaT.tipo:
                        idTipoPersona=lineaT.id
                        break



                #busca la nacionalidad que es igual en el fichero csv e inserta el record completo
                for linea in resultQueryNacionalidad:
                    if row[3]==linea.nacionalidad:
                        idPais=linea.id
                        #'sexo':row[25],
                        persona ={'ci':row[0].strip(' '),'nombre':row[1].strip(' '),'apellidos':row[2].strip(' '),'idNacionalidad':idPais,
                                  'id_tipo_Persona':idTipoPersona,'id_Area':idArea,'sexo':row[25].strip(' '),}
                        registroP = db.Persona(**db.Persona._filter_fields(persona)) # Check for a match.

                        if registroP:
                             Persona_id =  registroP.ci
                        else: db.Persona.insert(**db.Persona._filter_fields(persona))

    except Exception, e:
           print ("Error al importar el fichero CSV")

    return locals()

def import_and_sync():
    form = FORM(INPUT(_type='file', _name='data'), INPUT(_type='submit'))
    if form.process().accepted:
        db.import_from_csv_file(open('test.csv', 'r'), unique=False)
        # for every table
        for table in db.tables:
            # for every uuid, delete all but the latest
            items = db(db[table]).select(db[table].id,
                                         db[table].uuid,
                                         orderby=db[table].modified_on,
                                         groupby=db[table].uuid)
            for item in items:
                db((db[table].uuid==item.uuid) &
                   (db[table].id!=item.id)).delete()
    return dict(form=form)
