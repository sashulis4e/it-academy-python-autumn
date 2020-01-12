# Создайте декоратор, который хранит в файле результаты
# вызова функций (за все время, не только текущий запуск программы)


def func_results(func):
    def wrapper():
        res = func()
        with open('funcs_results.txt', 'a') as f:
            f.write('{}\n'.format(res))
            f.close()

    return wrapper


@func_results
def hw2_1():
    M = int(input('Введите рубли'))
    N = int(input('Введите копейки'))
    L = int(input('Введите количество товара'))
    return (M + N / 100) * L


hw2_1()
