# code that refreshes the website for entered duration
# https://sites.google.com/a/chromium.org/chromedriver/downloads -> for chrome driver
# place this in the current working directory

from selenium import webdriver
import time
import urllib.request

x=input("Enter the URL\n")
refreshrate=int(input("Enter the number of seconds\n"))
input_ = 0

driver = webdriver.Chrome()
driver.get("http://"+x)
while True:
    time.sleep(refreshrate)
    driver.refresh()
