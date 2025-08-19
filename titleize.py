# accepts a string of words and returns a new string with the first letter of every word capitalized
def titleize(my_string):
    split = my_string.split()
    cptlz = []
    
    for s in split:
        new_str = s[0].upper() + s[1:]
        cptlz.append(new_str)
    new_word = ' '.join(cptlz)

    return new_word

titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"