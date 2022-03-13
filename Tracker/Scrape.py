import requests
from bs4 import BeautifulSoup
import time
import csv
print("Welcome to the Steam price tracker Alpha 0.01,Created by Ivan Chan")
url =input("Plz paste the game that you wanna track on (website)")

def getTitle(url):
    page = requests.get(url)
    html = page.content
    soup = BeautifulSoup(html,"html.parser")
    title = soup.find("title")
    title = title.contents[0]
    title = title.replace('on','')
    title = title.replace('Steam','')
    return(title)

def getPrice(url):
    page = requests.get(url)
    html = page.content
    soup = BeautifulSoup(html,"html.parser")
    price = soup.find("div", class_="game_purchase_price price")
    price = price.contents[0]
    price = price.replace(",",".")
    price = price.replace("€","")
    price = float(price)
    return price



print(getTitle(url))
print(getPrice(url))

f = open("T&p per hour.csv","a")
line = str(getTitle(url)) + "," + str(getPrice(url)) + "\n"
f.write(line)
f.close()