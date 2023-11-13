def calculate_factorial(n):
    n = int(n)
    i = 1
    result = 1
    while i <= n-1:
        result = (result)*(i+1)
        i += 1
    return result


n = input("enter a positive integer ")
print(calculate_factorial(n))

def recursive_factorial(n):

    #function takes n as input
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

print(recursive_factorial(6))

'''iteration1: n = 4 
    4*fact(3)
    call 2 : n = 3
    3*fact(2)
    call 3 : n = 2
    2*1
    call 4 : n = 1
    1'''

    #if n is equal 1 then return 1
    # #else return n * factorial(n-1)


