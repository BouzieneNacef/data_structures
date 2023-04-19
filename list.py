'''
List: is a collection which is ordered and changeable. Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable. Allows duplicate members.
Set: is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary: is a collection which is ordered** and changeable. No duplicate members.

firsname = input('write your first name \n')
lastname = input('write your last name \n')
print('your name is '+firsname+' ' +lastname)'''
list = ['a', 15,False,'allez', 22]
print(list)
print('---')

# list length:
print(len(list))
print('---')
 
 #  verify list
if 'a' in  list:
    pass
print('---')

# insert(index, value)
list.insert(2,'hello')
print(list)
print('---')

# Append(x)
list.append('plus')
print(list)
print(list[5])
print(list[-1])
print(list[0])
print('---')

# extend() 
another_list = ['always', 15, True, 88.24]
list.extend(another_list)
print(list)
print('---')

#remove(value)
list.remove(88.24)
print(list)
print('---')

# pop(index)
list.pop(2)
print(list)
print('---')

# del
del list[0]
print(list)
print('---')

# clear(): Remove all items from the list
#list.clear()

# reverse(): list reversed
list11 = [1,2,3,4,5,6,7,8,9]
list11.reverse()
print(list11)
print('---')

# sort(): sort the list
list33 = [5,7,11,2,88,100,3]
list33.sort()
print(list33)
print('---')

# loop list
# for loop:
for x in list:
    print(x)
print('---')

for i in range(len(list)):
    print(list[i])
print('---')

[ print(x) for x in list]

# while loop:
i = 0
while i< len(list):
    print(list[i])
    i = i+1
print('---')





