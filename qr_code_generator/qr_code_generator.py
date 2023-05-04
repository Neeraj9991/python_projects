import pyqrcode

from pyqrcode import QRCode

# String which will be converted to QR Code
str = 'https://www.google.com/'

# Generate QR Code
url = pyqrcode.create(str)


url.svg('pyqrcode',scale=5)
