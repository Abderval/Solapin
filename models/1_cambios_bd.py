__author__ = 'Rosario'

#########################################################
# Aqui se crean las tablas que guardan los cambios
# de las actualizaciones que se hagan a la base de datos
# cuando se carge el csv de contabilidad.
#
# Se le puso un 0 en el nombre del archivo db delante para que
# este archivo se ejecutara luego de que db fuera creado
#########################################################

db.define_table("actualizacion",
                Field("fecha", "datetime", default=None),
                )

db.define_table("act_persona",
                Field("foto", "string"),
                Field("ci", "string"),

                )