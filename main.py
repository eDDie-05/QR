import qrcode 
data="Dogo vp"
qr=qrcode.make(data)
qr.save ("qrcode.png")
print("qrcode created successfully")
        