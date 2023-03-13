# https://www.codewars.com/kata/514a024011ea4fb54200004b
# import re


# def domain_name(url):
#     return re.search('(https?://)?(www\.)?(?P<domain>[^.]+)\.', url).group('domain')

def domain_name(url):
    return url.split('//')[-1].replace('www.', '').split('.')[0]


print(domain_name("http://google.com"), "google")
print(domain_name("http://google.co.jp"), "google")
print(domain_name("www.xakep.ru"), "xakep")
