#function should return a dictionary created from the keys and values.
def two_list_dictionary(key_list,value_list):
    new_dict = {}
    count = 0
    for i in key_list:
        try:
            new_dict[i] = value_list[count]
        #If there are not enough values, the remaining keys should have a value of null.
        except IndexError:
            new_dict[i] = None
        count += 1
    return new_dict

two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}