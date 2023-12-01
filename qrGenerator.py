import qrcode

def gen_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=5,
    )
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save(file_name)

# input text to generate QR code for.
text = "github.com/Lutezzi"

# input name to save the QR code image.
file_name = "qrCode.png"

gen_qr_code(text, file_name)
print(f"QR code saved as {file_name}")