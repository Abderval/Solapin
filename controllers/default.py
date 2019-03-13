# !/usr/bin/env python
# coding: utf-8
import unittest
from name_utils import slug, abbreviate
@auth.requires_login()
def index():
    return locals()

@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
@auth.requires_login()
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
@auth.requires_login()
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

#Generar codigo Qr a partir del CI, OBS NO SE ESTA USANDO PERO SIRVE PARA JUNTAR TODAS LAS IMAGENES EN UNA SOLA
@auth.requires_login()
def GenerateSolapin(ci):

        ToQRData = ci
        import qrcode
        import StringIO
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=1,
        )
        qr.add_data(ToQRData)
        qr.make(fit=True)

        # use um objeto de memoria para guadar
        output = StringIO.StringIO()
        img = qr.make_image()#genera la imagen
        img.save(output)#guarda la imagen
        img_tag = output.getvalue().encode('base64').replace('\n', '')# guarda la string con formato base64
        img_tag +="="*((4-len(img_tag)%4)%4)# calculo para  eliminar los paddingg
        img_tag='data:image/png;base64,'+img_tag
        #im=Image.open(BytesIO(base64.b64decode(img_tag)))#decodificar la imagen
       # img.save('accept.jpg','JPEG')#guarda la imagen en jpg
        # and the use getvalue() method to get the string
        #img_tag = '<img src="data:image/png;base64,%s">' % output.getvalue().encode('base64').replace('\n', '')
        #img_tag +="="*((4-len(img_tag)%4)%4)
        #base64.b64decode(img_tag+'='*(len(img_tag)%4))
        #image=Image.fromstring('RGB',('20','20'),decodestring(img_tag))
        #image.save("rosario299.png")
        return img_tag

