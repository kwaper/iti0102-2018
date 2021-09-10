"""Test 1 (t12)."""


def has23(nums):
    """
    Given an int array length 2, return True if it contains a 2 or a 3.

    has23([2, 5]) → True
    has23([4, 3]) → True
    has23([4, 5]) → False

    :param nums: list of integers.
    :return: True if the list contains a 2 or a 3.
    """
    num = nums[0:2]
    if num[0] == 2 or num[1] == 2:
        return True
    elif num[0] == 3 or num[1] == 3:
        return True
    else:
        return False
    pass


def near_ten(nr):
    """
    Given a non-negative number "num", return True if num is within 2 of a multiple of 10.

    near_ten(0) →  True
    near_ten(3) →  False
    near_ten(10) →  True
    near_ten(23) →  False
    near_ten(198) →  True

    :param nr: non-negative integer.
    :return: True if num is within 2 of a multiple of 10.
    """
    if (nr % 10) >= 8 or (nr % 10) == 0 or (nr % 10) <= 2:
        return True
    else:
        return False
    pass


def left2(s):
    """
    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.

    The string length will be at least 2.

    left2('Hello') → 'lloHe'
    left2('java') → 'vaja'
    left2('Hi') → 'Hi'
    :param s: input string.
    :return: "rotated" string.
    """
    s = s[2:len(s)] + s[:2]
    return s
    pass


def num_as_index(nums):
    """
    Return element which index is the value of the smaller of the first and the last element.

    If there is no such element (index is too high), return the smaller of the first and the last element.

    num_as_index([1, 2, 3]) => 2
    num_as_index([4, 5, 6]) => 4
    num_as_index([0, 1, 0]) => 0
    num_as_index([3, 5, 6, 1, 1]) => 5

    :param nums: list of non-negative integers.
    :return: element value in the specific index.
    """
    for i in range(10):
        if nums.index(i) <= nums.index([0]) and nums.index(i) < nums.index([-1]):
            return nums(nums.index(i))
        else:
            return num_as_index(min(nums))


def remove_in_middle(text, to_remove):
    """
    Remove substring from the text, except for the first and the last occurrence.

    remove_in_middle("abc", "def") => "abc"
    remove_in_middle("abcabcabc", "abc") => "abcabc"
    remove_in_middle("abcdabceabcabc", "abc") => "abcdeabc"
    remove_in_middle("abcd", "abc") => "abcd"
    remove_in_middle("abcdabc", "abc") => "abcdabc"
    remove_in_middle("ABCAaaaAA", "a") => "ABCAaaAA

    :param text: string from where the remove takes place.
    :param to_remove: substring to be removed.
    :return: string with middle substrings removed.
    """
    pass


if __name__ == '__main__':
    print(has23([2, 5]))
    print(near_ten(3))
    print(left2('Hello'))
    print(num_as_index([1, 2, 3]))
    print(remove_in_middle("abcabcabc", "abc"))
