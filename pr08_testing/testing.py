"""testing shortest way back."""
from shortest_way_back import shortest_way_back
import random


def test_south():
    """testing south direction."""
    assert "N" == shortest_way_back("S")


def test_north():
    """testing north direction."""
    assert "S" == shortest_way_back("N")


def test_east():
    """testing east direction."""
    assert "W" == shortest_way_back("E")


def test_west():
    """testing west direction."""
    assert "E" == shortest_way_back("W")


def test_nothing():
    """testing empty space."""
    assert "" == shortest_way_back("")


def test_same():
    """testing same spot direction."""
    assert "" == shortest_way_back("NSWE")


def test_long():
    """testing long direction."""
    assert "SSSSSSSSSSSSSSS" == shortest_way_back("NNNNNNNNNNNNNNN")


def test_other1():
    """testing direction with 2 chances to go back."""
    assert shortest_way_back("NNSSEWNSES") in ["WN", "NW"]


def test_other2():
    """testing direction with 2 chances to go back."""
    assert shortest_way_back("EEWWNE") in ["SW", "WS"]


def test_other3():
    """testing direction with 2 chances to go back."""
    assert shortest_way_back("SSSNNNWS") in ["NE", "EN"]


def test_other4():
    """testing direction with 2 chances to go back."""
    assert shortest_way_back("EEWWSSNNNW") in ["SE", "ES"]


def test_random():
    """testing random directions."""
    assert shortest_way_back(random.choice(["NESW", "NWSE", "NSWE", "WESN", "SEWN", "SWEN"])) == ""
