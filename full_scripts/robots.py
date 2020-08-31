import requests
from bs4 import BeautifulSoup


def robot():
    try:
        url = input('Enter host [https://site.com]: ')
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        url = 'http://' + url
        if url[-1] == '/':
            page = requests.get(url + 'robots.txt', headers=head)
        else:
            page = requests.get(url + '/robots.txt', headers=head)
        if page.status_code != 404:
            get_page_data(page)
        else:

            print(f"\nFile 'robots.txt' not found!\n")
    except Exception as e:
        print(e)


def get_page_data(html):
    res = BeautifulSoup(html.text, 'lxml')
    print(res)
