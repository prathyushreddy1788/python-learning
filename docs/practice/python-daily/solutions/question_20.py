

def fibonacci_sequence(n: int):
        if n <= 0:
                return 0
        elif n == 1:
                return 1
        else:
                return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)

print(fibonacci_sequence(7))

# 0,1,1,2,3,5,8,13........
#


