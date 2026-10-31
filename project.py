import qrcode
data=input("enter data: ")
qrname=input("enter name: ")
qr=qrcode.make(data)
qr.save(qrname + ".png")
qr.show()
print("QR Generated Successfully!")
print("saved as: "+qrname+".png")
