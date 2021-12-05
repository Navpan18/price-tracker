import requests 
from bs4 import BeautifulSoup 
import pygame 
import time
import json

with open('settings.json','r') as file:
    settings = json.load(file)

pygame.mixer.init()
pygame.mixer.music.load(settings["remind-sound-path"])

my_price = settings['budget']

currency_symbols = ['€', '	£', '$', "¥", "HK$", "₹", "¥", "," ] 

URL = settings['url']

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'} 

def checking_price():
    page = requests.get(URL, headers=headers)
    soup  = BeautifulSoup(page.content, 'html.parser')

    product_title = soup.find('span', id='productTitle')
    product_title = product_title.text.strip()
    product_price = soup.find('span', id='priceblock_ourprice')
    product_price = product_price.text.strip()

    for i in currency_symbols : 
        product_price = product_price.replace(i, '')

    product_price = int(float(product_price))


    print("The Product Name is:" ,product_title.strip())
    print("The Price is:" ,product_price)

    if(product_price<my_price):
        pygame.mixer.music.play()
        print("You Can Buy This Now!")
        time.sleep(3)
        exit()
    else:
        print("The Price Is Too High!")

while True:
    checking_price()
    time.sleep(settings['remind-time']) 
