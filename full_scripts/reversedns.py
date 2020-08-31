from dns import reversename, resolver
import socket


def dns_reverse():
    try:
        ip = input('Enter ip: ')
        rev_name = reversename.from_address(socket.gethostbyname(ip))
        reversed_dns = str(resolver.query(rev_name, "PTR")[0])
        print(reversed_dns)

    except Exception as e:
        print(e)
