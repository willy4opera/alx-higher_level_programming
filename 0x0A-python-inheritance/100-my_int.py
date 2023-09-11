#!/usr/bin/python3

"""Here, we defined a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        res = self.real != value
        return res
    def __ne__(self, value):
        """Override != operator with == behavior."""
        res = self.real == value
        return res
