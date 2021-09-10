"""Find the shortest way back in a taxicab geometry."""


def shortest_way_back(path: str) -> str:
    """
    Find the shortest way back in a taxicab geometry.

    :param path: string of moves, where moves are encoded as follows:.
    N - north -  (1, 0)
    S - south -  (-1, 0)
    E - east  -  (0, 1)
    W - west  -  (0, -1)
    (first coordinate indicates steps towards north,
    second coordinate indicates steps towards east)

    :return: the shortest way back encoded the same way as :param path:.
    """
    d = {"N": (1, 0),
         "S": (-1, 0),
         "E": (0, 1),
         "W": (0, -1)}
    pos = (0, 0)
    back = ""
    for direct in path:
        pos = (pos[0] + d[direct][0], pos[1] + d[direct][1])
    print(pos)
    while pos != (0, 0):
        if pos[0] != 0:
            while pos[0] > 0:
                pos = (pos[0] - 1, pos[1])
                back += "S"
            while pos[0] < 0:
                pos = (pos[0] + 1, pos[1])
                back += "N"
        if pos[1] != 0:
            while pos[1] > 0:
                pos = (pos[0], pos[1] - 1)
                back += "W"
            while pos[1] < 0:
                pos = (pos[0], pos[1] + 1)
                back += "E"
    return back


if __name__ == '__main__':
    assert shortest_way_back("NNN") == "SSS"
    assert shortest_way_back("SS") == "NN"
    assert shortest_way_back("E") == "W"
    assert shortest_way_back("WWWW") == "EEEE"

    assert shortest_way_back("") == ""
    assert shortest_way_back("NESW") == ""

    assert shortest_way_back("NNEESEW") in ["SWW", "WSW", "WWS"]
