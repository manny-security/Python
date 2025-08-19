#accepts a list and a number and returns the first pair of numbers that sum to the number passed
def sum_pairs(my_list,my_number):
    retrlst = []
    for i in my_list:
        new_value = my_list[0] + i
        if new_value == my_number:
            retrlst.append(my_list[0])
            retrlst.append(i)
            return retrlst
    return retrlst


print(sum_pairs([4,2,10,5,1], 6)) #[4,2]
print(sum_pairs([11,20,4,2,1,5], 100)) #[]