import dns.resolver


def dns_main():
    try:
        addres = input('Enter domain: ')
        my_resolver = dns.resolver.Resolver(configure=False)
        my_resolver.nameservers = ['8.8.8.8', '1.1.1.1']
        answers = my_resolver.query(addres, 'MX')
        for rdata in answers:
            print(f"MX Record: {rdata.exchange}\n")

    except Exception as e:
        print(f"{e}\n")
