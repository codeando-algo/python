from qrcode import QRCode

qr = QRCode(version=3, box_size=20, border=20)

qr.add_data('Hola mundo')
qr.make(fit=True)

img = qr.make_image(fill_color=(230, 255, 8), back_color = (182, 0, 0))
img.save('wtf.png')
img.show()
