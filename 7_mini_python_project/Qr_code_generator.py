import qrcode


print("=========== QR Code Generator ===========")

data = input("Enter text or URL: ")

img = qrcode.make(data)

file_name = input("Enter file name (without.png): ")

img.save(f"{file_name}.png")

print(f"\n QR code generated successfully! ")

print(f"file Saved as: {file_name}.png")