"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""
from abc import ABC, abstractmethod

# abstract class Shape
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def set_values(self, x, y):
        pass


class Rectangle(Shape):
    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if width >= 0:
            self.__width = width
        else:
            raise ValueError("Width must be a non-negative value")

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height >= 0:
            self.__height = height
        else:
            raise ValueError("Height must be a non-negative value")


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle()

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
