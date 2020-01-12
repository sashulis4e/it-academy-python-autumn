def prices():
    M = int(input('Введите рубли'))
    N = int(input('Введите копейки'))
    L = int(input('Введите количество товара'))
    return (M + N / 100) * L


def fibonachi():
    n = int(input('Enter number'))
    f1 = f2 = 1
    print(f1)
    print(f2)
    i = 1
    for i in range(2, n):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        print(f3)


def chekio():
    a = input('Enter your name')
    b = input('Enter your age')
    return "Hi. My name is", a, "and I'm", b, "years old"


def gen_numbers():
    number = 1
    while number <= 100:
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)
        number = number + 1


def words():
    lst1 = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
    del lst1[1::2]
    print(lst1)

    lst2 = ['1a', '2a', '3a', '4a']
    wrd = lst2.index('2a')
    lst2.remove('2a')
    print(lst2)
    lst2.copy()
    lst2.insert(wrd, '2a')
    print(lst2)


def hw4_3():
    lst = ['a', 'b', 'c']
    lst = tuple(lst)
    print(lst)
    tpl = ('a', 'b', 'c')
    tpl = list(tpl)
    print(tpl)
    a, b, c = 'a', 2, 'gamma'
    d = (a, b, c)
    tpl2 = (d,)
    print(tpl2)
    if len(tpl2) == 1:
        print('True')
    else:
        print('False')


def hw5_1():
    number = int(input('Введите число '))
    dct_numbers = dict()
    for number in range(1, number):
        dct_numbers[number] = number ** 2
    print(dct_numbers)


def hw5_2():
    text = input('Введите текст ')
    words = {}
    result = []
    text = ''.join(sign for sign in text if sign not in (',', '.', '?', '!',
                                                         ':', ';', '(', ')',
                                                         '[', ']', '{', '}',
                                                         '+', '-', '/', '|',
                                                         '>', '<', '=', '#',
                                                         '$', '%', '^', '&',
                                                         '*'))
    text = text.lower().split()
    for word in range(len(text)):
        words[text[word]] = words.get(text[word], 0) + 1
    for key in words:
        if words[key] == max(words.values()):
            result.append(key)
    print(sorted(result)[0])


def hw5_3():
    countries = {}
    for i in range(int(input('Количество стран '))):
        country, *city = input('Страны и их города ').split()
        countries[country] = city

    cities = []
    for k in range(int(input('Количество городов '))):
        city = input('Город ')
        cities.append(city)
        for city in cities:
            print(countries.get(city))


def hw5_4():
    lst1 = [1, 5, 7, 7, 9, 15, 34]
    lst2 = [1, 10, 9, 8, 16, 34]
    print(len(set(lst1) & set(lst2)))


def hw5_5():
    lst1 = [1, 5, 7, 7, 9, 15, 34]
    lst2 = [1, 10, 9, 8, 16, 34]
    print(len(set(lst1) ^ set(lst2)))
