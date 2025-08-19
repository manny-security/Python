#accepts a list and returns True if list a lists.
def list_check(my_list):
    count = 0
    #checks each element
    for l in my_list:
        if type(l) is list:
            count += 1
    #compares 
    if count == len(my_list):
        return True
    return False
    

print(list_check([[],[1],[2,3], [1,2]])) #True
print(list_check([1, True, [],[1],[2,3]])) #False