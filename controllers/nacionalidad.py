# -*- coding: utf-8 -*-
# try something like
@auth.requires_login()
def index():
    return locals()

@auth.requires_login()
def crear():
    # form = crud.create(db.auth_user, db.auth_membership)

    formulario = SQLFORM.factory(db.nacionalidad)

    return locals()

@auth.requires_login()
def admin():
    grid = SQLFORM.grid(db.Nacionalidad,  fields=None,
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
                            upload='<default>',
                            args=[],user_signature=True,
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
                            search_widget='default',)
    return dict(grid=grid)
