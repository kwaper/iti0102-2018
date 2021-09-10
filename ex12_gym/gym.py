"""Gym imitation."""


class Trainers:
    """Represents trainers model."""

    def __init__(self, stamina: int, color: str):
        """Item description."""
        self.stamina = stamina
        self.color = color

    def __repr__(self):
        """Item representation."""
        return f"Trainers: [{self.stamina}, {self.color}]"


class Member:
    """Customer."""

    def __init__(self, name: str, age: int, trainers: Trainers):
        """Object description."""
        self.name = name
        self.age = age
        self.trainers = trainers
        self.gyms = []

    def get_all_gyms(self) -> list:
        """All gyms."""
        return self.gyms

    def __repr__(self):
        """Object representation."""
        return f"{self.name}, {self.age}: {self.trainers}"


class Gym:
    """Main place."""

    def __init__(self, name: str, max_members_number: int):
        """Object description."""
        self.name = name
        self.max_members_number = max_members_number
        self.gym_members = []

    def add_member(self, member: Member):
        """Adding member to the gym."""
        if self.can_add_member(member) is False:
            return None

        if len(self.gym_members) == self.max_members_number:
            stamina = min([i.trainers.stamina for i in self.gym_members])
            new = [m for m in self.gym_members if m.trainers.stamina > stamina]
            new.append(member)
            self.gym_members = new
            member.gyms.append(self.name)
            return member
        else:
            self.gym_members.append(member)
            member.gyms.append(self.name)
            return member.gyms

    def can_add_member(self, member: Member) -> bool:
        """Checking."""
        if member.trainers.stamina >= 0 and member.trainers.color and member not in self.gym_members:
            return True
        else:
            return False

    def remove_member(self, member: Member):
        """Removing member."""
        if member in self.gym_members:
            self.gym_members.remove(member)
            member.gyms.remove(self.name)

    def get_total_stamina(self) -> int:
        """Stamina sum."""
        if len(self.gym_members) > 0:
            return sum([i.trainers.stamina for i in self.gym_members])
        else:
            return 0

    def get_members_number(self) -> int:
        """Member sum."""
        return len(self.gym_members)

    def get_all_members(self) -> list:
        """Member list."""
        return self.gym_members

    def get_average_age(self) -> float:
        """Average age."""
        return round(sum([i.age for i in self.gym_members]) / len(self.gym_members), 2)

    def __repr__(self):
        """Place representation."""
        return f"Gym {self.name} : {len(self.gym_members)} member(s)"


class City:
    """Storage of gyms."""

    def __init__(self, max_gym_number: int):
        """Object description."""
        self.max_gym_number = max_gym_number
        self.gyms = []

    def build_gym(self, gym: Gym):
        """Building gym."""
        if self.can_build_gym() is True:
            self.gyms.append(gym)
            return gym

    def can_build_gym(self) -> bool:
        """Check for building gym."""
        return len(self.gyms) < self.max_gym_number

    def destroy_gym(self):
        """Destroying gym."""
        if len(self.gyms) > 0:
            min_member_nums = min([i.get_members_number() for i in self.gyms])
            new = [m for m in self.gyms if m.get_members_number() > min_member_nums]
            self.gyms = new
            return self.gyms

    def get_max_members_gym(self) -> list:
        """List of gyms with max members."""
        gym_max = max([i.get_members_number() for i in self.gyms])
        return [m for m in self.gyms if m.get_members_number() == gym_max]

    def get_max_stamina_gyms(self) -> list:
        """List of gyms with max stamina."""
        stamina_max = max([i.get_total_stamina() for i in self.gyms])
        return [m for m in self.gyms if m.get_total_stamina() == stamina_max]

    def get_max_average_ages(self) -> list:
        """List of gyms with max average age."""
        age_max = max([i.get_average_age() for i in self.gyms])
        return [m for m in self.gyms if m.get_average_age() == age_max]

    def get_min_average_ages(self) -> list:
        """List of gyms with min average age."""
        age_min = min([i.get_average_age() for i in self.gyms])
        return [m for m in self.gyms if m.get_average_age() == age_min]

    def get_gyms_by_trainers_color(self, color: str) -> list:
        """List of gyms with certain trainers color."""
        new = []
        for i in self.gyms:
            if color in [i.trainers.color for i in i.gym_members]:
                new.append(i)
        return sorted(new, key=lambda x: [x.trainers.color for x in x.gym_members].count(color), reverse=True)

    def get_gyms_by_name(self, name: str) -> list:
        """List of gyms with certain name."""
        new = []
        for i in self.gyms:
            if name in [i.name for i in i.gym_members]:
                new.append(i)
        return sorted(new, key=lambda x: [x.name for x in x.gym_members].count(name), reverse=True)

    def get_all_gyms(self) -> list:
        """All gyms in list."""
        return self.gyms
