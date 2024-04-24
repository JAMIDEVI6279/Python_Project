import qrcode 
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)

qr.add_data("https://developers.google.com/focus/web-development")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="pink")
img.save("Course.png")


"""
We import the qrcode library to generate QR codes.
We import the Image class from the PIL module for image manipulation.
We create a QRCode object with specific parameters using the qrcode library.
We add data to the QR code using the add_data() method.
We generate the QR code using the make() method with fit=True to automatically resize the QR code.
We create an image representation of the QR code with specific colors using the make_image() method.
We save the generated QR code image to a file named "Course.png".  """