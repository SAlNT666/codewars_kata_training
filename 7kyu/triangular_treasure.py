import codewars_test as test


def triangular(n):
    return n > 0 and n * (n + 1) // 2


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(triangular(2), 3)
        test.assert_equals(triangular(4), 10)
        test.assert_equals(triangular(45), 1035)
        test.assert_equals(triangular(-9), 0)
