import sys
import os
import re
import unicodedata

from pdf2image import convert_from_path

from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError)

#taking path of image
images = convert_from_path(sys.argv[1])

# converting each page to image and sending to ocr
for i, image in enumerate(images):
    fname = 'image'+str(i)+'.png'
    image.save(fname, "PNG")
    os.system("tesseract.exe "+ fname + " A" + str(i) + " -l eng")

#combining all pages
os.system("copy A*.txt final.txt")

#sending to app
f= open("final.txt","r",encoding='utf-8')
text=f.read()
"""
text2=re.sub(r"\s+"," ", text, flags = re.I)

print("വയസ്സ് ")
pattern = "വയസ്സ്(.*?)\("

ptaluk = "താലൂക്ക്‌(.*?)ദേശം

substring= re.search(pattern, text2)

taluk=re.search(ptaluk,text2)

g= open("name.txt","w",encoding='utf-8')
g.write(substring.group(1))

h= open("taluk.txt","w",encoding='utf-8')
h.write(taluk.group(1))

type = text2.split()[0]

i= open("type.txt","w",encoding='utf-8')
i.write(type)

"""
