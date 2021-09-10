"""KT4."""

def two_digits_into_list(nr: int) -> list:
    """
    Return list of digits of 2-digit number.

    two_digits_into_list(11) => [1, 1]
    two_digits_into_list(71) => [7, 1]

    :param nr: 2-digit number
    :return: list of length 2
    """
    return [int(a) for a in list(str(nr))]
    pass


def fizzbuzz_series_up(nr: int) -> list:
    """
    Create a list of fizzbuzz series.

    Create a list with the pattern

    [1,   1, 2,   1, 2, 3,   ... 1, 2, 3, 4, 5, 6, 7 .., 14, 15, 16 , .., n],

    where additionally all numbers divisible by 3 are replaced with string "fizz",
    and all numbers divisible by 5 are replaced with string "buzz"
    if number is divisible by 3 and 5, it should be replaced with "fizzbuzz:

    [1,   1, 2,   1, 2, "fizz",   ... 1, 2, "fizz", 4, "buzz", "fizz, 7 .., 14, "fizzbuzz, 16 , .., n]].

    (spaces added to show the grouping).

    If n is not positive, return empty list.

    series_up(3) → [1, 1, 2, 1, 2, "fizz"]

    series_up(2) → [1, 1, 2]

    series_up(4) → [1, 1, 2, 1, 2, "fizz", 1, 2, "fizz", 4]

    series_up(7) → [
                        1,
                        1, 2,
                        1, 2, "fizz",
                        1, 2, "fizz", 4,
                        1, 2, "fizz", 4, "buzz",
                        1, 2, "fizz", 4, "buzz", "fizz",
                        1, 2, "fizz", 4, "buzz", "fizz", 7
                    ]

    series_up(0) → []
    """
    new = []
    if nr <= 0:
        return new
    for i in range(1, nr + 1):
        for s in range(1, i + 1):
            if s % 3 == 0 and s % 5 != 0:
                new.append("fizz")
            elif s % 5 == 0 and s % 3 != 0:
                new.append("buzz")
            elif s % 3 == 0 and s % 5 == 0:
                new.append("fizzbuzz")
            else:
                new.append(s)
    return new

    pass


def min_diff(nums):
    """
    Find the smallest diff between two integer numbers in the list.

    The list will have at least 2 elements.

    min_diff([1, 2, 3]) => 1
    min_diff([1, 9, 17]) => 8
    min_diff([100, 90]) => 10
    min_diff([1, 100, 1000, 1]) => 0

    :param nums: list of ints, at least 2 elements.
    :return: min diff between 2 numbers.
    """
    dif = abs(nums[0] - nums[1])
    for i in range(len(nums)):
        for c in range(len(nums)):
            if i != c:
                if abs(nums[c] - nums[i]) < dif:
                    dif = abs(nums[c] - nums[i])
    return dif



print(min_diff([15, -15, 49]))