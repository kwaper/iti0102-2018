"""Sorting."""


def number_of_vowels(string: str):
    """Find the number of vowels(a, e, i, o, u) in word."""
    count = 0
    for letter in string.lower():
        if letter in ["a", "e", "i", "o", "u"]:
            count += 1  # count += 1
    return count


def word_with_most_vowels(string_list: list):
    """Find and return the string with most vowels in the list."""
    max_count = 0
    string_index = 0
    # list(0, element)
    for i, string in enumerate(string_list):
        vowels = number_of_vowels(string)
        if max_count < vowels:
            max_count = vowels
            string_index = i
    return string_list[string_index]


def sort_list(string_list: list):
    """Sort the list by the number of vowels in the string."""
    new_list = []
    for _ in range(len(string_list)):
        max_vowels = word_with_most_vowels(string_list)
        new_list.append(max_vowels)
        string_list.remove(max_vowels)
    return new_list


if __name__ == "__main__":
    print(sort_list(["lololo", "LooOOoser", "winnerIIIIIiii"]))
