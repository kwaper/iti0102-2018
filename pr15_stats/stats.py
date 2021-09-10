"""PR15 Statistics - lambdas."""


class Person:
    """Represent a person."""

    def __init__(self, first_name, last_name, email, gender, age):
        """Object description."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.age = age

    def __repr__(self):
        """Object representation."""
        return f"{self.first_name}"


def get_oldest_person(person_list):
    """Return the person with the highest age."""
    return max(person_list, key=lambda x: x.age)


def get_person_with_shortest_name(person_list):
    """Return the person with the shortest name (first name + last name)."""
    return min(person_list, key=lambda x: (len(x.first_name) + len(x.last_name)))


def get_all_underage_people(person_list):
    """Return a list of all underage (under 18) people in the given list."""
    return [x for x in person_list if x.age < 18]


def filter_list_by_gender(person_list, gender):
    """Filter the given list by the given gender."""
    return [x for x in person_list if x.gender == gender]


def get_people_with_government_emails(person_list):
    """Return a list of all people with an email ending with '.gov'."""
    return [x for x in person_list if x.email[-4:] == ".gov"]


def sort_list_by_email_length(person_list):
    """Sort the given list by the length of a persons email in ascending order."""
    return sorted(person_list, key=lambda x: len(x.email))


def get_list_of_all_names_in_uppercase(person_list):
    """Return a list of the first names of all persons in the list, in uppercase."""
    return [x.first_name.upper() for x in person_list]


if __name__ == "__main__":
    jack = Person("Jack", "O'Neill", "jack@sgone.com", "Male", 50)
    sam = Person("Samantha", "Carter", "sam@sgone.com", "Female", 41)
    hammond = Person("George", "Hammond", "george.hammond@usaf.gov", "Male", 65)
    ryac = Person("Rya'c", "Teal'cson", "ryac@chulak.sg", "Male", 12)
    cassie = Person("Cassandra", "Fraiser", "cassandra@gmail.sg", "Female", 16)

    person_list = [jack, sam, hammond, ryac, cassie]

    # siin näidetes on return-väärtustele viidatud kui objektidele, mitte sõnedele - tagastatav väärtus sõne kujul ei ole tähtis
    # (selguse mõttes võite endale kirjutada __repr__ funktsiooni, kui tahtate näha, mis objekti funktsioon tagastab)

    print(get_oldest_person(person_list))  # hammond
    print(get_person_with_shortest_name(person_list))  # jack
    print(get_all_underage_people(person_list))  # [ryac, cassie]
    print(filter_list_by_gender(person_list, "Female"))  # [sam, cassie]
    print(get_people_with_government_emails(person_list))  # [hammond]
    print(sort_list_by_email_length(person_list))  # [sam, jack, ryac, cassie, hammond]
    print(get_list_of_all_names_in_uppercase(person_list))  # ["JACK", "SAMANTHA", ...]
