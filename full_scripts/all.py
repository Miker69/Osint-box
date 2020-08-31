import socket
import pygeoip
import whois
from nslookup import Nslookup
import dns.resolver
from dns import reversename, resolver
import requests
from bs4 import BeautifulSoup
import urllib3

menu = (

    '1. Host ip', '2. Site location', '3. Whois', '4. Nslookup', '5. DNS MX-Record', '6. Reverse DNS', '7. robots.txt',
    '8. sitemap.xml', '9. Reverse ip site')


def address():
    try:
        host = input('Enter host: ')
        if '://' in host:
            host = host.split('://')[1]
        host = host.replace('/', '')
        with open('Check_domain.txt', 'a') as file:

            file.write(f"{'-' * 35}{chr(10) + menu[0] + chr(10)}{'-' * 35}")
            file.write(f"Ip address of {host} is {socket.gethostbyname(host)}\n")

        geoip(host)
    except Exception as e:
        print(e)


def geoip(s):
    try:
        with open('Check_domain.txt', 'a') as file:
            file.write(f"{'-' * 35}{chr(10) + menu[1] + chr(10)}{'-' * 35}")
            gi = pygeoip.GeoIP('../GeoIPCity.dat')
            city = gi.record_by_addr(socket.gethostbyname(s))
            for key in city:
                if city[key] is None or city[key] == 0:
                    continue
                else:
                    file.write(f" {key} : {city[key]} \n")
        who(s)
    except Exception as e:
        print(e)


def who(add):
    try:
        with open('Check_domain.txt', 'a') as file:
            file.write(f"{'-' * 35}{chr(10) + menu[2] + chr(10)}{'-' * 35}")
            domain = whois.query(add)
            res = domain.__dict__
            for i in res:
                file.write(f"{i} : {res[i]}\n")
        nslook(add)
    except Exception as e:
        print(e)


def nslook(domain):
    try:
        with open('Check_domain.txt', 'a') as file:
            file.write(f"{'-' * 35}{chr(10) + menu[3] + chr(10)}{'-' * 35}")
            dns_query = Nslookup(dns_servers=['1.1.1.1'])
            ips_record = dns_query.dns_lookup(domain)
            for i in ips_record.response_full:
                file.write(f"{''.join(i.split('. '))}\n")
            soa_record = dns_query.soa_lookup(domain)
            for i in soa_record.response_full:
                file.write(f"{str(i)}\n")
        dns_main(domain)
    except Exception as e:
        print(e)


def dns_main(addres):
    try:
        with open('Check_domain.txt', 'a') as file:
            file.write(f"{'-' * 35}{chr(10) + menu[4] + chr(10)}{'-' * 35}")
            my_resolver = dns.resolver.Resolver(configure=False)
            my_resolver.nameservers = ['8.8.8.8', '1.1.1.1']
            answers = my_resolver.query(addres, 'MX')
            for rdata in answers:
                file.write(f"MX Record: {rdata.exchange}\n")
        dns_reverse(addres)
    except Exception as e:
        with open('Check_domain.txt', 'a') as file:
            file.write(f"{e}\n")


def dns_reverse(a):
    try:

        with open('Check_domain.txt', 'a') as file:
            rev_name = reversename.from_address(socket.gethostbyname(a))
            reversed_dns = str(resolver.query(rev_name, "PTR")[0])
            file.write(f"{'-' * 35}{chr(10) + menu[5] + chr(10)}{'-' * 35}")
            file.write(f"{reversed_dns}\n")

    except Exception as e:
        with open('Check_domain.txt', 'a') as file:
            file.write(f"{'-' * 35}{chr(10) + menu[5] + chr(10)}{'-' * 35}")
            file.write(f"{e}\n")
    finally:
        robot(a)


def get_page_datas(html):
    res = html.text
    with open('Check_domain.txt', 'a') as file:
        file.write(f"{'-' * 35}{chr(10) + menu[6] + chr(10)}{'-' * 35}")
        file.write(f"{res}\n")


def robot(url):
    try:

        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        url = 'http://' + url
        if url[-1] == '/':
            page = requests.get(url + 'robots.txt', headers=head)
        else:
            page = requests.get(url + '/robots.txt', headers=head)
        if page.status_code != 404:
            get_page_datas(page)
        else:
            with open('Check_domain.txt', 'a') as file:
                file.write(f"{'-' * 35}{chr(10) + menu[6] + chr(10)}{'-' * 35}")
                file.write(f"\nFile 'robots.txt' not found!\n")
        sitemap(url)
    except Exception as e:
        print(e)


def get_page_data(html):
    res = BeautifulSoup(html.text, 'lxml')
    line = res.find_all('loc')
    with open('Check_domain.txt', 'a') as file:
        file.write(f"{'-' * 35}{chr(10) + menu[7] + chr(10)}{'-' * 35}")
        for i in line:
            file.write(f"{i.text}\n")


def sitemap(url):
    try:

        if url[-1] == '/':
            page = requests.get(url + 'sitemap.xml')
        else:
            page = requests.get(url + '/sitemap.xml')
        if page.status_code == 200:
            get_page_data(page)
        else:
            with open('Check_domain.txt', 'a') as file:
                file.write(f"{'-' * 35}{chr(10) + menu[7] + chr(10)}{'-' * 35}")
                file.write(f"File 'sitemap.xml' not found!\n")
    except Exception as e:
        print(e)
    finally:
        url = url.replace('http://', '')
        reverse_ip(socket.gethostbyname(url))


def request_info(html, ip):
    with open('Check_domain.txt', 'a') as file:
        file.write(f"{'-' * 35}{chr(10) + menu[8] + chr(10)}{'-' * 35}")
        file.write(f"Found domain hosted on the same web server as {ip} ({socket.gethostbyname(ip)})\n")
        soup = BeautifulSoup(html.text, 'lxml')

        line = soup.find("div", {"class": "ml20"}).find_all('table')

        for i in line[1].find_all('a', href=True):
            file.write(i.text)


def reverse_ip(ip):
    try:
        url = 'https://www.cy-pr.com/tools/oneip/'
        x = {'ip': ip}
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        page = requests.post(url, data=x, verify=False)
        request_info(page, ip)

    except Exception as e:
        print(e)
    finally:
        print('Done!')
