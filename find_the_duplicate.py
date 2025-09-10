#returns the number that is a duplicate or None if there are no duplicates.
def find_the_duplicate(number_list):
    duplicates = [n for i, n in enumerate(number_list) if n in number_list[i+1:]] 

    if duplicates:
        return duplicates[0]
    else:
        return None

#not the most efficient but I wanted to try list comprehension solution      

print(find_the_duplicate([1,2,1,4,3,12])) # 1
print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
print(find_the_duplicate([2,1,3,4])) # None