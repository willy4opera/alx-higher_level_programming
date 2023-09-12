#!/usr/bin/python3

"""Here, we defined the class Student."""


class Student:
    """Here, we represent a student."""

    def __init__(self, first_name, last_name, age):
        """Here, we initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        result = self.__dict__
        return result
