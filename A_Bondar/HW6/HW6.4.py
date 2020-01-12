# В файле хранятся данные с сайта IMDB. Скопированные
# данные хранятся в файле ./data6/ ratings.list.
# Откройте и прочитайте файл(если его нет необходимо
# вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt –
# названия файлов, ratings.txt – гистограмма
# рейтингов, years.txt – гистограмма годов.

from collections import Counter
import sys

try:
    with open('data6/ratings.list', encoding="utf-8") as imdb_rating:
        top250_movies = []
        for line in imdb_rating:
            if line.startswith('0'):
                top250_movies.append(line.strip())
                if len(top250_movies) == 250:
                    break
except FileNotFoundError:
    print('Sorry, file not found.')
    sys.exit()

top250_movies_add = [elem.split() for elem in top250_movies]

for line in top250_movies_add:
    title = line[1:-2]
    movie_title = ' '.join(title)
    with open('top250_movies.txt', 'a') as top250_imdb:
        top250_imdb.write(movie_title + "\n")
    top250_imdb.close()

with open('data6/ratings.list', encoding="utf-8") as file:
    all_ratings = Counter(line[-4:-1] for line in file)
    with open('ratings.txt', 'w') as movies_imdb_ratings:
        for key, value in all_ratings.items():
            movies_imdb_ratings.write(str(key) + ' ' + int(value) * '*' + '\n')
    movies_imdb_ratings.close()

with open('data6/ratings.list', encoding="utf-8") as file:
    all_years = Counter(line[-10:-6] for line in file)
    with open('years.txt', 'w') as top250_movies_years:
        for key, value in all_years.items():
            top250_movies_years.write(str(key) + ' ' + int(value) * '*' + '\n')
    top250_movies_years.close()

imdb_rating.close()
