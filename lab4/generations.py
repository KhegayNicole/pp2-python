#task 1 
def squares_gen(n):
    for i in range(1, n + 1):
        yield i * i

# generator = squares_gen(5)
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())

#task 2 
def print_even():
    n = int(input('n = '))
    def even_gen(n):
        for i in range(0, n + 1, 2):
            yield i

    even_numbers = ', '.join(str(num) for num in even_gen(n))
    print(even_numbers)
n = int(input('n = '))
print_even(n)
# print_even()
#task 3   
def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_by_3_and_4(30):
     print(num)

#task 4 
def squares_from_a_to_b(a, b):
    for i in range(a, b+1):
        yield i * i


for num in squares_from_a_to_b(3, 6):
    print(num)
        
#task 5
def from_n_to_0(n):
    for i in range(n, -1, -1):
        yield i
   

for i in from_n_to_0(4):
    print(i)