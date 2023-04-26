'''
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*,
 changeable and do not allow duplicates.
'''
# dictionary declare
user ={
    "first_name" : 'Ahmed',
    "last_name" : 'Fathi',
    "age" : 28,
    "function" : 'software engineer'
}
#print dictionary:
print(user)
print('------------------------------')
print('the first name: '+user["first_name"])
print('the last name: '+user['last_name'])
print('------------------------------')

# len function: 
print(len(user))
print('------------------------------')

# type:
print(type(user))
print('------------------------------')

# can you use dictionary like constructor:
const = user
print(const)
print('------------------------------')

# get() method called:
method = user.get("first_name")
print(method)
print('------------------------------')

# key(): return a list of all the key
key = user.keys()
print(key)
print('------------------------------')

#update():
user.update({"first_name" : "Leo"})
print(user['first_name'])
print('------------------------------')

# remove():
     #pop():
user.pop("function")
print(user)
print('------------------------------')
    #del:
del user['age']
print(user) 
print('------------------------------')
#del user
#print(user) 
#this will cause an error because "user" no longer exists.

#clear():       
'''
user.clear()
print(user)
print('------------------------------')
'''

user02 = user.copy()
print(user02)
print('------------------------------')

# Nested Dictionary:

user001 ={
    "first_name" : 'Ahmed',
    "last_name" : 'Fathi',
    "age" : 28,
    "function" : 'software engineer'
}

user002 ={
    "first_name" : 'Mark',
    "last_name" : 'lockay',
    "age" : 24,
    "function" : 'system engineer'
}

user003 ={
    "first_name" : 'roberto',
    "last_name" : 'Ancheloti',
    "age" : 31,
    "function" : 'cloud engineer'
}

Admin = {
    "user1":user001,
    "user2":user002,
    "user3":user003
}
print(Admin['user2']['first_name'])
print('------------------------------')














