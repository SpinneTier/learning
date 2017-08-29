import random
from PIL import Image
asd=str(input('Введите адрес картинки:\n'))
copy=Image.open('/home/krtk/copy.png').convert('RGBA')
im=Image.open(asd).convert('RGBA')
copy=copy.resize((im.width*2, im.height*2))
copy.paste(im,(0,0))
copy.paste(im,(im.width,0))
copy.paste(im,(im.width,im.height))
copy.paste(im,(0,im.height))
pixels=copy.load()
for x in range(copy.width//2):
    for y in range(copy.height):
        r, g, b, tr = pixels[x, y]
        a=(r+g+b)
        if a//3>300:
            pixels[x, y] = (204,g,b, 255)
        else:
            pixels[x, y] = (144,g,b, 255)
for x in range(copy.width):
    for y in range(copy.height//2):
        r, g, b, tr = pixels[x, y]
        a=(r+g+b)
        if a//3>300:
            pixels[x, y] = (r,198,b, 255)
        else:
            pixels[x, y] = (r,104,b, 255)
for x in range(copy.height//2,im.height):
    for y in range(copy.width//2):
        r, g, b, tr = pixels[x, y]
        a=(r+g+b)
        if a//3>300:
            pixels[x, y] = (r,g,234, 255)
        else:
            pixels[x, y] = (r,g,103, 255)
for x in range(copy.width//2,copy.width):
    for y in range(copy.height//2,copy.height):
        r, g, b, tr = pixels[x, y]
        a=(r+g+b)
        if a//3>300:
            pixels[x, y] = (r+100,g+100,b+100, 255)
        else:
            pixels[x, y] = (r+100,g+100,b+100, 255)
f=str(input('Введите адрес cохранения:\n'))
copy.save(f)
