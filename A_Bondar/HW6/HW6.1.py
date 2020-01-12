# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner.
# runner() – все фукнции вызываются по очереди
# runner(‘gen_numbers’) – вызывается только функцию gen_numbers.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции

import allhmwrks


def runner(*defs):
    defs_list = [attr for attr in dir(allhmwrks) if not attr.startswith("__")]
    if len(defs) >= 1:
        for el in defs:
            func_hw = getattr(allhmwrks, el)
            print(func_hw())
    else:
        for elem in defs_list:
            function = getattr(allhmwrks, elem)
            print(function())

# runner()
# runner('gen_numbers')
# runner('chekio', 'words')
