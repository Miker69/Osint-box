import requests
import socket
from bs4 import BeautifulSoup
import urllib3


# 178.208.83.7

def request_info(html, ip):
    print(f"Found domain hosted on the same web server as {ip} ({socket.gethostbyname(ip)})\n")
    soup = BeautifulSoup(html.text, 'lxml')

    line = soup.find("div", {"class": "ml20"}).find_all('table')

    for i in line[1].find_all('a', href=True):
        print(i.text)


def reverse_ip():
    try:
        url = 'https://www.cy-pr.com/tools/oneip/'
        ip = input('Enter ip: ')
        x = {'ip': ip}
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        page = requests.post(url, data=x, verify=False)
        request_info(page, ip)
    except Exception as e:
        print(e)
