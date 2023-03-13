# https://www.codewars.com/kata/54a91a4883a7de5d7800009c
import codewars_test as test


def increment_string(strng):
    head = strng.rstrip('0123456789')
    if head == strng:
        return strng + '1'
    else:
        tail = strng[len(head):]
        return head + str(int(tail) + 1).rjust(len(tail), '0')


test.assert_equals(increment_string("foo"), "foo1")
test.assert_equals(increment_string("foobar001"), "foobar002")
test.assert_equals(increment_string("foobar1"), "foobar2")
test.assert_equals(increment_string("foobar00"), "foobar01")
test.assert_equals(increment_string("foobar99"), "foobar100")
test.assert_equals(increment_string("foobar099"), "foobar100")
test.assert_equals(increment_string("fo99obar99"), "fo99obar100")
test.assert_equals(increment_string(""), "1")
