def disemvowel(string_):
    return ''.join(i for i in string_ if i not in 'AaEeIiOoUu')


print(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")
