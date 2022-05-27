# install it 
!pip install  wifi_qrcode_generator

# Import module
import wifi_qrcode_generator as qr

# Use wifi_qrcode() to create a QR image
qr.wifi_qrcode('wifi name ', False, 'WPA', 'password')
