#accepts a list and returns a new list with every second value removed
def remove_every_other(my_list):
    count = 0
    new_list = []
    for i in my_list:
        count += 1
        if count % 2:
            new_list.append(i)
    return new_list


remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]