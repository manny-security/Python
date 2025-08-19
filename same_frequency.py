#returns True if they contain the same frequency of digits. Otherwise,False
def same_frequency(first_number,second_number):
    for f in list(map(int, str(first_number))):
        if f not in list(map(int, str(second_number))):
            return False 
    return True


same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True