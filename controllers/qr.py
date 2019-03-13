
import qrcode
import StringIO
def qrpage():
    #Install Python Modules: (Pillow,qrcode)
    #https://github.com/lincolnloop/python-qrcode
    
    ToQRData='Likes MLP:FIM'
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(ToQRData)
    qr.make(fit=True)

    # use an in-memory object to save
    salida = StringIO.StringIO()
    img = qr.make_image()
    img.save(salida)

    # and the use getvalue() method to get the string
    img_tag = '<img src="data:image/png;base64,%s">' % salida.getvalue().encode('base64').replace('\n', '')
    return locals()