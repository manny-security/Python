# accept a parameter which is a letter, and the inner function should return the number of times that letter appears.
def letter_counter(a_value):
    wrdlr = a_value.lower()
    wrdlst = list(wrdlr)
    def inner_fuction(letter):
        count = 0
        for l in wrdlst:
            if letter == l:
                count += 1
        return count
    return inner_fuction


counter = letter_counter('Amazing')
print(counter('a')) # 2
print(counter('m')) # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 