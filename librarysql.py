import sqlite3

import time


class Book():
    def __init__(self,name,author,publisher,genre,edition):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.edition = edition

    def __str__(self):
        return f"Name: {self.name}\n Author: {self.author}\n Publisher: {self.publisher}\n Genre: {self.genre}\n Edition: {self.edition}\n"
        

class Library():
    def __init__(self):
        self.connectDatabase()
    

    def connectDatabase(self):

        self.connection = sqlite3.connect("library.db")
        self.cursor = self.connection.cursor()

        check = "Create Table If not exists books (name TEXT, author TEXT, publisher TEXT, genre TEXT, edition INT)"

        self.cursor.execute(check)
        self.connection.commit()

    def cutConnection(self):
        self.connection.close()

    
    def showBooks(self):
        check = "Select * from books"
        self.cursor.execute(check)
        books = self.cursor.fetchall()

        if len(books) == 0:
            print("There is no book in the library")
        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3],i[4])
                print(book)

    def checkBook(self,name):
        check = "Select * From books where name = ?"

        self.cursor.execute(check,(name,))

        books = self.cursor.fetchall()

        if len(books) == 0:
            print("There is no match")
        else:
            book = Book(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4])
            print(book)

    def addBook(self,book):
        check = "Insert into books Values(?,?,?,?,?)"

        self.cursor.execute(check,(book.name,book.author,book.publisher,book.genre,book.edition))
        self.connection.commit()

    def deleteBook(self,name):

        check = "Delete from book where name = ?"

        self.cursor.execute(check,(name,))

        self.connection.commit()

    def addEdition(self,name):
        check = "Select * From books where name = ?"
        self.cursor.execute(check,(name,))
        book = self.cursor.fetchall()

        if len(book) == 0:
            print("There is no match")
        else:
            edition = book[0][4]
            edition += 1
            update = "Update From books set edition = ? where name = ?"

            self.cursor.execute(update,(edition,name))

            self.connection.commit()

        