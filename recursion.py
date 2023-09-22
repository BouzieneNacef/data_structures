# factorial function:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

def factorial2(n):
    factorial = 1
    for i in range(1, n+1): 
        factorial *= i  
    return factorial

print(factorial2(5))