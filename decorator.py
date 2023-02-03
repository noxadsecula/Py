def extrafeature(func):
    

    def wrapper(numbers):
        odds = 0
        evens = 0
        sumOfOdds = 0
        sumOfEvens = 0
        for i in numbers:
            if (i % 2 == 0):
                sumOfEvens += i
                evens += 1
            else:
                sumOfOdds+= i
                odds += 1
        print("Average of Odd numbers: ", sumOfEvens/evens )
        print("Average of Even numbers: ", sumOfOdds/odds )
        func(numbers)
    return wrapper

@extrafeature
def findAverage(numbers):
    sum = 0

    for i in numbers:
        sum += i

    print(f"Average of the numbers is {sum/(len(numbers))}")



findAverage((1,2,3,4,5,10,62,100,77,23))



# *******************************************






def pNumber(func):
    
    def wrapper():
        print("Perfect numbers...")
        for number in range(1,1001):
            sum = 0
            i = 1
            while (i < number):
                if (number % i == 0):
                    sum += i
                i +=1
            if (sum == number):
                print(number)
        func()
                
    return wrapper
    


@pNumber
def primes():
    print("Prime Numbers...")
    for number in range(2,1001):
        i = 2 
        say = 0
        while (i < number):
            if (number % i == 0):
                say += 1
            i += 1
        if (say == 0):
            print(number)
            
primes()    
