import qrcode

link_pagina = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(link_pagina)
qr.make()

img = qr.make_image(fill_color = 'blue', back_color = 'white')
img.save('proyectos/qr-gen/qr.png')

print("QR Creado")