#The function returns the number which is a duplicate or None if there are no duplicates.
def find_the_duplicate(number_list):
    count = 0
    for a in number_list:
        count += 1
        if a in number_list[count:]:
            return a             
        

find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None