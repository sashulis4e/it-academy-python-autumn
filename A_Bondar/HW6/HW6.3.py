# Реализовать функцию get_ranges которая получает на вход
# непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
# get_ranges([4,7,10]) // "4,7,10"
# get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(numbers):
    solution = ""
    for number in range(len(numbers) - 1):
        if numbers[number] + 1 == numbers[number + 1] and numbers[number] - 1 != numbers[number - 1]:
            solution += '{}-'.format(numbers[number])
        elif numbers[number] + 1 != numbers[number + 1]:
            solution += '{},'.format(numbers[number])
    solution += str(numbers[-1])
    print(solution)


lst_numbers = [7, 11, 12, 13, 21, 22, 38, 39, 40]
get_ranges(lst_numbers)
