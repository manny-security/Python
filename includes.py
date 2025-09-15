#Return True if the value exists in the collection, search from the starting index. Otherwise, return False.
def includes(my_list,my_value,optional_index = 0):
    if type(my_list) is dict:
        return my_value in my_list.values()
        
    if optional_index == 0:
        return my_value in my_list
    return my_value == my_list[optional_index]


print(includes([1, 2, 3], 1)) # True 
print(includes([1, 2, 3], 1, 2)) # False
print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False