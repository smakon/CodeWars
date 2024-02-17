"""
Your task is to make a function that can take any non-negative integer as an argument and return it with
its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""


def descending_order(num):
    num = list(str(num))
    num_str = "".join(map(str, sorted(num, reverse=True)))
    return int(num_str)


def some_test():
    assert descending_order(501) == 510
    assert descending_order(0) == 0
    assert descending_order(1) == 1
    assert descending_order(123456789) == 987654321
    assert descending_order(12345607789) == 98776543210
    return 0


print(some_test())
