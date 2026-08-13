import qrcode

url=input("enter thr url").strip()
file_path="C:\\Users\\Adnan\\Desktop\\qrcode.png"

obj=qrcode.QRCode()
obj.add_data(url)
img =obj.make_image()
img.save(file_path)