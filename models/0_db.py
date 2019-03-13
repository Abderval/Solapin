# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.tools import Service
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth
service = Service()

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
   # db = DAL(configuration.get('db.uri'),
    #         pool_size=configuration.get('db.pool_size'),
    #        migrate_enabled=configuration.get('db.migrate'),
    #       check_reserved=['all'])
     # base de datos para las tareas programadas
    db = SQLDB("sqlite://db.db",db_codec='utf8')

    dbTask = DAL("sqlite://dbTask.db")
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = [] 
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)

auth = Auth(db, host_names=configuration.get('host.names'))
# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
auth.settings.extra_fields['auth_user'] = []
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get('smtp.server')
mail.settings.sender = configuration.get('smtp.sender')
mail.settings.login = configuration.get('smtp.login')
mail.settings.tls = configuration.get('smtp.tls') or False
mail.settings.ssl = configuration.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------




#auth.settings.table_group_name = 'user_group'
#auth.settings.table_membership_name = 'user_membership'
#auth.settings.table_permission_name = 'user_permission'
#auth.settings.table_event_name = 'user_event'

#auth.settings.login_userfield = 'username'        #the loginfield will be email instead of username

# -------------------------------------------------------------------------  
# read more at http://dev.w3.org/html5/markup/meta.name.html               
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
#response.show_toolbar = configuration.get('app.toolbar')

# -------------------------------------------------------------------------
# your http://google.com/analytics id                                      
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get('scheduler.heartbeat'))

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)



db.define_table("Tipo_Persona",
    Field("tipo", "string",notnull=True,requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),format='%(tipo)s',)

db.define_table("Nacionalidad",
    Field("nacionalidad","string",unique=True, length=100,notnull=True, requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
    migrate=True,format='%(nacionalidad)s',)

db.define_table("Area",
    Field("area", "string",),format='%(area)s',)

db.define_table("Tipo_Vehiculo",
    Field("nombre", "string", default=None),format='%(nombre)s',)

sexo=('Masculino','Feminino')

db.define_table("Persona",
    Field("nombre", "string", notnull=True,requires=[IS_NOT_EMPTY()]),
    Field("apellidos", "string", default=None,requires=[IS_NOT_EMPTY()]),
    Field("ci", "string",unique=False,requires=[IS_NOT_EMPTY()]),
    Field("idNacionalidad","reference Nacionalidad",label='Nacionalidad',requires=[IS_NOT_EMPTY()]),
    Field("foto", "upload",),#uploadfield='foto64',
    Field("sexo",requires=IS_IN_SET(sexo)),
    Field("id_tipo_Persona", "reference Tipo_Persona",label='Tipo de Persona',requires=[IS_NOT_EMPTY()]),
    Field("id_Area", "reference Area",label='Area',requires=[IS_NOT_EMPTY()]),
    Field("becado", "boolean"),
    Field("foto64", "blob"),format='%(foto64)s', )
#,format='%(foto64)s',

db.define_table("Vehiculo",
    Field("nombreVehiculo", "string",unique=True, default=None,requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
    Field("chapa", "string", length=40, default=None),
    Field("id_Persona", "reference Persona",label="Nombre Persona"),
    Field("id_Tipo_Vehiculo", "reference Tipo_Vehiculo",label='Tipo de Vehiculo'),
    Field("descripcion", "string", default=None))



db.define_table("sub_area",
    Field("nombre", "string", default=None,requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
    Field("id_Area", "reference Area",label='Area a que pertenece'))



# Tabla para verificar si se esta actualizando la base de datos y asi bloquear otras funcionalidades
db.define_table("verificar_actualizacion",
                Field("actualizando", "boolean", default=False)
                )

# Tabla para llevar el registro de los cambios de estado
db.define_table("cambio_estado",
                Field("fecha", "datetime"),
                Field("codigo_persona", "string"),
                Field("estado"))

""" Relations between tables (remove fields you don't need from requires) """

db.Vehiculo.id_Persona.requires=IS_IN_DB( db, 'Persona.id', ' %(nombre)s %(ci)s %(foto)s %(apellidos)s %(idNacionalidad)s %(id_tipo_Persona)s %(id_Area)s')
db.Vehiculo.id_Tipo_Vehiculo.requires=IS_IN_DB( db, 'Tipo_Vehiculo.id', ' %(nombre)s')
db.Persona.idNacionalidad.requires=IS_IN_DB( db, 'Nacionalidad.id', ' %(nacionalidad)s')
db.Persona.id_tipo_Persona.requires=IS_IN_DB( db, 'Tipo_Persona.id', ' %(tipo)s')
db.Persona.id_Area.requires=IS_IN_DB( db, 'Area.id', ' %(area)s')
db.sub_area.id_Area.requires=IS_IN_DB( db, 'Area.id', ' %(area)s')

auth = Auth(db)
auth.define_tables(username=True, signature=True)

#----------Autenticacion----------
auth.settings.controller = 'usuario'
auth.settings.login_url = URL('usuario', 'login')
auth.settings.login_next = URL('default', 'index')
auth.settings.on_failed_authentication = URL('usuario', 'login')
auth.settings.logout_next = URL('usuario', 'login')

auth.settings.registration_requires_approval=False
auth.settings.registration_requires_verification=False
auth.settings.reset_password_requires_verification = True
#-----------------mensages en la autenticacion
auth.messages.invalid_login = T('Falló la autenticación')
auth.messages.invalid_user = T('El usuario especificado no es válido')
auth.messages.is_empty = T("No puede ser vacío")
auth.messages.logged_out = T('Se ha cerrado la sesión')

# -------------------------------------------------------------------------
auth.settings.actions_disabled=['profile','reset+password']