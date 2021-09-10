"""Pokemons."""
import requests
import random

types = ["poison", "grass", "bug", "ground", "rock", "fire", "electric", "water", "ice", "flying", "fairy",
         "ghost", "normal", "fighting", "psychic", "steel"]


class CannotAddPokemonException(Exception):
    """Custom exception."""


class NoAvailablePokemonsInWorldException(Exception):
    """Custom exception."""


class Person:
    """Simple Person class."""

    def __init__(self, name, age):
        """
        Person constructor.

        :param name: Name of the Person.
        :param age:  Age of the Person.
        """
        self.name = name
        self.age = age
        self.pokemon = None

    def add_pokemon(self, pokemon):
        """
        Add pokemon to Person.

        :param pokemon: Pokemon to add.
        :return:
        """
        if not isinstance(pokemon, Pokemon):
            raise CannotAddPokemonException("Must be instance of Pokemon!")
        elif self.pokemon is not None:
            raise CannotAddPokemonException("Person already has a pokemon!")
        elif self.pokemon is None and pokemon.owner is None:
            self.pokemon = pokemon
            self.pokemon.owner = self

    def get_pokemon(self):
        """
        Get Person's Pokemon.

        :return: Pokemon or None.
        """
        return self.pokemon

    def remove_pokemon(self):
        """Remove Person's Pokemon."""
        if self.pokemon is not None:
            self.pokemon.owner = None
            self.pokemon = None

    def __repr__(self):
        """
        Representation of object.

        :return: Person's name, Person's age, Pokemon: Person's pokemon.
        """
        return f"{self.name}, {self.age}, Pokemon: {self.pokemon}"


class Data:
    """Class for getting data from API."""

    @staticmethod
    def get_all_pokemons_data(url):
        """
        Make request to API.

        :param endpoint: Address where to make the GET request.
        :return: Response data.
        """
        return requests.get(url).json()["results"]

    @staticmethod
    def get_additional_data(url):
        """
        Make request to API to get additional data for each Pokemon.

        :param endpoint: Address where to make the GET request.
        :return: Response data.
        """
        return requests.get(url).json()


class Pokemon:
    """Class for Pokemon."""

    def __init__(self, name, experience, attack, defence, types):
        """
        Class constructor.

        :param name: Pokemon's name.
        :param experience: Pokemon's experience
        :param attack: Pokemon's attack level
        :param defence: Pokemon's defence level.
        :param types: Pokemon's types.
        """
        self.name = name
        self.experience = experience
        self.attack = attack
        self.deff = defence
        self.types = types
        self.power = 0
        self.owner = None

    def get_power(self):
        """
        Calculate power of Pokemon.

        :return: Power.
        """
        self.power = (self.experience / self.attack + self.deff) * len(self.name)
        return self.power

    def __str__(self):
        """
        String representation of object.

        :return: Pokemon's name, experience: Pokemon's experience, att: Pokemon's attack level, def: Pokemon's defence level, types: Pokemon's types.
        """
        return f"{self.name} experience: {self.experience} att: {self.attack} def: {self.deff} types: {self.types}"

    def __repr__(self):
        """
        Object representation.

        :return: Pokemon's name
        """
        return f"{self.name}"


