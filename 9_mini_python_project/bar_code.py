import barcode
from barcode.writer import ImageWriter

text = input("Enter text: ")

code128 = barcode.get_barcode_class('code128')
barcode_img = code128(text, writer=ImageWriter())

file_name = barcode_img.save("my_barcode")

print(f"Barcode Saved as {file_name}.png")

