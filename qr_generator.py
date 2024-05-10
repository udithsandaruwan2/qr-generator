import qrcode

def qr_generator(text):

    qr = qrcode.QRCode(
        version = 1.0,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_1.png")
    print("Successfully Generated!!!")

text = input("ENTER THE TEXT : ")
qr_generator(text)