class World:
    """World class."""

    def __init__(self, name):
        """
        Class constructor.

        :param name:
        """
        self.name = name
        self.pokemons = []
        self.available_pokemons = []

    def add_pokemons(self, no_of_pokemons):
        """Add Pokemons to world, GET data from the API."""
        pokemons = Data.get_all_pokemons_data("https://pokeapi.co/api/v2/pokemon/")[:no_of_pokemons]
        for i in pokemons:
            poke_url = requests.get(i["url"]).json()
            poke_name = poke_url["name"].upper()
            poke_exp = poke_url["base_experience"]
            poke_attack = [i for i in poke_url["stats"] if i["stat"]["name"] == "attack"][0]["base_stat"]
            poke_defense = [i for i in poke_url["stats"] if i["stat"]["name"] == "defense"][0]["base_stat"]
            poke_types = [t["name"] for t in [i["type"] for i in poke_url["types"]]]
            pokemon = Pokemon(poke_name, poke_exp, poke_attack, poke_defense, poke_types)
            self.pokemons.append(pokemon)
            self.available_pokemons.append(pokemon)

    def get_pokemons_by_type(self):
        """
        Get Pokemons by type.

        :return: Dict of Pokemons, grouped by types.
        """
        types_dict = {i: [x for x in self.pokemons if i in x.types] for i in types}
        return {i: types_dict[i] for i in types_dict if types_dict[i] != []}

    def hike(self, person: Person):
        """
        Person goes to a hike to find a Pokemon.

        :param person: Person who goes to hike.
        """
        if not self.available_pokemons:
            raise NoAvailablePokemonsInWorldException("Could not find any pokemons.")
        random_poke = random.choice(self.available_pokemons)
        self.remove_available_pokemon(random_poke)
        person.add_pokemon(random_poke)

    def remove_available_pokemon(self, pokemon: Pokemon):
        """
        Remove Pokemon from available Pokemons, which means that the Pokemon got a owner.

        :param pokemon: Pokemon to be removed.
        """
        self.available_pokemons.remove(pokemon)

    def remove_pokemon_from_world(self, pokemon: Pokemon):
        """
        Remove Pokemon from the world, which means that the Pokemon died.

        :param pokemon: Pokemon to be removed.
        """
        if pokemon in self.pokemons:
            self.pokemons.remove(pokemon)
            if pokemon.owner is not None:
                pokemon.owner.remove_pokemon()
            if pokemon in self.available_pokemons:
                self.available_pokemons.remove(pokemon)

    def fight(self, person1: Person, person2: Person):
        """
        Two people fight with their Pokemons.

        :param person1:
        :param person2:
        :return: Pokemon which wins.
        """
        win = person1 if person1.pokemon.get_power() > person2.pokemon.get_power() else person2
        lost = person1 if person1.pokemon.get_power() < person2.pokemon.get_power() else person2
        result = f"There was a battle between {person1.pokemon} and {person2.pokemon} and the winner was {win}"
        self.remove_pokemon_from_world(lost.pokemon)
        return result

    def group_pokemons(self):
        """
        Group Pokemons by given format.

        :return: Dictionary of grouped Pokemons.
        """
        grouped = {"EARTH": [i for i in self.pokemons if i.types[0] in ["poison", "grass", "bug", "ground", "rock"]],
                   "FIRE": [i for i in self.pokemons if i.types[0] in ["fire", "electric"]],
                   "WATER": [i for i in self.pokemons if i.types[0] in ["water", "ice"]],
                   "AIR": [i for i in self.pokemons if i.types[0] in ["flying", "fairy", "ghost"]],
                   "OTHER": [i for i in self.pokemons if i.types[0] in ["normal", "fighting", "psychic", "steel"]]}
        return grouped

    def sort_by_type_experience(self):
        """
        Sort Pokemons by type adn experience. The first Pokemons should be Fire type and experience level of under 100.

        :return: List of sorted Pokemons.
        """
        top = sorted([i for i in self.pokemons if i.types[0] == "fire" and i.experience < 100],
                     key=lambda x: x.experience, reverse=True)
        for i in types:
            new = sorted([x for x in self.pokemons if x.types[0] == i],
                         key=lambda x: x.experience, reverse=True)
            if i == "fire":
                new = sorted([x for x in self.pokemons if x.types[0] == i and x.experience >= 100],
                             key=lambda x: x.experience, reverse=True)
            for p in new:
                top.append(p)
        return top

    def get_most_experienced_pokemon(self):
        """Get the Pokemon(s) which has the maximum experience level."""
        return [i for i in self.pokemons if i.experience == max([i.experience for i in self.pokemons])]

    def get_min_experience_pokemon(self):
        """Get the Pokemon(s) which has the minimum experience level."""
        return [i for i in self.pokemons if i.experience == min([i.experience for i in self.pokemons])]
