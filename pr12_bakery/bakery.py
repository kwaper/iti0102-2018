"""Bakery imitation."""


class Baker:
    """Baker."""

    def __init__(self, name: str, experience_level: int, money: int):
        """Baker model."""
        self.name = name
        self.experience_level = experience_level
        self.money = money

    def __repr__(self):
        """Baker representation."""
        return f"Baker: {self.name}({self.experience_level})"


class Pastry:
    """Pastry."""

    def __init__(self, name: str, complexity_level: int):
        """Pastry model."""
        self.collection = {}
        self.name = name
        self.complexity_level = complexity_level

    def __repr__(self):
        """Pastry representation."""
        return f"{self.name}"


class Bakery:
    """Bakery."""

    def __init__(self, name: str, min_experience_level: int, budget: int):
        """Bakery model."""
        self.personal = []
        self.name = name
        self.min_experience_level = min_experience_level
        self.budget = budget
        self.recipes = {}
        self.bakers = []
        self.xp = []
        self.pastries = []

    def add_baker(self, baker: Baker) -> Baker:
        """Giving work to bakers."""
        if baker.experience_level >= self.min_experience_level:
            self.personal.append(baker)
            self.xp.append(baker.experience_level)
            return Baker(baker.name, baker.experience_level, baker.money)

    def remove_baker(self, baker: Baker):
        """Taking work back from bakers."""
        if baker in self.personal:
            self.personal.remove(baker)

    def add_recipe(self, name: str):
        """Adding recipe to recipe book."""
        if len(self.personal) > 0:
            if name not in self.recipes:
                if self.budget >= len(name):
                    complexity_level = abs(len(name) * len(self.personal) - min(self.xp))
                    self.recipes[name] = complexity_level
                    self.budget -= len(name)

    def make_order(self, name: str) -> Pastry:
        """That how we complete orders."""
        if name in self.recipes:
            if len(self.personal) > 0:
                for i in self.xp:
                    if i >= self.recipes[name]:
                        worker = min(self.personal,
                                     key=lambda x: x.experience_level if x.experience_level >= self.recipes[
                                         name] else False)
                        worker.experience_level += len(name)
                        worker.money += (len(name) * 2)
                        print(worker)
                        self.budget += (len(name) * 2)
                        self.min_experience_level += 1
                        self.pastries.append(name)
                        return Pastry(name, self.recipes[name])

    def get_recipes(self) -> dict:
        """Get all recipes."""
        return self.recipes

    def get_pastries(self) -> list:
        """Get all done pastries."""
        new = []
        for i in self.pastries:
            new.append(Pastry(i, self.recipes[i]))
        return sorted(new, key=lambda c: c.complexity_level, reverse=True)

    def get_bakers(self) -> list:
        """Get all workers."""
        return sorted(self.personal, key=lambda x: x.experience_level, reverse=True)

    def __repr__(self):
        """Working place representation."""
        return f"Bakery {self.name}: {len(self.personal)} baker(s)"
