__author__ = 'Rosario'
#
# -*- coding: utf-8 -*-

from gluon import current

class RESIZE(object):
    def __init__(self, nx=260, ny=260, error_message=' image resize'):
        (self.nx, self.ny, self.error_message) = (nx, ny, error_message)

    def __call__(self, value):
        if isinstance(value, str) and len(value) == 0:
            return (value, None)
        from PIL import Image
        import cStringIO
        try:
            img = Image.open(value.file)
            img.thumbnail((self.nx, self.ny), Image.ANTIALIAS)
            s = cStringIO.StringIO()
            img.save(s, 'JPEG', quality=100)
            s.seek(0)
            value.file = s
        except:
            return (value, self.error_message)
        else:
            return (value, None)

def THUMB(image, nx=260, ny=260, gae=False, name='thumb'):
    if image:
        if not gae:
            request = current.request
            from PIL import Image
            import os
            #img = Image.open(os.path.join(request.folder,'static','images' + '/' + image[11:13] + '/'  + image))
            img = Image.open(os.path.join(request.folder , 'static/images/albums/image.file/', image[11:13] +'/'+  image))
            img.thumbnail((nx, ny), Image.ANTIALIAS)
            root, ext = os.path.splitext(image)
            thumb = '%s_%s%s' % (root, name, ext)
            img.save(request.folder + 'static/images/albums/image.file/', thumb[11:13] +'/' +   thumb)
            return thumb
        else:
            return image