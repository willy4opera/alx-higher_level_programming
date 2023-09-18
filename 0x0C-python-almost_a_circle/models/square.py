#!/usr/bin/python3
"""Here we defined the square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """We represent a square."""

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Here, we update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            num1 = 0
            for arg in args:
                if num1 == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif num1 == 1:
                    self.size = arg
                elif num1 == 2:
                    self.x = arg
                elif num1 == 3:
                    self.y = arg
                num1 += 1

        elif kwargs and len(kwargs) != 0:
            for num2, num3 in kwargs.items():
                if num2 == "id":
                    if num3 is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = num3
                elif num2 == "size":
                    self.size = num3
                elif num2 == "x":
                    self.x = num3
                elif num2 == "y":
                    self.y = num3

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        result = "[Square] ({}) {}/{} - {}".format(self.id,
                                                   self.x, self.y,
                                                   self.width)
        return result
