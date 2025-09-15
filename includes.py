#Return True if the value exists in the collection, search from the starting index. Otherwise, return False.
def includes(my_list,my_value,optional_index = 0):
    return my_value in (my_list.values() if isinstance(my_list, dict) else ([my_list[optional_index]] if optional_index != 0 else my_list))


print(includes([1, 2, 3], 1)) # True 
print(includes([1, 2, 3], 1, 2)) # False
print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False