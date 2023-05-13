# install the libraries = pip3 install qrcode Image
# function that collects a text and converts it into a QR code
# save the QR code as an image
# run funtcion

import qrcode


def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5
    )

    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr.png")


my_ulr = input("Paste the url here: ")
generate_qr_code(my_ulr)
