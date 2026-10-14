'''
Write a python program that allows a librarian to add several books to a library.
For each book, ask the user to enter its title and number of copies.
Store each book and its available copies in a dictionary.

After the books have been added, display a menu that lets the user issue a book, return a book, display
all books or exit the program.

Appy these conditions:
- Book titles should be compared without distinguishing uppercase and lowercase letters.
- A book can be issued only if it exists in the libraray and at least one copy is available.
- Issueing a book decreases its availablw copy count by one
- A book can only be returned if it exists in the library and at least one copy has already been issued.
- Display an appropriate message fr an unavailable book, an invalid choice or an invalid number of copies.
'''


class Library:
    def __init__(self):
        self.books = dict()

    def add_book(self, title: str, copies: int):
        title_lower = title.lower()

        if copies <= 0:
            print("Invalid number of copies")
            return

        if title_lower in self.books:
            self.books[title_lower][0] += copies
            self.books[title_lower][1] += copies
        else:
            self.books[title_lower] = [copies, copies]

    def issue_book(self, title: str):
        title_lower = title.lower()

        if title_lower not in self.books or self.books[title_lower][1] == 0:
            print("Sorry! This book is not available")
            return

        self.books[title_lower][1] -= 1
        print(f"{title.title()} issued successfully!")

    def return_book(self, title: str):
        title_lower = title.lower()

        if (title_lower not in self.books or
                self.books[title_lower][1] == self.books[title_lower][0]):
            print("No issued copy of this book to return")
            return

        self.books[title_lower][1] += 1
        print(f"{title.title()} returned successfully")

    def display_books(self):
        print(f"{'Book Title':<45}{'Total':>8}{'Available':>12}")
        for k, v in self.books.items():
            print(f"{k.title():<45}{v[0]:>8}{v[1]:>12}")


# Sample data
def add_sample_books(my_lib):
    books = [
        ["The Alchemist", 8],
        ["Harry Potter and the Philosopher's Stone", 12],
        ["The Hobbit", 5],
        ["Pride and Prejudice", 7],
        ["1984", 9],
        ["To Kill a Mockingbird", 6],
        ["The Great Gatsby", 4],
        ["Animal Farm", 10],
        ["The Catcher in the Rye", 3],
        ["The Lord of the Rings", 8],
        ["The Kite Runner", 6],
        ["A Thousand Splendid Suns", 5],
        ["The Fault in Our Stars", 11],
        ["Looking for Alaska", 4],
        ["The Book Thief", 7],
        ["The Hunger Games", 9],
        ["Catching Fire", 6],
        ["Mockingjay", 5],
        ["The Da Vinci Code", 8],
        ["Angels & Demons", 4],
        ["Inferno", 7],
        ["Sherlock Holmes: The Complete Novels", 10],
        ["Murder on the Orient Express", 6],
        ["And Then There Were None", 9],
        ["The Silent Patient", 5],
        ["Gone Girl", 7],
        ["It Ends with Us", 12],
        ["Verity", 8],
        ["November 9", 4],
        ["The Midnight Library", 6],
        ["The Picture of Dorian Gray", 3],
        ["Jane Eyre", 5],
        ["Wuthering Heights", 4],
        ["Little Women", 7],
        ["The Old Man and the Sea", 9],
        ["The Chronicles of Narnia", 6],
        ["Dune", 5],
        ["The Martian", 8],
        ["Project Hail Mary", 4],
        ["The Shining", 7],
        ["It", 3],
        ["Dracula", 6],
        ["Frankenstein", 5],
        ["The Three Musketeers", 4],
        ["Les Misérables", 3],
        ["The White Tiger", 8],
        ["Train to Pakistan", 6],
        ["The Guide", 5],
        ["Five Point Someone", 10],
        ["The Immortals of Meluha", 9]
    ]
    for book in books:
        my_lib.add_book(book[0], book[1])


print("=====LIBRARY MANAGEMENT=====")
my_lib = Library()
add_sample_books(my_lib)
while (1):
    print("1. Add books")
    print("2. Issue book")
    print("3. Return book")
    print("4. Display all books")
    print("5. Exit")
    choice = input("Enter Option: ")
    if choice.isdigit():
        choice = int(choice)
    else:
        print("Invalid choice")
        continue
    if choice == "1":
        n = int(input("Enter number of distinct books to add: "))
        for i in range(n):
            t = input("Enter book title: ")
            c = int(input("Enter number of copies: "))
            if c <= 0:
                print("Invalid number of copies")
                i -= 1
            my_lib.add_book(t, c)

    elif choice == 2:
        t = input("Enter Book Title: ")
        my_lib.issue_book(t)
    elif choice == 3:
        t = input("Enter Book Title: ")
        my_lib.return_book(t)
    elif choice == 4:
        my_lib.display_books()
    elif choice == 5:
        exit(0)
    else:
        print("Invalid choice")