import requests
from bs4 import BeautifulSoup


def get_page_data(html):
    res = BeautifulSoup(html.text, 'lxml')
    line = res.find_all('loc')
    for i in line:
        print(f"{i.text}")


def sitemap():
    try:
        url = input('Enter host [https://site.com]: ')
        if url[-1] == '/':
            page = requests.get(url + 'sitemap.xml')
        else:
            page = requests.get(url + '/sitemap.xml')
        if page.status_code == 200:
            get_page_data(page)
        else:
            print("File 'sitemap.xml' not found!")
    except Exception as e:
        print(e)
