import sqlite3

con = sqlite3.connect("exdatabase.db")

cursor = con.cursor()



def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS library(Name TEXT, Author TEXT, Publisher TEXT,NumberOfPages INT)")
    con.commit()

def addData():
    cursor.execute("Insert into library Values('İstanbul Hatırası','Ahmet Ümit','Everest','561')")
    con.commit()

def addData2(name, author, publisher, numberOfPages):
    cursor.execute("Insert into library Values(?,?,?,?)",(name,author,publisher,numberOfPages))
    con.commit()

def pickData():
    cursor.execute("Select * From library")
    listedBooks = cursor.fetchall()
    print("List of book library")
    for i in listedBooks:
        print(i)

def pickData2():
    cursor.execute("Select Name,Author from library")
    nameAuthorList = cursor.fetchall()
    print("List of books and authors")
    for i in nameAuthorList:
        print(i)

def pickData3(publisher):
    cursor.execute("Select * from library where publisher = ?",(publisher,))
    allList = cursor.fetchall()
    for i in allList:
        print(i)

def updateData(setNewPublisher,oldPublisher):
    cursor.execute("Update library set publisher = ? where publisher = ?",(setNewPublisher,oldPublisher))
    con.commit()
    
def deleteData(author):
    cursor.execute("Delete From library where author = ?",(author,))
    con.commit()

# name = input("Name:")
# author = input("Author: ")
# publisher = input("Publisher: ")
# numberOfPages = input("Number of Pages: ")

# addData2(name,author,publisher,numberOfPages)

pickData()





con.close()