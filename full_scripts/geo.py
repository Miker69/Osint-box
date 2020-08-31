import pygeoip
from inspect import getsourcefile
from os.path import abspath


def geoip():
    try:
        p= abspath(getsourcefile(lambda:0))
        ip = input('Enter ip: ')
        gi = pygeoip.GeoIP(str(p)[:-6]+'GeoIPCity.dat')
        city = gi.record_by_addr(ip)
        for key in city:
            if city[key] is None or city[key] == 0:
                continue
            else:
                print(key, city[key], sep=": ")

    except Exception as e:
        print(e)
