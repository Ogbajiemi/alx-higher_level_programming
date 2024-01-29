#!/usr/bin/python3

"""
Rectangle Module
"""


class Rectangle:
    """
    A class that defines a rectangle.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        number_of_instances (int): Number of Rectangle instances.
        print_symbol: Symbol for printing.

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than 0.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: Width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """int: Height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): Height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        self._validate_dimension(value, "height")
        self.__height = value

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): Width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        self._validate_dimension(value, "width")
        self.__width = value

    def _validate_dimension(self, value, dimension_name):
        """
        Validates a dimension value.

        Args:
            value (int): Dimension value.
            dimension_name (str): Name of the dimension.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{dimension_name} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension_name} must be >= 0")

    def area(self):
        """
        Area calculator.

        Returns:
            int: Area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Perimeter calculator.

        Returns:
            int: Perimeter.
        """
        return 2 * (self.__width + self.__height) if self.__width != 0 and self.__height != 0 else 0

    def __str__(self):
        """
        String representation of the rectangle.

        Returns:
            str: Rectangle.
        """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        for i in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width
            if i != (self.__height - 1):
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
        String representation of the function call.

        Returns:
            str: Function call.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor method."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

