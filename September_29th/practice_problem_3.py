'''
Write a Python Program to manage a small library using a dictionary.
The program must repeatedly allow the user to add books, issue books,return books, and display the current book record.

Conditions:
    1. Store book title as key and available copies as the value
    2. A book can be issued only if it exists and at least 1 copy is available.
    3. Return a book only if it already exists in the library record.
    4. Book names should work regardless of uppercase or lowercase letters.
'''


library = {}

while True:
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Book Record")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_title = input("Enter book title: ")
        copies = int(input("Enter number of copies: "))
        library[book_title.lower()] = copies

    elif choice == 2:
        book_title = input("Enter book title: ")
        if book_title.lower() in library:
            if library[book_title.lower()] > 0:
                library[book_title.lower()] -= 1
                print("Book issued.")
            else:
                print("Book not available.")
        else:
            print("Book not found.")

    elif choice == 3:
        book_title = input("Enter book title: ")
        if book_title.lower() in library:
            library[book_title.lower()] += 1
            print("Book returned.")
        else:
            print("Book not found.")
    elif choice == 4:
        print("Book Record:")
        for book, copies in library.items():
            print(f"{book.title()}: {copies} copies")
    elif choice == 5:
        break
    else: 
        print("Invalid choice. Please try again.")