# Define a dict comprehension which returns a dictionary where the keys are
# numbers between 1 and n (both included) and the values are square of keys.
# Define a code which count and return the numbers of each character in
# a count_me_string argument.

number = int(input('Введите число '))
dct_numbers = dict()
for number in range(1, number):
    dct_numbers[number] = number ** 2
print(dct_numbers)
