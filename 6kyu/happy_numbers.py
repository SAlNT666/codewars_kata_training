import codewars_test as test


def is_happy(n):
    while n > 4:
        r = 0
        while n:
            r, n = r + (n % 10) ** 2, n // 10
        n = r
    return n == 1


@test.it("Should obtain correct answer for fixed tests where n IS n happy number")
def test_is_happy_fixed():
    test.assert_equals(is_happy(1), True, "Returned solution incorrect for fixed test with n = 1, 1 is n happy number")
    test.assert_equals(is_happy(7), True, "Returned solution incorrect for fixed test with n = 7, 7 is n happy number")
    test.assert_equals(is_happy(901), True,
                       "Returned solution incorrect for fixed test with n = 901, 901 is n happy number")
