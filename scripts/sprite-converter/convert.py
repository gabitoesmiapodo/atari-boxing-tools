#!/usr/bin/env python3

from PIL import Image
import pyperclip
import sys

if len(sys.argv) != 2:
    print("Usage: python3 script.py <image.png>")
    sys.exit(1)

path = './img/' + sys.argv[1]
img = Image.open(path).convert("RGB")
w, h = img.size

frame = "export const frame00 = `"
print(frame)

for y in range(h):
    line = ""
    for x in range(w):
        r, g, b = img.getpixel((x, y))
        if (r, g, b) == (210, 210, 210):
            line += "X"
        else:
            line += "."

    # Rellenar con '.' hasta que tenga al menos 134 caracteres
    if len(line) < 134:
        line += '.' * (134 - len(line))

    # Cerrar el string en la última línea
    if y == h - 1:
        line += "`.slice(1)"

    print(line)
    frame += '\n' + line

pyperclip.copy(frame)
print("\nCopied to clipboard.")
