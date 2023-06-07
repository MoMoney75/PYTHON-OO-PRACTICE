"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """takes a path to a file as a paramater and opens it"""
    """uses the built in OPEN method. The open() function returns"""
    """a file object, which has a read() method for reading the content of the file:"""

    def __init__(self, path):
        file = open(path)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in file
                if w.strip() and not w.startswith("#")]
