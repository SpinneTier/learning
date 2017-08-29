import telebot
import uuid
import random
from PIL import Image
token = "390694492:AAF-q4GJUneidzlDSeyFcjZEjGCgdBTDB5E"
bot = telebot.TeleBot(token=token)
def change(path_to_file):
    im=Image.open(path_to_file).convert('RGBA')
    pr=Image.open('/home/krtk/pr.png').convert('RGBA')
    pr=pr.resize((im.width, im.height))
    pr.paste(im)
    im=im.resize((im.width*2, im.height*2))
    pixels = im.load()
    im.paste(pr,(0,0))
    im.paste(pr,(im.width//2,0))
    im.paste(pr,(im.width//2,im.height//2))
    im.paste(pr,(0,im.height//2))
    a=0
    print('fine')
    for x in range(im.width//2):
     for y in range(0,im.height//2):
        r, g, b, tr = pixels[x, y]
        a=(r+g+b)
        if a//3>300:
            pixels[x, y] = (204,g,b, 255)
        else:
            pixels[x, y] = (144,g,b, 255)
    print('fine')
    for x in range(im.width//2,im.width):
     for y in range(0,im.height//2):
        r, g, b, tr = pixels[x, y]
        a=(r+g+b)
        if a//3>300:
            pixels[x, y] = (r,198,b, 255)
        else:
            pixels[x, y] = (r,104,b, 255)
    for x in range(0,im.width//2):
     for y in range(im.height//2,im.height):
        r, g, b, tr = pixels[x, y]
        a=(r+g+b)
        if a//3>300:
            pixels[x, y] = (r,g,234, 255)
        else:
            pixels[x, y] = (r,g,103, 255)
    for x in range(im.width//2,im.width):
     for y in range(im.height//2,im.height):
        r, g, b, tr = pixels[x, y]
        a=(r+g+b)
        if a//3>300:
            pixels[x, y] = (r+100,g+100,b+100, 255)
        else:
            pixels[x, y] = (r+100,g+100,b+100, 255)
    im.save(path_to_file)
    print('fine')
@bot.message_handler(content_types=['photo'])
def message_handler(message):
    # скачивание файла
    file_id = message.photo[-1].file_id
    path = bot.get_file(file_id)
    downloaded_file = bot.download_file(path.file_path)
    # применяем фильтр
    # узнаешь расширение и придумываем имя
    extn = '.' + str(path.file_path).split('.')[-1] # .jpg
    filename = str(uuid.uuid4()) + extn
    path_to_file = "images/" + filename
    print(path_to_file)
    
    # создаем файл и записываем туда данные
    with open(path_to_file, 'wb') as new_file:
        new_file.write(downloaded_file)
    change(path_to_file)
    # открываем файл и отправляем его пользователю
    with open(path_to_file, 'rb') as new_file:
        bot.send_photo(message.chat.id, new_file.read())
bot.polling(none_stop=True)
print('fine')
