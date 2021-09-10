"""Hobbies."""
import csv


def create_list_from_file(file):
    """Collect lines from given file into list."""
    with open(file) as file:  # Opens file "example.txt".
        hobby = file.read().splitlines()  # Reads all the lines from the file and stores it as a string.
        return hobby


def create_dictionary(file):
    """Create dictionary about given peoples' hobbies as Name: [hobby_1, hobby_2]."""
    hobby_dict = {}
    for i in create_list_from_file(file):
        key = i.split(":")[0]
        value = i.split(":")[1]
        if key in hobby_dict:
            if value not in hobby_dict[key]:
                hobby_dict[key].append(value)
        else:
            hobby_dict[key] = [value]
    return hobby_dict


def find_person_with_most_hobbies(file):
    """Find the person (or people) who have more hobbies than others."""
    max_value = len(list(create_dictionary(file).values())[0])
    max_list = []
    for key, value in create_dictionary(file).items():
        if len(value) > max_value:
            max_value = len(value)
            max_list.clear()
            max_list.append(key)
        elif len(value) == max_value:
            max_list.append(key)
    return max_list


def find_person_with_least_hobbies(file):
    """Find the person (or people) who have less hobbies than others."""
    min_value = len(list(create_dictionary(file).values())[0])
    min_list = []
    for key, value in create_dictionary(file).items():
        if len(value) < min_value:
            min_value = len(value)
            min_list.clear()
            min_list.append(key)
        elif len(value) == min_value:
            min_list.append(key)
    return min_list


def find_most_popular_hobby(file):
    """Find the most popular hobby."""
    hobbies = []
    hobbies_count = []
    mostpop_hobby = []
    for i in create_dictionary(file):
        for x in set(create_dictionary(file)[i]):
            hobbies.append(x)
    for x in set(hobbies):
        hobbies_count.append(hobbies.count(x))
    for y in set(hobbies):
        if hobbies.count(y) == max(hobbies_count):
            mostpop_hobby.append(y)
    return mostpop_hobby


def find_least_popular_hobby(file):
    """Find the least popular hobby."""
    hobbies = []
    hobbies_count = []
    leastpop_hobby = []
    for i in create_dictionary(file):
        for x in set(create_dictionary(file)[i]):
            hobbies.append(x)
    for x in set(hobbies):
        hobbies_count.append(hobbies.count(x))
    for y in set(hobbies):
        if hobbies.count(y) == min(hobbies_count):
            leastpop_hobby.append(y)
    return leastpop_hobby


def write_corrected_database(file, file_to_write):
    """
    Write .csv file in a proper way. Use collected and structured data.

    :param file: original file path
    :param file_to_write: file to write result
    """
    with open(file_to_write, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])
        hobby = sorted(create_dictionary(file).items())
        for key, value in hobby:
            writer.writerow([key, "-".join(sorted(value))])


if __name__ == '__main__':
    dic = create_dictionary("hobbies_database.txt")
    print(len(create_list_from_file("hobbies_database.txt")))  # -> 100
    print("Check presence of hobbies for chosen person:")
    print("shopping" in dic["Wendy"])  # -> True
    print("fitness" in dic["Sophie"])  # -> False
    print("gaming" in dic["Peter"])  # -> True
    print("Check if hobbies - person relation is correct:")
    print("Check if a person(people) with the biggest amount of hobbies is(are) correct:")
    print(find_person_with_most_hobbies("hobbies_database.txt"))  # -> ['Jack']
    print(len(dic["Jack"]))  # ->  12
    print(len(dic["Carmen"]))  # -> 10
    print("Check if a person(people) with the smallest amount of hobbies is(are) correct:")
    print(find_person_with_least_hobbies("hobbies_database.txt"))  # -> ['Molly']
    print(len(dic["Molly"]))  # -> 5
    print(len(dic["Sophie"]))  # -> 7
    print("Check if the most popular hobby(ies) is(are) correct")
    print(find_most_popular_hobby("hobbies_database.txt"))  # -> ['gaming', 'sport', 'football']
    print("Check if the least popular hobby(ies) is(are) correct")
    print(find_least_popular_hobby("hobbies_database.txt"))  # -> ['tennis', 'dance', 'puzzles', 'flowers']
    write_corrected_database("hobbies_database.txt", 'correct_hobbies_database.csv')
