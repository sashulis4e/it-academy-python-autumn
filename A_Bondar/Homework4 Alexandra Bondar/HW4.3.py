# Tuple practice
# Create the list ['a', 'b', 'c'], then create a tuple from that list.
# Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
# (Hint: the material needed to do this has been covered, but it's not entirely obvious)
# Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'. (That is, in one line of code).
# Create a tuple containing just a single element which in turn contains the three elements 'a', 'b', and 'c'.
# Verify that the length is actually 1 by using the len() function.

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
