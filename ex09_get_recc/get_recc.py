"""Make life easier whilst volunteering in a French language camp."""


def count_portions(number_of_participants: int, day: int) -> int:
    """
    Count the total of portions served to participants during the camp recursively.

    There are 4 meals in each day and we expect that every participant eats 1 portion
    per meal. At the end of each day one participant leaves the camp and is not ours to
    feed.

    We are only counting the participants' meals, the organisers and volunteers
    eat separately. In case of negative participants or days the number of meals is
    still 0.

    count_portions(0, 7) == 0
    count_portions(6, 0) == 0
    count_portions(-8, 5) == 0
    count_portions(9, -5) == 0

    count_portions(6, 1) == 24
    count_portions(6, 2) == 44
    count_portions(6, 3) == 60

    :param number_of_participants: the initial number of participants.
    :param day: the specified day.
    :return: a total of portions served during the camp at the end of the specified day.
    """
    if number_of_participants <= 0 or day <= 0:
        return 0
    elif number_of_participants > 0 and day == 1:
        return number_of_participants * 4
    elif number_of_participants > 0 and day > 1:
        return (number_of_participants * 4) + count_portions(number_of_participants - 1, day - 1)
    pass


def names_to_be_eliminated(points_dict: dict, names: set = None, lowest_score: int = None) -> set:
    """
    Recursively find the names that are to be eliminated.

    When two or more people have the same lowest score, return a set in which every lowest
    scoring person is listed.

    names_to_be_eliminated({}) == set()
    names_to_be_eliminated({"Dylan": 10}) == {"Dylan"}
    names_to_be_eliminated({"Carl": 4, "Bert": -10}) == {"Bert"}
    names_to_be_eliminated({"Terry": 4, "Pete": 4}) == {"Terry", "Pete"}

    :param points_dict: dictionary containing name strings as
                        keys and points integers as values.
    :param names: helper to store current names
    :param lowest_score: helper to store current lowest score
    :return: set of names of lowest scoring people.
    """
    name = list(points_dict.keys())
    values = list(points_dict.values())
    if len(points_dict) == 0:
        return set()
    if names is None:
        names = [name[0]]
    elif len(names) != 0:
        names = list(names)
    if len(name) <= 1:
        return set(names)
    else:
        if values[0] > values[1]:
            names.clear()
            names.append(name[1])
            points_dict.pop(name[0])
            return names_to_be_eliminated(points_dict, set(names))
        elif values[0] < values[1]:
            points_dict.pop(name[1])
            return names_to_be_eliminated(points_dict, set(names))
        if values[0] == values[1]:
            names.append(name[1])
            points_dict.pop(name[0])
            return names_to_be_eliminated(points_dict, set(names))


def people_in_the_know(hours_passed, cache: dict = None) -> int:
    """
    Return the number of people who know a rumor given the hours passed from the initial release.

    Every hour there is a recess where everybody can talk to everybody. Rumors always spread in
    the same fashion: everybody who are in the know are silent one recess after the recess they
    were told of the rumor. After that they begin to pass it on, one person per recess.

    people_in_the_know(0) == 0
    people_in_the_know(1) == 1
    people_in_the_know(2) == 1
    people_in_the_know(3) == 2
    people_in_the_know(4) == 3
    people_in_the_know(7) == 13

    :param hours_passed: the hours passed from the initial release.
    :param cache: helper to store already calculated results.
    :return: the number of people that have heard the rumor.
    """
    if cache is None and hours_passed > 0:
        cache = {"all": 1, "wait": 1, "go_wait": 1}
    elif cache is not None:
        cache["all"] = cache["wait"]
        cache["wait"] = cache["all"] + cache["go_wait"]
        cache["go_wait"] = cache["all"]
    if hours_passed < 2:
        if cache is not None:
            return cache["all"]
        else:
            return 0
    else:
        return people_in_the_know(hours_passed - 1, cache)


def traversable_coordinates(world_map: list, coord: tuple = (0, 0), traversable_coords: set = None) -> set:
    """
    Return the coordinates that are traversable by humans or adjacent to traversable coordinates.

    Given a two-dimensional list as a map, give the coordinates of traversable cells with the
    coordinates of cells which are adjacent to traversable cells with respect to the
    beginning coordinate.

    If there is not a traversable path from the beginning coordinate
    to the traversable cell, the traversable cell coordinate is not returned. Traversable
    cells are represented by empty strings. If the beginning coordinate cell is not traversable,
    return empty set.

    Coordinates are in the format (row, column). Negative coordinate values are considered invalid.
    world_map is not necessarily rectangular. Paths can be made through a diagonal.

    traversable_coordinates([]) == set()
    traversable_coordinates([[]]) == set()
    traversable_coordinates([["", "", ""]], (5, 2)) == set()
    traversable_coordinates([["1", "1", ""]], (-4, -9)) == set()
    traversable_coordinates([["1", [], "1"]], (0, 1)) == set()

    world = [["1", "1", "1", "1", "1"],
             ["1", "1", "1",  "", "1"],
             ["1", "1",  "", "1", "1"],
             ["1", "1",  "", "1", "1"],
             ["1", "1", "1", "1", "1"]]

    traversable = {(0, 2), (0, 3), (0, 4),
                   (1, 1), (1, 2), (1, 3), (1, 4),
                   (2, 1), (2, 2), (2, 3), (2, 4),
                   (3, 1), (3, 2), (3, 3),
                   (4, 1), (4, 2), (4, 3)}

    traversable_coordinates(world, (2, 2)) == traversable

    :param world_map: two-dimensional list of strings.
    :param coord: the (beginning) coordinate.
    :param traversable_coords: helper to store traversable coordinates.
    :return: set of traversable and traversable-adjacent cell
            coordinate tuples with respect to starting coord
    """
    if coord[0] < 0 or coord[0] > len(world_map) - 1 or coord[1] < 0 or coord[1] > len(world_map[coord[0]]) - 1 or \
            world_map[coord[0]][coord[1]] is "1":
        return set()
    a = {coord: world_map[coord[0]][coord[1]]}
    if traversable_coords is None:
        traversable_coords = [(coord[0], coord[1])]
    for i, b in enumerate(world_map):
        for c, d in enumerate(b):
            a[(i, c)] = d

    circle = []
    for i in range(-1, 2):
        for c in range(-1, 2):
            if (coord[0] + i, coord[1] + c) in a:
                traversable_coords.append((coord[0] + i, coord[1] + c))
                if a[(coord[0] + i, coord[1] + c)] is "":
                    circle.append((coord[0] + i, coord[1] + c))
    for i in circle:
        world_map[coord[0]].pop(coord[1])
        world_map[coord[0]].insert(coord[1], "1")
        traversable_coords.extend(list(traversable_coordinates(world_map, (i[0], i[1]))))

    return set(traversable_coords)

    pass
