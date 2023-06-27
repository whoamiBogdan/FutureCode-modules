#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs

link = 'https://www.wildberries.ru/'

def get_soup(link):
    global html
    r = requests.get(link)
    html = bs(r.content, 'html.parser')
    return html

def get_source(link):
    get_soup(link)
    print(html)

def get_a(link):
    get_soup(link)
    a = html.find_all('a')
    for i in a:
        url = i.get('href')
        print(url)

get_a(link)
