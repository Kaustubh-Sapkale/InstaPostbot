from instabot import Bot

import os, random

import glob
cookie_del = glob.glob("config/*cookie.json")
if len(cookie_del) > 0:
    os.remove(cookie_del[0])

f = random.choice(os.listdir("./data/2004_Torun"))

bot = Bot()
bot.login(username="for_learning_purpose", password="@12345678")


bot.upload_photo('HPIM3239.JPG', caption="your post caption")

