import time
import os
import requests

if not os.path.isdir("C:\\PODARKI"):
     os.mkdir("C:\\PODARKI")
giftCount = 1278
print("Darova! Vse podarki budut sckachnany v papku C:/PODARKI. Udachi ne poluchit ban po ip!")
for i in range(1, giftCount):
    link = "https://vk.com/images/gift/"+str(i)+"/256.jpg"
    time.sleep(4)
    p = requests.get(link)
    out = open("C:\\PODARKI\\podarok"+str(i)+".jpg", "wb")
    out.write(p.content)
    out.close()
    print(link)