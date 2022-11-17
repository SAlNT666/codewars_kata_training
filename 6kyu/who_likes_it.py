import codewars_test as test


def likes(names):
    n = len(names)
    return {0: 'no one likes this',
            1: '{} likes this',
            2: '{} and {} like this',
            3: '{}, {} and {} like this',
            4: '{}, {} and {others} others like this'}[min(4, n)].format(*names[:3], others=n - 2)


@test.it('Basic tests')
def _():
    test.assert_equals(likes([]), 'no one likes this')
    test.assert_equals(likes(['Peter']), 'Peter likes this')
    test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
