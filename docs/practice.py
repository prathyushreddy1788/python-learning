'''Write a Python function that takes a list of integers as input and
returns a new list containing only the prime numbers from the original list.'''
def get_factors(number:int)-> list:
    factors: list = []
    for i in range(1,number+1):
        if number % i == 0:
            factors.append(i)

    return factors




#def prime(primex):

    #first eliminate even numbers
    # x




prime_numbers_list: list = []
list_of_integers: list = [2,3,4,5,6,7,8,9]
for i in list_of_integers:
    get_factors(i)
    if len(get_factors(i)) < 3:
        prime_numbers_list.append(i)
print(prime_numbers_list)








#prime(list)
