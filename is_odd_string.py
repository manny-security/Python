import string

#returns true if sum of each character's position in the alphabet is odd.
def is_odd_string(a_string):
    alphabet_dict = dict(zip(string.ascii_lowercase, range(1, 27)))
    result = sum(alphabet_dict[i] for i in list(a_string.lower()))
        
    #check for odd
    return result % 2 == 1

print(is_odd_string('a')) # True
print(is_odd_string('aaaa')) # False
print(is_odd_string('Amazing')) # True
print(is_odd_string('veryfun')) # True
print(is_odd_string('veryfunny')) # False