from PIL import Image
import os

img = Image.open('./imagem/inuyasha-007.webp')

region = (300,150,500, 300) # alterei esses valores, sendo diferente do exemplo do pdf.
img_crop = img.crop(region)

img_rot = img.rotate(45)

img_crop.show( title='InuyashaCrooped')
img_rot.show('InuyashaRotated')

img_crop.save('./imagem/inuyashacrop.png')

img_rot.save('./imagem/inuyashaRoteted.png')
