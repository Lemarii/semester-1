# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name, birth):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name == "":
            raise ValueError("name must not be empty")
        if not isinstance(birth, date):
            raise TypeError("birth must be a date")

        self.name = name
        self.birth = birth

    def initials(self):
        """Return the uppercase initial of each part of the person's name."""
        return "".join(part[0].upper() for part in self.name.split())

    def is_birthday(self):
        """Return whether today is the person's birthday."""
        today = date.today()
        return self.birth.month == today.month and self.birth.day == today.day
