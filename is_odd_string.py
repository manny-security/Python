import string

#returns true if sum of each character's position in the alphabet is odd.
def is_odd_string(a_string):
    alphabet_dict = {}
    number_value = []
    alphabet_key = []
    total = 0

    for char in string.ascii_lowercase:
        alphabet_key.append(char)

    for n in range(1,27):
        number_value.append(n)

    for key,value in zip(alphabet_key,number_value):
        alphabet_dict[key] = value


    #sums all values
    for i in list(a_string):
        total += alphabet_dict[i]

    #check for odd
    if total % 2:
        return True
    
    return False


is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False