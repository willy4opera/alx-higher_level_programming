#!/usr/bin/python3

"""Here, we defined the base model class."""
import turtle
import json
import csv

class Base:
    """Here we defined the Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """We initialized the new  base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(dict_list):
        """Return the JSON serialization of a list of dicts.

        Args:
            dict_list (list): A list of dictionaries.
        """
        if dict_list is None or dict_list == []:
            return "[]"
        return json.dumps(dict_list)

    @classmethod
    def save_to_file(clrs, Obj_list):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            Obj_list (list): A list of inherited Base instances.
        """
        f_name = clrs.__name__ + ".json"
        with open(f_name, "w") as jsonfile:
            if Obj_list is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in Obj_list]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(string_json):
        """Return the deserialization of a JSON string.

        Args:
            string_json (str): A JSON str representation of a list of dicts.
        Returns:
            If string_json is None or empty - an empty list.
            Otherwise - the Python list represented by string_json.
        """
        if string_json is None or string_json == "[]":
            return []
        return json.loads(string_json)

    @classmethod
    def create(clrs, **dev_dict):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dev_dict and dev_dict != {}:
            if clrs.__name__ == "Rectangle":
                dev_new = clrs(1, 1)
            else:
                dev_new = clrs(1)
            dev_new.update(**dev_dict)
            return dev_new

    @classmethod
    def load_from_file(clrs):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<clrs.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        f_name = str(clrs.__name__) + ".json"
        try:
            with open(f_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [clrs.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(clrs, Obj_list):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            Obj_list (list): A list of inherited Base instances.
        """
        f_name = clrs.__name__ + ".csv"
        with open(f_name, "w", newline="") as csvfile:
            if Obj_list is None or Obj_list == []:
                csvfile.write("[]")
            else:
                if clrs.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in Obj_list:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(clrs):
        """Here, we return a list of classes instantiated from a CSV file.

        Reads from `<clrs.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        f_name = clrs.__name__ + ".csv"
        try:
            with open(f_name, "r", newline="") as csvfile:
                if clrs.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [clrs.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(rect_list, sqr_list):
        """Here we draw Rectangles and Squares using the turtle module.

        Args:
            rect_list (list): A list of Rectangle objects to draw.
            sqr_list (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in rect_list:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in sqr_list:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
