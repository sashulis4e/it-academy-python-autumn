# List practice
# Use a list comprehension to construct the list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].

lst1 = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
del lst1[1::2]
print(lst1)

# Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
# Simultaneously remove the element '2a' from the above list and print it.
# Copy the above list and add '2a' back into the list such that the original is still missing it.

lst2 = ['1a', '2a', '3a', '4a']
wrd = lst2.index('2a')
lst2.remove('2a')
print(lst2)
lst2.copy()
lst2.insert(wrd, '2a')
print(lst2)
