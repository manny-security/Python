#returns the number that is a duplicate or None if there are no duplicates.
def find_the_duplicate(number_list):
    seen = set()
    for item in number_list:
        if item in seen:
            return item
        seen.add(item)
    return None           
        

print(find_the_duplicate([1,2,1,4,3,12])) # 1
print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
print(find_the_duplicate([2,1,3,4])) # None