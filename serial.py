"""Python serial number generator."""
import random


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """choose a starting number, everytime this method is called"""
        """the starting number will be incremented by 1."""

        self.start = self.next = start

    def __repr__(self):
        """"show representation"""
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):

        self.next += 1
        return self.next - 1

    def generateRandom(self):
        """decided to add a class for generating random serial number"""
        rand = random.randint(1000, 1000000)
        return rand

    def reset(self):
        """Reset number to original start."""

        self.next = self.start
