import qrcode

url = "https://carlosgallegogarcia.github.io/CV/"
img = qrcode.make(url)
img.save("my_cv_qr.png")