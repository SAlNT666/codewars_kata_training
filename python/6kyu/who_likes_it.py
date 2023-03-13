# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names):
    n = len(names)
    return {0: 'no one likes this',
            1: '{} likes this',
            2: '{} and {} like this',
            3: '{}, {} and {} like this',
            4: '{}, {} and {others} others like this'}[min(4, n)].format(*names[:3], others=n - 2)


print(likes([]), 'no one likes this', sep='\n', end='\n\n')
print(likes(['Peter']), 'Peter likes this', sep='\n', end='\n\n')
print(likes(['Jacob', 'Alex']), 'Jacob and Alex like this', sep='\n', end='\n\n')
print(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this', sep='\n', end='\n\n')
print(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this', sep='\n', end='\n\n')
