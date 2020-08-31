import whois


def who():
    try:
        add = input('Enter domain: ')
        domain = whois.query(add)
        res = domain.__dict__
        for i in res:
            print(f"{i} : {res[i]}\n")
    except Exception as e:
        print(e)
