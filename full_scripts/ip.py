import socket


def address():
    try:
        host = input('Enter host: ')
        if '://' in host:
            host = host.split('://')[1]
        host = host.replace('/', '')
        print(f"Ip address of {host} is {socket.gethostbyname(host)}")

    except Exception as e:
        print(e)
