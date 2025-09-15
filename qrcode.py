import qrcode
data = input("enter your data :").strip()
file_name = input("enter your file name :").strip()
qr = qrcode.QRcode(box_size=15,border=5)
qr.add_data(data)
qr.make_image(fill_color="bright pink ", back_color="white")
qr.save(f'{file_name}.png')