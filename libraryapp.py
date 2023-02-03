from librarysql import *

print("""
Welcome to Library App


Options


1 - Show Books

2 - Check Books

3 - Add Books

4 - Delete Books

5 - Add edition to a Book


To leave press "q"
""")

libr = Library()

while True:
    options = input("Choose the option that you want to execute: ")

    if options == "q":
        print("You are leaving now...")
        break
    elif options == "1":
        libr.showBooks()

    elif options == "2":
        name = input("Which book do you want: ")
        print("Book is checking....")
        time.sleep(2)
        libr.checkBook(name)

    elif options == "3":
        print("Enter the features of the book")
        name = input("Name: ")
        author = input("Author: ")
        publisher = input("Publisher: ")
        genre = input("Genre: ")
        edition = int(input("Edition: "))

        newBook = Book(name,author,publisher,genre,edition)

        print("Book is adding to the library...")
        time.sleep(2)
        print("Book is added")
        
        libr.addBook(newBook)

    elif options == "4":
        name = input("Which book do you want to delete from library")
        check = input("Are you sure Y/N?")

        if check == "Y":
            print(f"{name} is deleting from library...")
            libr.deleteBook(name)
            time.sleep(2)
            print(f"{name} is deleted.")
    elif options == "5":
        name = input("Choose the book which you want to add edition: ")
        print("Edition is setting...")
        time.sleep(2)
        libr.addEdition(name)
        print("Edition is updated.")
    else:
        print("Invalid option")

