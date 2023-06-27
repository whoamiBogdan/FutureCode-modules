#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import xlsxwriter


pages = 10

def get_soup(url):
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    return soup

def parse(pages):
    urls = []
    fmt = 'https://www.parsemachine.com/sandbox/catalog/?page={page}'

    for i in range(1, 1 + pages):
        page_url = fmt.format(page=i)
        soup = get_soup(page_url)
        for tag in soup.select('.product-card .title'):
            href = tag.attrs['href']
            url = f'https://www.parsemachine.com{href}'
            urls.append(url)

    return urls

def parse_product(urls):
    data = []
    for url in urls:
        soup = get_soup(url)
        name = soup.select_one('#product_name').text.strip()
        price = soup.select_one('#product_amount').text.strip()
        techs = {}
        for x in soup.select('#characteristics tbody tr'):
            cols = x.select('td')
            cols = [c.text.strip() for c in cols]
            techs[cols[0]] = cols[1]

        item = {
            'name' : name,
            'amount' : price,
            'techs' : techs,
        }
        data.append(item)
    return data

def main():
    urls = parse(pages)
    data = parse_product(urls)
    headers = ['Название', 'Цена']
    with xlsxwriter.Workbook('table.xlsx') as file:
        ws = file.add_worksheet()
        headers.extend(data[0]['techs'].keys())

        for a, b in enumerate(headers):
            ws.write_string(0, a, b)

        for i, x in enumerate(data, start=1):
            ws.write_string(i, 0, x['name'])
            ws.write_string(i, 1, x['amount'])
            for name_p, value_p in x['techs'].items():
                col = headers.index(name_p)
                ws.write_string(i, col, value_p)

main()
