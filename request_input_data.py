import requests
from requests.auth import HTTPBasicAuth
    
def get_input(day):
    cookie = '53616c7465645f5fd63fff2a9b7be957982482537e21ae780652017b2ccab600203a71b5fe1994c3c6906d2e155fb259'
    url_str = "https://adventofcode.com/2021/day/%s/input" % (day)
    cookies = dict(session=cookie)
    f= requests.get(url_str, cookies=cookies)
    fo = f.text.splitlines()
    return fo

## Print lines in input file
# for line in get_input(1):
#     print(line)

