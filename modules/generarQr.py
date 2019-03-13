import qrcode
import StringIO
from fpdf import FPDF

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('rosario')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.show()
img.save("C:/Users/Rosario/Pictures/Pictures/rosarioq.PNG")

def add_image(image_path,image_path2):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image_path, x=10, y=8, w=100)
    pdf.image(image_path2, x=40, y=32, w=100)
    pdf.set_font("Arial", size=12)
    pdf.ln(85)  # move 85 down
    pdf.cell(200, 10, txt="{}".format(image_path), ln=1)
    pdf.output("add_image.pdf")

if __name__ == '__main__':
    add_image('C:\\Users\Rosario\\Pictures\\Pictures\\rosario.jpg','C:\\Users\Rosario\\Pictures\\Pictures\\rosarioqr.PNG')



