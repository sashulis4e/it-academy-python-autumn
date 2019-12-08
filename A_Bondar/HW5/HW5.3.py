#  Дан список стран и городов каждой страны. Затем даны названия городов.
#  Для каждого города укажите, в какой стране он находится.

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
