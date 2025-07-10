from book_and_member import Book

class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id
        self.borrowed_books = []

class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, title, author, isbn):
        new_book = Book(title, author, isbn)
        library.books.append(new_book)
        print(f"{self.name} added book '{title}' to the library")


class Library:
    def __init__(self):
        self.books = []

    def display_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books:
                book.display_info()

if __name__ == "__main__":
    library = Library()
    staff = StaffMember("Ahmed", "M123", "S001")

    staff.add_book(library, "Algorithms", "Dr. Omar", "333")
    library.display_books()
