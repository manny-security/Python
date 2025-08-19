#The function should return True if the value exists in the collection when we search starting from the starting index. Otherwise, it should return False.
def includes(my_list,my_value,optional_index = 0):
    if type(my_list) is dict:
        my_dict = my_list
        return my_value in my_dict.values()
        
    if optional_index > 1:
        return my_value == my_list[optional_index]
    return my_value in my_list


print(includes([1, 2, 3], 1)) # True 
print(includes([1, 2, 3], 1, 2)) # False
print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False