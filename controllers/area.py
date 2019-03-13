
# -*- coding: utf-8 -*-
# intente algo como
@auth.requires_login()
def index():
    return locals()
# pide que el usuario que entre en este controller, este registrado
@auth.requires_login()
def admin():
    grid = SQLFORM.grid(db.Area, searchable=False,
                             paginate=None, csv=None,
                             showbuttontext=False,
                             sortable=False, maxtextlength=1000)
    return dict(grid=grid)
@auth.requires_login()
def crear():
    # form = crud.create(db.auth_user, db.auth_membership)

    formulario = SQLFORM.factory(db.Area)

    return locals()
