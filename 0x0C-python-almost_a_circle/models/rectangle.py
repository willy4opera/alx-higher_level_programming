#!/usr/bin/python3
"""Here, we defined a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Here, we represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """we Here, we set/ get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Here, we set/ get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Here, we set/ getthe x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Here, we set/ get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """We return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            num1 = 0
            for arg in args:
                if num1 == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif num1 == 1:
                    self.width = arg
                elif num1 == 2:
                    self.height = arg
                elif num1 == 3:
                    self.x = arg
                elif num1 == 4:
                    self.y = arg
                num1 += 1

        elif kwargs and len(kwargs) != 0:
            for num2, num3 in kwargs.items():
                if num2 == "id":
                    if num3 is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = num3
                elif num2 == "width":
                    self.width = num3
                elif num2 == "height":
                    self.height = num3
                elif num2 == "x":
                    self.x = num3
                elif num2 == "y":
                    self.y = num3

    def to_dictionary(self):
        """We return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """We return the print() and str() representation of the Rectangle."""
        result = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                         self.x, self.y,
                                                         self.width,
                                                         self.height)
        return result