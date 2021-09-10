"""KT3."""


def duplicate_last(nums: list) -> list:
    """
    Return a list where the last element is doubled.

    In the case of empty list, return empty list.

    duplicate_last([1, 2, 3]) => [1, 2, 3, 3]
    duplicate_last([7]) => [7, 7]
    duplicate_last([]) => []
    """
    new = []
    if len(nums) <= 0:
        return new
    for i in nums:
        new.append(i)
    new.append(nums[-1])
    return new


print(duplicate_last([1, 2, 3]))


def list_query(data: list, query_set: set) -> dict:
    """
    Return dict, where keys are elements from set and values are key counts in data.

    The set does not contain elements which cannot be used as key. Also, the set does not contain True/False.

    list_query(["a", "b", "b", "c"], {"a", "b"}) => {"a": 1, "b": 2}
    list_query(["a", "b", "b", "c"], {"a", "d"}) => {"a": 1, "d": 0}
    list_query(["a", "b", "b", "c"], set()) => {}
    list_query([], {"a", "b"}) => {"a": 1, "b": 2}
    list_query([1, True], {1}) => {1: 1}

    """
    return {i:list.count(i) for i in query_set}


print(list_query(["a", "b", "b", "c"], {"a", "b"}))


def sum_numbers(s):
    """
    Given a string, return the sum of the numbers appearing in the string, ignoring all other characters.

    A number is a series of 1 or more digit chars in a row.

    sum_numbers("abc123xyz") => 123
    sum_numbers("aa11b33") => 44
    sum_numbers("7 11") => 18
    """
    """
        nums = []
        for i in range(len(s)-3):
        if len(s) >= 2 and s[i - 1].isalpha() and s[i].isdigit() and (s[i + 1].isalpha() or None):
            nums.append(int(s[i]))
        if len(s) >= 3 and s[i - 1].isalpha() and s[i:i+2].isdigit() and (s[i + 2].isalpha() or None):
            nums.append(int(s[i:i+2]))
        if len(s) >= 4 and s[i - 1].isalpha() and s[i:i+3].isdigit() and (s[i + 3].isalpha() or None):
            nums.append(int(s[i:i+3]))
    return nums
    """
    return sum(re.findall(r"[\d]+", s))


print(sum_numbers("abc123xyz"))
print(sum_numbers("aa11b33"))
print(sum_numbers("7 11"))
