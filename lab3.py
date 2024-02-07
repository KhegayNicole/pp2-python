#Classess

#tak1
class ConsoleString:

    def __init__(self):
        self.string = ''
        
    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())




#task2

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0



class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2



#task3

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

#task4
    
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def show(self):
        print(f"x = {self.x}, y = {self.y}")

    def move(self, x1, y1):
        self.x = x1
        self.y = y1
    
    def dist(self, x1, y1):
        distance = ((x1 - self.x)**2 + (y1 - self.y)**2) ** 0.5
        print(f"distance between points: {distance}")


#task5

class Account:
    def __init__(self, owner='', balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            
            raise(BaseException('You cant withdraw more than you have'))
 
        else: 
            self.balance -= amount
            return amount



#task6
def primeFilter(nums: list):

    def isPrime(n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return False if n == 1 else True
    
    return list(filter(lambda x: isPrime(x), nums))

print(primeFilter([1, 3, 4, 6, 7 ,1 ,6 ,21 ,14, 17, 25, 15, 19]))

#FUNCTIONS1

#task1

def Ounces(n):
    return n * 28.3495231

n = int(input("Enter a number: "))
result = Ounces(n)
print("Result in ounces:", result)

#task2

def toCelcius(f):
    print((5 / 9) * (f - 32))

#task3
def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            print(num_chickens, num_rabbits)
            return
    print("No solution")

#task4

def filter_prime(nums: list):

    def isPrime(n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return False if n == 1 else True
    
    return list(filter(lambda x: isPrime(x), nums))

#task5

def str_permutations(s):
    from itertools import permutations
    [print(''.join(p)) for p in permutations(s)]
#task6        
def changeOrder(s):
    print(' '.join(reversed(s.split())))

#task7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

#task8
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
        
    return False
#task9
def sph_vol(r):
    from math import pi
    return (4/3) * pi * (r**3)
#task10
def uniqueList(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i) 
    return res
#task11

def is_pal(s):
    return True if s == s[::-1] else False

def hist(arr):
    for i in arr:
        print('*' * i)
#task12
def is_pal(s):
    return True if s == s[::-1] else False

def hist(arr):
    for i in arr:
        print('*' * i)
#task13
def guessNumber():
    from random import randint
    rand = randint(1, 20)

    name = input("Hello! What is your name?\n")
    print(f'Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.')
    counter = 0
    while True:
        num = int(input())
        counter += 1
        if num < rand:
            print('Your guess is too low.\nTake a guess.')
        elif num> rand:
            print('Your guess is too high.\nTake a guess.')
        else:
            print(f'Good job, {name}! You guessed my number in {counter} guesses!')
            break

#FUNCTiIONS2


# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#task1
def higher5_5(movie):
    return movie['imdb'] > 5.5

#task2

def movies_above5_5(movies):
    return [movie['name'] for movie in movies if movie['imdb'] > 5.5]
#task3
def by_category(movies, category):
    return [movie['name'] for movie in movies if movie['category'] == category]
#task4
def average(movies):
    avg = sum([movie['imdb'] for movie in movies])

    return avg / len(movies)
#task5
def average_by_category(movies, category):
    movieList = [movie['imdb'] for movie in movies if movie['category'] == category]
  
    return sum(movieList) / len(movieList) 



