import random
from PIL import Image
asd=str(input('Введите адрес картинки: '))
copy=Image.open('/home/krtk/python/pr.png').convert('RGBA')
im=Image.open(asd).convert('RGBA')
copy=copy.resize((im.width, im.height))
copy.paste(im)
pixels=copy.load()
a=0
for x in range(copy.width):
    for y in range(copy.height):
        r, g, b, tr = pixels[x, y]
        a=random.randint(-256,256)
        pixels[x, y]=(r,b,g,127)
        a=random.randint(-256,256)
        pixels[x, y]=(r,b*a,g,127)
        a=random.randint(-256,256)
        pixels[x, y]=(a,b,g*a,127)
im.paste(copy)
f=str(input('Введите адрес cохранения: '))
im.save(f)
