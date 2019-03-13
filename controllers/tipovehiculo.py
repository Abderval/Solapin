# -*- coding: utf-8 -*-
# intente algo como
@auth.requires_login()
def index():
    return locals()
@auth.requires_login()
def crear():
    # form = crud.create(db.auth_user, db.auth_membership)

    formulario = SQLFORM.factory(db.tipoVehiculo)

    return locals()

@auth.requires_login()
def admin():
    grid = SQLFORM.grid(db.Tipo_Vehiculo, searchable=False,
                             paginate=None, csv=None,
                             showbuttontext=False,
                             sortable=False, maxtextlength=1000)
    return dict(grid=grid)
