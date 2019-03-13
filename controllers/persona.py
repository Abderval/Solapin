
# -*- coding: utf-8 -*-
# try something like

import base64
from PIL import Image
import cStringIO
from io import BytesIO
import io
import random
import StringIO
from base64 import decodestring
import csv
import io
import os
import base64
from io import BytesIO
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
#nao estou a usar pero funciona perfecto para guardar las imagens
def grava():
    import sys

    try:
        #aqui faz os imports necessários
        import os
        import base64
        from PIL import Image
        from io import BytesIO
        #aqui nomeia as variáveis do nome da imagem
        nome_imagem='minha_imagem.png'
        nome_imagem2='minha_imagem.jpg'

        # use um objeto de memoria para guadar
        #output = StringIO.StringIO()
        #img = qr.make_image()#genera la imagen
        #img.save(output)#guarda la imagen
        output='/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDABALDA4MChAODQ4SERATGCgaGBYWGDEjJR0oOjM9PDkzODdASFxOQERXRTc4UG1RV19iZ2hnPk1xeXBkeFxlZ2P/2wBDARESEhgVGC8aGi9jQjhCY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2P/wAARCAAyADIDASIAAhEBAxEB/8QAGgAAAwEBAQEAAAAAAAAAAAAAAAQFAwECBv/EADIQAAIBAwMBBQYFBQAAAAAAAAECEQADIQQSMUEFE1FhgTJxscHh8CIjkaHRFjM0UoL/xAAYAQADAQEAAAAAAAAAAAAAAAAAAgMBBP/EAB8RAAICAgIDAQAAAAAAAAAAAAABAhESIQMzEzFBYf/aAAwDAQACEQMRAD8AoqF3h53EnGZg/Oa7dvbYkgljgDJJilg7KpEAgEHiQKWv62xYC95dAdjALcnPw/ao+VV+krN7js6lrnBkd3gjHxqI9w3dZedgysFCDbEHM/r7NManVjvu6B6c+HpSVtiLzjkkzJPM5H8elTUnJ2zIvZStbT0UluRFNJHsloPiMUlYksSMbhyZp+yDMGInx4+8U5Q2BSMhp6/gorvdeO+fJj/FFBpHuaxEO4KSBwq4nH1pC3p7ms1gvah2O0AwoiPIVue6W9t3gvBnaZAziSeea3QD2yu0t8PsUSWC0K6UbFdba/N7yARnnM++s7YJGEP5KgKf91+kCfWqVy13qbefCkNKFt3ttxd0SQRMx14pON3oSA9os5ggeNU7SjEEkVP0+xVDWmDWzlYHT7x6VS0rgQSfnVSo4FwJQz7jRTQ2wKKKA+X7R0zNtu21nH4hbAJZTHl+ngR6iFq9XfusA6bLZG5B5fYq1qe0X0qHSKpV7ZKE8FYgD4VJ7bS2t21dXcxZYYtOSAM0bjLCRWcVJZof7M1CtZS2zjvCMLOSBRrENu8t1BBBkEDr1qBYvG1qDcRm7xDKz1HBB8MGqOt7SfUHZbGy34HkmkfG1K0c+LvQ/o1bbcRUbaIe1AkeYnx6U5pdVLEJwQOvNQLOpe0IDNsOCAeau3ttnT6RrWLWpTeHjkgkMvof2p5P6UplcaobRNpZ86KlB3jAEdMfSikzMsU7VA/qPViB/kP8qU7WJBUAmBpTA/7j4AUUVXl7UUj1MlAkoWOTAEn3CvJ6etFFaIaN/anrFW7bMOybABIC65gM8Somiipy9M1jiAbF91FFFQA//9k='
        img_tag = output.replace('\n', '')# guarda la string con formato base64
        img_tag +="="*((4-len(img_tag)%4)%4)# calculo para  eliminar los paddingg
        im=Image.open(BytesIO(base64.b64decode(img_tag)))#decodificar la
        val=1
        nombre="accept" 'vall' ".jpg"
        im.save(nombre,'JPEG')#guarda la imagen en jpg
        # and the use getvalue() method to get the string
        #img_tag = '<img src="data:image/png;base64,%s">' % output.getvalue().encode('base64').replace('\n', '')
        #img_tag +="="*((4-len(img_tag)%4)%4)
        #base64.b64decode(img_tag+'='*(len(img_tag)%4))
        #image=Image.fromstring('RGB',('20','20'),decodestring(img_tag))
        #image.save("rosario299.png")

            #aqui pega a string binaria base64 enviada pelo $.post
        #img = "data:image/jpeg;base64,"
        #img =img[22:] # aqui "recorta as 22 primerias posições da string - qua nao podem ser processadas pela PIL

        #aqui está o código de gravação da imagem em si (PNG e JPG)
        #im = Image.open(BytesIO(base64.b64decode(img))).save(request.folder + 'static/images/' + nome_imagem,'PNG')
        #im2 = Image.open(BytesIO(base64.b64decode(img))).save(request.folder + 'static/images/' + nome_imagem2,'JPEG')

        #retorno = im

    except IOError as erro:
        pass
        #retorno="erro %s" % erro

    #return retorno
@auth.requires_login()
def index():
    return locals()

@auth.requires_login()
def crear():
    # form = crud.create(db.auth_user, db.auth_membership)
    formulario = SQLFORM.factory(db.Persona)
    return locals()

@auth.requires_login()
def admin():

    f= request.vars.foto64=request.vars.foto
    #strImg = base64.b64encode(f)
    response.vars="rosario"
    #ocultar el camppo en la Crud
    if 'view' in request.args:

        db.Persona.foto64.writable = False
        db.Persona.foto64.readable = False
    if 'edit' in request.args:

        db.Persona.foto64.writable = False
        db.Persona.foto64.readable = False
    if 'new' in request.args:
        #db.Persona.foto64.default = 'texto'
        db.Persona.foto64.writable = False
        db.Persona.foto64.readable = False

    grid = SQLFORM.smartgrid(db.Persona,
                            #fields=['foto64'],
                            field_id=None,
                            left=None,
                            headers={},
                            orderby=None,
                            groupby=None,
                            searchable=True,
                            sortable=True,
                            paginate=20,
                            deletable=True,
                            editable=True,
                            details=True,
                            selectable=None,
                            create=True,
                            csv=True,
                            links=None,
                            links_in_grid=True,

                            args=[],user_signature=False,
                            maxtextlengths={},
                            maxtextlength=20,
                            onvalidation=None,
                            oncreate=None,
                            onupdate=None,
                            ondelete=None,
                            sorter_icons=(XML('&#x2191;'),
                            XML('&#x2193;')),
                            ui = 'web2py',
                            showbuttontext=True,
                            _class="web2py_grid",
                            formname='web2py_grid',
                            search_widget='default',
                        )
    #leer las imagenes y guardar en base64 en la base de datos
    resultQueryPersona= db().select(db.Persona.id, db.Persona.foto,db.Persona.foto64)
    for linea in resultQueryPersona:
         if linea.foto:

            url = os.path.join(request.folder, "uploads/"+linea.foto)
            image = open(url, 'rb') #open binary file in read mode
            image_read = image.read()
            image_64_encode = base64.encodestring(image_read)
            db(db.Persona.id==linea.id).update(foto64=image_64_encode)

    return dict(grid=grid)

def personaJson():
    gente = db().select(db.Persona.ALL).as_list()
    return dict(gente=gente)

def download():
    return response.download(request, db)