import shelve

class Library:
    def __init__(self, fn):
        pass

    def add(self, book):
        pass

    def get_by_isbn(self, isbn):
        pass

    def get_by_title(self, title):
        pass

    def get_by_author(self, author):
        pass

    def close(self):
        pass

class Book:
    def __init__(self, isbn, title, authors):
        self.isbn, self.title, self.authors = isbn, title, authors

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

class Author:
    def __init__(self, first_name, middle_name, last_name):
        self.first_name, self.middle_name, self.last_name = first_name, middle_name, last_name

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
