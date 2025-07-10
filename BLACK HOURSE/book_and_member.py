# book_and_member.py

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn  # Private attribute
        self.available = True

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.__isbn}, Available: {self.available}")

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn


class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id  # Private attribute
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'")

    def get_membership_id(self):
        return self.__membership_id

    def set_membership_id(self, new_id):
        self.__membership_id = new_id


# Example usage
if __name__ == "__main__":
    book1 = Book("Python Basics", "Ali Hassan", "111")
    book2 = Book("OOP in Python", "Nour Ahmed", "222")

    member = Member("Sara", "M001")

    book1.display_info()
    member.borrow_book(book1)
    member.return_book(book1)
