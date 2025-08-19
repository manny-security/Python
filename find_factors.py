#returns a list of all of the numbers that are  divisible by the given value, starting from 1 and going up.
def find_factors(number):
    return sorted([number // i for i in range(1, number + 1) if number % i == 0])


print(find_factors(10)) # [1,2,5,10 ]
print(find_factors(11)) # [1,11]
print(find_factors(111)) # [1,3,37,111 ]
print(find_factors(321421)) # [1,293,1097,321421]