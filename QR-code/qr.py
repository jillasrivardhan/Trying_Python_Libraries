import segno

import qrcode

#this is a simple code to generate a QR code for the text 'porsche 911 TurboS' and save it as an SVG file with a dark green color.

#segno.make takes the text that you want to encode in the QR code as an argument and returns a QR code object. 
#
# The save method is then called on the QR code object to save it as an SVG file with the specified filename and color.

qrcode = segno.make('porsche 911 TurboS')
qrcode.save('my first qr code.svg',dark='green') 


data = 'porsche 911 TurboS'
qr = qrcode.QRCode(
      version=1, 
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
)
qr.add_data(data)
qr.make(fit=True)
qr.save('my second qr code.png')
