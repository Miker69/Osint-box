from nslookup import Nslookup


def nslook():
    try:
        domain = input('Enter host: ')
        dns_query = Nslookup(dns_servers=['1.1.1.1'])
        ips_record = dns_query.dns_lookup(domain)
        for i in ips_record.response_full:
            print(f"{''.join(i.split('. '))}\n")
        soa_record = dns_query.soa_lookup(domain)
        for i in soa_record.response_full:
            print(f"{str(i)}\n")
    except Exception as e:
        print(e)
