# Ex1
liste = []
for i in range(3):
    numbers = int(input("Enter numbers"))
    liste.append(numbers)





# *********************************************************








# Ex2
print(f"Multiplication of the numbers: {liste[0]*liste[1]*liste[2]}")

print("Please enter your height and weight to calculate index...")

height = int(input("Height: "))
weight = int(input("Weight: "))

index = weight / height

print(index)






# *********************************************************











# Ex3

a = int(input("Number 1: "))
b = int(input("Number 2: "))

a,b = b,a


print(f"a = {a} , n = {b}")






# *********************************************************








# Ex4

listeMax = []
for i in range(3):
    numbers = int(input("Enter numbers"))
    listeMax.append(numbers)

for i in listeMax:
    if i >= listeMax[0] and i>= listeMax[1] and i>= listeMax[2]:
        maxNumber = i
        print(maxNumber)
    







# *********************************************************






# Ex5 (List Comprehension)

liste1 = [(5,10),(20,30),(40,50)]

liste2 = [i*j for i,j in liste1]

print(liste2)







# *********************************************************



# Ex 6 (Liste Comprehension)
# ***************************
liste = [(1,2),(3,4,5,6),(7,8,9,10)]

liste1 = [x for i in liste for x in i]
print(liste1)
        
# ***************************


# Ex7 (Fibonacci Series)


a = 1
b = 1

fibonacci = [a,b]

for i in range(20):
    a,b = b,a+b
    fibonacci.append(b)

print(fibonacci)






# *********************************************************






# Ex8 (Perfect Number)
while True:
    pnumber = int(input("Enter a number: "))
    i = 1
    sum = 0
    while (i < pnumber):
        if (pnumber % i == 0):
            sum += i
        i += 1

    if (sum == pnumber):
        print("Number is a perfect number")
        break
    else:
        print("Number is not a perfect number")





# *********************************************************







# Ex9 (Armstrong Number)

number = input("Enter a number: ")
total = 0
pwr = len(number)
for i in number:
    total += int(i)**pwr

if int(number) == total:
    print(f"Number: {number} is an Armstrong number")
else:
    print(f"Number: {number} is not an Armstrong number")




# *********************************************************

# Ex 10

liste = []

for i in range(1,101):
    liste.append(i)

for i in liste:
    if (i % 3 == 0):
        print(i)

    











# Ex11 (Lambda Structure)

tag = lambda parameter1,parameter2 : function

def multiplyByTwo(x):
    return x*2

print(multiplyByTwo(5))


multiplyByTwoLambda = lambda x : x*2

print(multiplyByTwoLambda(20))


    


# *********************************************************









# Ex12 (Perfect Number Function)


def perfectnumber(pnumb):
    dividers = []
    sum = 0
    for i in range(1,pnumb):
        if pnumb % i == 0:
            dividers.append(i)

    for i in dividers:
        sum += i
    
    if (sum == pnumb):
        return True
    else:
        return False



number = int(input("Enter a Number"))

if (perfectnumber(number)):
    print("Number is perfect")
else:
    print("Number is not perfect")




# *********************************************************





# Ex 13 (Class)

class Animals():
    def __init__(self,familia,name,gender):
        self.familia = familia
        self.name = name
        self.gender = gender

    def __str__(self):
        print(f"""
        Familia: {self.familia}
        Name: {self.name}
        Gender: {self.gender}
        """)

    def __len__(self):
        print(len(Animals))

class Dog(Animals):
    def __init__(self, familia, name, gender):
        super().__init__(familia, name, gender)

class Bird(Animals):
    def __init__(self, familia, name, gender, wingspan, migrationfield):
        super().__init__(familia, name, gender)

        self.wingspan = wingspan
        self.migrationfield = migrationfield


class Horse(Animals):
    def __init__(self, familia, name, gender, breed):
        super().__init__(familia, name, gender)
        self.breed = breed
    
    def __str__(self):
        print(f"""
        Familia: {self.familia}
        Name: {self.name}
        Gender: {self.gender}
        Breed: {self.breed}
        """)


horse = Horse(familia="Arabian", name="Küheylan", gender="Female", breed="Pure Blood")
dog = Dog(familia="Yorkshire",name="Jüpi",gender="Female")

print(horse)








# ***********************************






# Ex 14 (Try-Except)

liste = ["345","sadas","324a","14","kemal"]
for eleman in liste:
    try:
        eleman = int(eleman)
        print(eleman)

    except ValueError:
        print("Liste elemanı sayı içermiyor")




# ********************************



# Ex15 (Raise)

def isItEven(n):
    if n % 2 == 0:
        return n
    else:
        raise ValueError("Sayı tek")



liste = [1,2,3,4,5,6,7,8,9,10,11,12,13]


for i in liste:
    try:
        print(isItEven(i))
    except ValueError:
        pass





# **********************************************







# Ex 16 (Builtin Functions)


liste = [(3,4),(10,3),(5,6),(1,9)]

def calc(x):
    return x[0] * x[1]

print(list(map(calc , liste)))



# *********************

liste = [(3,4,5),(6,8,10),(3,10,7)]

def triangle(x):
    if (abs(x[0]+x[1]) > x[2] and abs(x[0]+x[2]) > x[1] and abs(x[1]+x[2]) > x[0]):
        return True
    else:
        return False

print(list(filter(triangle,liste)))


# *********************

from functools import reduce

listed = [1,2,3,4,5,6,7,8,9,10]

def even(x):
    if x % 2 == 0:
        return True
    else:
        return False


tosum = list(filter(even,listed))

print(reduce(lambda x,y : x + y, tosum))


# *********************



names = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
surnames = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]


for i,j in zip(names,surnames):
    print(f"Person: {i} {j}\n")








# *********************

