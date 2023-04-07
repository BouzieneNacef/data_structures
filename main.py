'''firsname = input('write your first name \n')
lastname = input('write your last name \n')
print('your name is '+firsname+' ' +lastname)'''
list = ['a', 15,False,'allez', 22]
print(list)

# list length:
print(len(list))
 
 #  verify list
if 'a' in  list:
    pass

# insert(index, value)
list.insert(2,'hello')
print(list)

# Append(x)
list.append('plus')
print(list)
print(list[5])
print(list[-1])
print(list[0])

# extend() 
another_list = ['always', 15, True, 88.24]
list.extend(another_list)
print(list)

#remove(value)
list.remove(88.24)
print(list)

# pop(index)
list.pop(2)
print(list)

# del
del list[0]
print(list)

# clear(): Remove all items from the list
#list.clear()

# loop list
# for loop:
for x in list:
    print(x)

for i in range(len(list)):
    print(list[i])

[ print(x) for x in list]

# while loop:
i = 0
while i< len(list):
    print(list[i])
    i = i+1





