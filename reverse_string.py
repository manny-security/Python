#function that accepts a string and returns a new string with all the characters reversed.
def reverse_string(my_string):
    #split string into a list
    splt = list(my_string)
    #reverse splt list
    rvs = splt[::-1]
    #join letters
    answ = "".join(rvs)

    return answ
