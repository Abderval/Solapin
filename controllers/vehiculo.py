# -*- coding: utf-8 -*-
# intente algo como
@auth.requires_login()
def index():
    return locals()

@auth.requires_login()
def crear():
    # form = crud.create(db.auth_user, db.auth_membership)

    formulario = SQLFORM.factory(db.vehiculo)

    return locals()

@auth.requires_login()
def admin():
    grid = SQLFORM.grid(db.Vehiculo, searchable=False,
                             paginate=None, csv=None,
                             showbuttontext=False,
                             sortable=True, maxtextlength=1000,
                             orderby=False,
                        )

    return dict(grid=grid)
