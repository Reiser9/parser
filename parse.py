import requests
from bs4 import BeautifulSoup as bs
import csv

URL = 'https://youla.ru/tyumen?q=%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C'
HEADERS = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.92 Safari/537.36 42885'}

def parse(url, headers):
    session = requests.Session()
    request = session.get(url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        cont = soup.find_all("li", class_="product_item")
        content = []
        for i in cont:
            title = i.find("div", class_="product_item__title").get_text(strip=True)
            price = i.find("div", class_="product_item__description").find_next("div").get_text(strip=True).replace("₽", " ")
            city = i.find("span", class_="product_item__location").get_text(strip=True)
            content.append({
                "title": title,
                "price": price,
                "city": city
            })
        print(content)
    else:
        print('Ошибка')

parse(URL, HEADERS)