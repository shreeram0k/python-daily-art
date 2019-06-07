# plays a music file when results are out!
from selenium import webdriver
from bs4 import BeautifulSoup
from pygame import mixer
import time
import urllib.request
import requests


# x=input("Enter the URL\n")
x = '#url_of_website_to_check'
refreshrate=int(input("Enter the number of seconds\n"))
input_ = 0
count = 0

source = requests.get('#url_of_website_to_check').text
soup = BeautifulSoup(source, 'lxml')
container = soup.find(class_='panel-body')
update_message = container.label.text
update_trancated = update_message[21:]
print(update_trancated)

driver = webdriver.Chrome()
driver.get("http://"+x)
while True:
    time.sleep(refreshrate)
    driver.refresh()
    if (update_trancated == ' 27/02/2019 @ 11:10 PM.'):
        count = count + 1
        print(count,'No updates...')
    else:
        print('Results updated!')
        mixer.init()
        mixer.music.load('music_file.mp3')
        mixer.music.play()
