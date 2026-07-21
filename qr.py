import segno

#this is a simple code to generate a QR code for the text 'porsche 911 TurboS' and save it as an SVG file with a dark green color.

#segno.make takes the text that you want to encode in the QR code as an argument and returns a QR code object. 
#
# The save method is then called on the QR code object to save it as an SVG file with the specified filename and color.

qrcode = segno.make('porsche 911 TurboS')
qrcode.save('my first qr code.svg',dark='green') 
