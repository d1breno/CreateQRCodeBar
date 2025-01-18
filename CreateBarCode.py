from barcode import Code128
from barcode.writer import ImageWriter

cep = ""

codigo_barras = Code128(cep, writer=ImageWriter())

codigo_barras.save("codigo_barras_cep")

print(f"Código de barras gerado com sucesso! Salvo como 'codigo_barras_cep.png'.")