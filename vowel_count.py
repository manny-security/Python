#accepts a string and returns a dictionary with the keys as the vowels and values as the count of times
def vowel_count(my_string):
    vowels = ['a','e','i','o','u']
    my_dict = {}
    lwrW = my_string.lower()
    split = list(lwrW)

    for v in vowels:
        count = 0
        for s in split:
            if v == s:
                count += 1
                my_dict[v] = count

    return my_dict 

vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}


