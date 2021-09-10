"""KT2."""


def last_to_first(s):
    """
    Move last symbol to the beginning of the string.

    last_to_first("ab") => "ba"
    last_to_first("") => ""
    last_to_first("hello") => "ohell"
    """
    if s == "":
        return ""
    return s[-1] + s[:-1]


print(last_to_first(""))


def have_seven(nums):
    """
    Given a list if ints, return True if the value 7 appears in the list exactly 3 times
    and no consecutive elements have the same value.

    have_seven([1, 2, 3]) => False
    have_seven([7, 1, 7, 7]) => False
    have_seven([7, 1, 7, 1, 7]) => True
    have_seven([7, 1, 7, 1, 1, 7]) => False
    """

    pass


def g_happy(s):
    """
    We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right.

    Return True if all the g's in the given string are happy.

    g_happy("xxggxx") => True
    g_happy("xxgxx") => False
    g_happy("xxggyygxx") => False
    """
    flag = False
    if len(s) < 2:
        return False

    for i in range(len(s) - 1):
        if flag is False and s[i] == "g" and s[i + 1] == "g" or s[i - 1] == "g":
            flag = True
        if flag is True and s[i] == "g" and s[i + 1] != "g" or s[i - 1] != "g":
            flag = False

    return flag


print(g_happy("xxggxx"))
