"""Having fun."""


def recursive_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using recursion.

    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    if len(numbers) > 1 and numbers[0] % 2 == 0:
        return numbers[0] + recursive_sum(numbers[1:])
    elif len(numbers) > 1 and numbers[0] % 2 != 0:
        return recursive_sum(numbers[1:])
    elif len(numbers) == 1 and numbers[0] % 2 == 0:
        return numbers[0]
    else:
        return 0


def loop_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using loops.

    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    nums = 0
    for i in numbers:
        if i % 2 == 0:
            nums += i
        else:
            nums += 0
    return nums
    pass


def loop_reverse(s: str) -> str:
    """Reverse a string using a loop.

    :param s: string
    :return: reverse of s
    """
    lis = []
    for i in s:
        lis += i
    lis.reverse()
    return "".join(lis)


def recursive_reverse(s: str) -> str:
    """Reverse a string using recursion.

    :param s: string
    :return: reverse of s
    """
    if len(s) <= 1:
        return s
    else:
        return s[-1] + recursive_reverse(s[:-1])


if __name__ == '__main__':
    print(recursive_sum([1, 3, 5, 7, 9]))
    print(recursive_sum([2, 4, 5, 8]))
    print(loop_sum([1, 3, 5, 7, 9]))
    print(loop_sum([2, 4, 5, 8]))
    print(recursive_reverse("abcdef"))
    print(loop_reverse("abcdef"))
