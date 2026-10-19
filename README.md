Python QR Code Generator

A simple Python project that generates QR codes from text or URLs and saves them as image files.

Features
Generate QR codes from text, URLs, or other data.
Save QR codes as PNG images.
Customize QR code colors.
Easy to use and beginner-friendly.
Requirements
Python 3.x
qrcode
Pillow
Installation
Clone or download this project.
Install the required libraries:
pip install qrcode[pil]

Usage

Run the Python script:

python main.py


Enter the text or URL you want to convert into a QR code. The generated QR code will be saved as qrcode.png.

Example Code
import qrcode

data = input("Enter text or URL: ")

qr = qrcode.make(data)
qr.save("qrcode.png")

print("QR code generated successfully!")

Project Structure
python-qr-code/
├── main.py
├── qrcode.png
└── README.md

Example Output

The program generates a QR code image that you can scan with a smartphone to open the encoded URL or read the stored text.

License

This project is open-source and available for educational and personal use.