@auth.requires_login()
def generarpagina():

    #Pagination de 50 en 50
    if not request.vars.page:
        redirect(URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    start = (page-1)*50
    end = page*50

    totalposts = db(db.Persona.id >= 0).count()
    totalpages = totalposts / 50

    i=0
    #arrays para guardar los datos de los solapines
    cantSolapin=0
    solapin = []
    nombre=[]
    foto=[]
    categoria=[]
    #hago el inner join para juntar las tablas persona y tipoPersona para obtener el id de tipopersona para poder buscar el tipode Persona e definir su icono izquierdo
    rows = db(db.Persona.id_tipo_Persona == db.Tipo_Persona.id).select(limitby=(start,end))

    for row in rows: #db().select(db.Persona.ci,db.Persona.nombre,db.Persona.foto,db.Persona.apellidos,db.Persona.id_tipo_Persona,limitby=(start,end) ):
        solapin.append(GenerateSolapin(row.Persona.ci))# como todos los campos estan juntos se especifica la tabla en q voy a buscar
        nombreCompleto=row.Persona.nombre+" "+row.Persona.apellidos
        nombre.append(Abreviar(nombreCompleto))
        categoria.append(row.Tipo_Persona.tipo)
        foto.append(row.Persona.foto)
        cantSolapin += 1
    return locals()

#generar un solo solapin() Falta Optimizar el codigo
@auth.requires_login()
def generarvarios():




    personas=db(db.Persona).select()

    cantSolapin=0
    solapin = []
    nombre=[]
    foto=[]
    categoria=[]
    variables =[]

    #hago el inner join para juntar las tablas persona y tipoPersona para obtener el id de tipopersona para poder buscar el tipode Persona e definir su icono izquierdo
    rows = db(db.Persona.id_tipo_Persona == db.Tipo_Persona.id).select()
    #si el usuario haz el post en el formulario
    if request.post_vars:
        #busca la lista de select de carnets
        variables =request.post_vars.getlist('ci')
        #saca los carnets individualmente y los guarda en valor

        for row in rows:
            for ci in variables:
             if(row.Persona.ci==ci):
                solapin.append(GenerateSolapin(row.Persona.ci))# como todos los campos estan juntos se especifica la tabla en q voy a buscar
                nombreCompleto=row.Persona.nombre+" "+row.Persona.apellidos
                nombre.append(Abreviar(nombreCompleto))
                categoria.append(row.Tipo_Persona.tipo)
                foto.append(row.Persona.foto)

                cantSolapin += 1

    return locals()

#generar solapin por ares
def generarporarea():
    #variable qeu retorna todas las areas en en Select Option
    areas=db(db.Area).select()

    cantSolapin=0
    solapin = []
    nombre=[]
    foto=[]
    categoria=[]
    variables =[]

    #variables para llenar el select Option
   # rows = db((db.Persona.id_tipo_Persona == db.Tipo_Persona.id) &( db.Persona.id_Area==4)).select()
    if request.post_vars:

        variables =request.post_vars.getlist('ci')

        for valor in variables:
            #hago el inner join para juntar las tablas persona y tipoPersona para obtener el id de tipopersona para poder buscar el tipode Persona e definir su icono izquierdo
            rows = db((db.Persona.id_tipo_Persona == db.Tipo_Persona.id) &( db.Persona.id_Area==valor)).select()
            for row in rows:
                for ci in variables:
                 if(row.Persona.id_Area==int(ci)):
                    solapin.append(GenerateSolapin(row.Persona.ci))# como todos los campos estan juntos se especifica la tabla en q voy a buscar
                    nombreCompleto=row.Persona.nombre+" "+row.Persona.apellidos
                    nombre.append(Abreviar(nombreCompleto))
                    categoria.append(row.Tipo_Persona.tipo)
                    foto.append(row.Persona.foto)
                    cantSolapin += 1
    return locals()
# generar todos los solapines
@auth.requires_login()
def generartodos():


    if not request.vars.page:
        redirect(URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    start = (page-1)*50
    end = page*50

    totalposts = db(db.Persona.id >= 0).count()
    totalpages = totalposts / 50
    i=0
    cantSolapin=0
    solapin = []
    nombre=[]
    foto=[]
    categoria=[]
    for row in db().select(db.Persona.ci,db.Persona.nombre,db.Persona.foto,db.Persona.apellidos,db.Persona.id_tipo_Persona ):
        solapin.append(GenerateSolapin(row.ci))
        nombre.append(Abreviar(row.nombre)+" "+row.apellidos)
        categoria.append(row.id_tipo_Persona)
        foto.append(row.foto)
        cantSolapin += 1
    return locals()

@auth.requires_login()
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


# si for maior que 29 caracteres abreviar el segundo Nombre
@auth.requires_login()
def Abreviar(nombre):

    cant=len(nombre)
    nombreOriginal=nombre.strip(' ')
    listaPalabra=nombre.split()# divide las palabras en char q tiene el nombre


    if (cant > 26):# si la cantidad total de nombre+apellidos >29
        segunda=[]# cria un arreglo para guardar los chaar que tiene cada palabra del nombre+apellidos para despues buscar la Letra abreviada
        for i in listaPalabra:
            segunda.append(listaPalabra)

        espacioEntreNombre=nombreOriginal.find(" ")# localiza adonde esta el espacion en el nombre
        letra=nombreOriginal[espacioEntreNombre:espacioEntreNombre+2]+"."# guarda la primera letra del segundo nombre y adiciona un punto
        nombreAbreviado1=nombreOriginal.replace(listaPalabra[1],letra) # entonces si es remplaza el segundo nombre por la letra
        #si el nombre sigue siendo mayor que 20 char abreviar el segundo



        cant2=len(nombreAbreviado1)
        nombreAbreviado2=nombreAbreviado1.lower().title().strip(' ')
        listaPalabra2=nombreAbreviado1.lower().title().split()# divide las palabras q tiene el nombreAbreviado1
        if (cant2 > 26):
            tercera=[]# cria un arreglo para guardar los chaar que tiene cada palabra del nombre+apellidos para despues buscar la Letra abreviada
            for i in listaPalabra2:
                tercera.append(listaPalabra2)
            #busca el segundo espacio en el nombre
            segundoNombreAbreviar=tercera[0][3]
            abrev=segundoNombreAbreviar[0:1]
            nombreAbreviado2=nombreAbreviado1.replace(segundoNombreAbreviar,abrev+".")# localiza adonde esta el espacion en el nombre




        return  nombreAbreviado2.lower().title()
    return nombreOriginal.lower().title()# sino retorna el nombre original



