#returns True  if any three consecutive numbers sum to an odd number.
def three_odd_numbers(number_list):
    if len(number_list) <= 3:
        if sum(number_list[:3]) % 2:
            return True

    elif sum(number_list[:3]) % 2 or sum(number_list[1:4]) % 2:
        return True
    
    return False

print(three_odd_numbers([1,2,3,4,5])) # True
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
print(three_odd_numbers([5,2,1])) # False
print(three_odd_numbers([1,2,3,3,2])) # False