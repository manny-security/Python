# Returns the number of times a number is larger than another number across the entire list.
def find_greater_numbers(nums):
    return sum(1 for f in range(len(nums)) for s in range(f+1, len(nums)) if nums[f] < nums[s])

print(find_greater_numbers([1,2,3])) # 3 
print(find_greater_numbers([6,1,2,7])) # 4
print(find_greater_numbers([5,4,3,2,1])) # 0
print(find_greater_numbers([])) # 0