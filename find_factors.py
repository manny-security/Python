#returns a list of all of the numbers which are is divisible by starting from 1 and going up to the number.
def find_factors(number):
    my_list = []
    for i in range(1,number):
        n = number / i
        if n == int(n):
            my_list.append(int(n))
    my_list.append(1)
    return_list = my_list[::-1]
    return return_list


find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421]