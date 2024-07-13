import qrcode

# URL of your hosted HTML page
url = "https://kevalkukadiya.github.io/qr-code-python/"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill="black", back_color="white")

# Save the image to a file
img.save("D:\qr_code1.png")

print("QR code generated successfully.")
