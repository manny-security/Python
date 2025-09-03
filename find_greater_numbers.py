#returns the number of times a number is followed by a larger number across the entire list.
def find_greater_numbers(lst):
    count = 0
    for f in range(len(lst)):
        for s in range(f + 1, len(lst)):  # start at the *next* number
            if lst[f] < lst[s]:
                count += 1
    return count

print(find_greater_numbers([1,2,3])) # 3 
print(find_greater_numbers([6,1,2,7])) # 4
print(find_greater_numbers([5,4,3,2,1])) # 0
print(find_greater_numbers([])) # 0