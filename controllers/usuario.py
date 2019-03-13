__author__ = 'Rosario'


def login():
    form = auth.login()
    return locals()


@auth.requires_login()
def change_password():
    form = auth.change_password()
    return locals()


@auth.requires_login()
def registrar():
    formulario = SQLFORM(db.auth_user)

    if formulario.process().accepted:
        response.flash = T("Usuario creado")
    return dict(form=formulario)

@auth.requires_membership('Administrador')
@auth.requires_login()
def admin():
    grid = SQLFORM.grid(db.auth_user, searchable=False,
                             paginate=None, csv=None,
                             showbuttontext=False,
                             sortable=False, maxtextlength=1000)
    return dict(grid=grid)


@auth.requires_membership('Administrador')
def crear():

 if request.post_vars:
    if formulario.process().accepted:
        response.flash = 'formulario aceptado'
        id_usuario = db.auth_user.insert(**db.auth_user._filter_fields(formulario.vars))
        grupo = formulario.vars.grupo_seleccion
        id_grupo = db.auth_group(db.auth_group.role == str(grupo)).id
        dict_membresia = {"user_id": id_usuario, "group_id": id_grupo}
        id_membresia = db.auth_membership.insert(**dict_membresia)
        response.flash = 'el registro ha sido creado'
    elif formulario.errors:
        response.flash = 'el formulario tiene errores'

    return locals()

@auth.requires_membership('Administrador')
@auth.requires_login()
def crearRol():
    # form = crud.create(db.auth_user, db.auth_membership)

    formulario = SQLFORM.factory(db.auth_group)

    return locals()

@auth.requires_membership('Administrador')
@auth.requires_login()
def gestionar_rol():
    #rol = db.auth_membership(request.args(0, cast=int)) or redirect(URL('default', 'index'))
    # fields = ['grupo_seleccion']
    # labels = {'grupo_seleccion': 'Rol del usuario'}
    formulario = SQLFORM.smartgrid(db.auth_group)


    return locals()



