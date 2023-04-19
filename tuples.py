'''
* Tuple is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Set, and Dictionary, all with different qualities and usage.
* A tuple is a collection which is ordered and unchangeable.
'''
# tuple declaration:
tup = ('they','hey' ,'are', 'michel')
print(tup)
print('---')

# length of tuple:
print(len(tup))
print(type(tup))
print('---')

# index of tuple
print(tup[0])
print(tup[-1])
print(tup[:2])
print(tup[:])
print('---')

# use if in tuple:
if 'michel' in tup:
    print('yes, is right')
else:
    print('not found !')
print('---')

if 'ahmed' in tup:
    print('yes, is right')
else:
    print('not found !')
print('---')

# update of tuple:
x = list(tup)
x[1] = 'hello!'
tup = tuple(x)
print(tup)
print('---')

# Add:
z = list(tup)
z.append('nacef')
print(z)
print('---')

# remove():
z.remove('nacef')
print(z)
print('---')

# delete :
'''
del tup
print(tup)  # this will raise an error because the tuple no longer exists
'''

# for loop: tuple item
for i in tup:
    print(i)
print('---')

# for loop : tuple index
for i in range (len(tup)):
    print(tup[i])
print('---')

# while loop:
i = 0
while i < len(tup):
  print(tup[i])
  i = i + 1
print('---')

# join:
tup1 = ('book', 'object', 'table')
tub2 = (1,2,3)
tub3 = tup1+tub2
print(tub3)
tub4 = tub2*3
print(tub4)

# count:
# index