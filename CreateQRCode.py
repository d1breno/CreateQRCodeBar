import qrcode

cep = ""
url = f"https://www.google.com/maps/search/?api=1&query={cep}"

qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10,  
    border=4,  
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("qr_code_cep.png")

print(f"QR Code gerado com sucesso! Escaneie-o para abrir o endereço do CEP {cep}.")