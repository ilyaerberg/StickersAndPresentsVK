import time
import os
import requests
#pip install requests
select = int(input("Подарки (1) или стикеры (2)? "))
if select == 1:
    giftCount = 1278
    lessCount = 1
    format = input("Выберите формат: gif, jpg ")
    path = input("Выберите папку, куда складировать стикеры. Пишите \\ вместо /: ")
    if not os.path.isdir(path):
        os.mkdir(path)
    kolwo = int(input("Скачивать до какого подарка? 0 если до "+str(giftCount)+" "))
    volvo = input("Скачивать от какого стикера? 0 если от одного ")
    if kolwo != 0:
        giftCount = kolwo
    if int(lessCount) != 0:
        lessCount = int(volvo)
    if (lessCount >= giftCount):
        print("Вы дебил?")
        lessCount = 0
        giftCount = 75241
    for i in range(lessCount, giftCount):
        link = "https://vk.com/images/gift/"+str(i)+"/256.jpg"
        time.sleep(4)
        p = requests.get(link)
        out = open(path+"\\"+str(i)+"."+str(format), "wb")
        out.write(p.content)
        out.close()
        print(link)
elif select == 2:
    format = input("Выберите формат: gif, jpg ")
    path = input("Выберите папку, куда складировать стикеры. Пишите \\ вместо /: ")
    size = input("Размер 128, 256, 512: ")
    if not os.path.isdir(path):
        os.mkdir(path)
    stickCount = 75241
    lessCount = 1
    kolwo = input("Скачивать до какого стикера? 0 если до "+str(stickCount)+" ")
    volvo = input("Скачивать от какого стикера? 0 если от одного ")
    if int(kolwo) != 0:
        stickCount = int(kolwo)
    if int(lessCount) != 0:
        lessCount = int(volvo)
    if (lessCount >= stickCount):
        print("????")
        lessCount = 0
        stickCount = 75241
    for i in range(lessCount, stickCount):
        link = ("https://vk.com/sticker/1-"+str(i)+"-"+str(size)+".png")
        time.sleep(4)
        p = requests.get(link)
        out = open(path+"\\"+ str(i) + "." + str(format), "wb")
        out.write(p.content)
        out.close()
        print(link)
elif select == 3:
    exit()