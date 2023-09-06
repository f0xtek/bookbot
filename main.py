"""
Provide statistical data about books
"""
from pathlib import Path


class Book:
    """
    A book with a given path
    """

    def __init__(self, path):
        self.path = path
        self.__content = self.__read_contents()

    def __read_contents(self):
        """
        Return the contents of the book
        """
        with open(self.path, "r", encoding="utf-8") as content:
            return content.read()

    def num_words(self):
        """
        Count the number of words in the book's content
        """
        return len(self.__content.split())

    def num_letters(self):
        """
        Return a dictionary containing the number of times
        a letter appears in the book's content.
        """
        results = {}
        for char in self.__content:
            char = char.lower()
            if char.isalpha():
                if char not in results:
                    results[char] = 1
                else:
                    results[char] += 1
        return results

    def print_report(self):
        """
        Print a summary of the book's content
        """
        print(f"--- Begin report of {self.path} ---")
        print(f"{self.num_words()} words found in the document", end="\n\n")
        for char in sorted(
                self.num_letters().items(),
                key=lambda x: x[1],
                reverse=True):
            print(f"The '{char[0]}' character was found {char[1]} times")
        print("--- End report ---", end="\n\n")


if __name__ == "__main__":
    for item in Path("books").iterdir():
        book = Book(item)
        book.print_report()
