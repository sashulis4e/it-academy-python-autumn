# Define a dict comprehension which returns a dictionary where the keys are
# numbers between 1 and n (both included) and the values are square of keys.
# Define a code which count and return the numbers of each character in
# a count_me_string argument.

n = int(input('Введите число'))
dct = dict()
for n in range(1, n):
    dct[n] = n ** 2
print(dct)
