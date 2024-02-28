import re


def task1():
    '''
    Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
    '''
    pattern = re.compile(r'ab*')
    
    text = input()

    print("YES" if pattern.search(text) else "NO")



def task2():
    '''
    Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
    '''
    pattern = re.compile(r'ab{2,3}')

    text = input()

    print("YES" if pattern.search(text) else "NO")


def task3():
    '''
    найти последовательности строчных букв, Соединенных символом подчеркивания.
    '''

    pattern = re.compile(r'[a-z]+\_')

    text = input()

    print(pattern.findall(text))

    
def task4():
    '''
    чтобы найти последовательности одной заглавной буквы, за которой следуют строчные буквы.
    '''

    pattern = re.compile(r'[A-Z]{1}[a-z]+')

    text = input()

    print(pattern.findall(text))

def task5():
    '''
   которая соответствует строке с буквой "А", за которой следует что-нибудь, заканчивающееся на "в".
    '''

    pattern = re.compile(r'a.+b\Z')

    text = input()

    print("YES" if pattern.search(text) else "NO")

def task6():
    '''
    чтобы заменить все вхождения пробела, запятой или точки двоеточием.
    '''

    pattern = re.compile(r'[ ,.]')

    text = input()

    print(pattern.sub(':', text))


def task7():
    '''
    для преобразования строки регистра snake в строку регистра camel.
.
    '''
    def snake_to_camel(snake_case):
        return re.sub(r"_([a-z])", lambda s: s.group(1).upper(), snake_case)
    

    snakeCase = input()

    camelCase = snake_to_camel(snakeCase)

    print(camelCase)

def task8():
    '''
    чтобы разбить строку на заглавные буквы.

    '''

    text = input()


    print(re.sub(r'([A-Z])', lambda s: ' '+s.group(1), text).lstrip())


def task9():
    '''
    для вставки пробелов между словами, начинающимися с заглавных букв.

    '''

    text = input()


    print(re.sub(r'([A-Z])', lambda s: ' '+s.group(1), text).lstrip())

def task10():
    '''
    Write a Python program to convert a given camel case string to snake case.
    '''

    def camelToSnake(snake_case):
        return re.sub(r"\B([A-Z])", lambda s: '_'+s.group(1), snake_case).lower()
    
    camelCase = input()

    snakeCase = camelToSnake(camelCase)

    print(snakeCase)
