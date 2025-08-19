#shorten a string to a specified length, and add "..." to the end
def truncate(a_sentence, number):
    if number < 3:
        return "Truncation must be at least 3 characters."
    
    if number > len(a_sentence):
        return a_sentence

    return f'{a_sentence[:(number-3)]}...'


print(truncate("Super cool", 2)) # "Truncation must be at least 3 characters."
print(truncate("Super cool", 1) )# "Truncation must be at least 3 characters."
print(truncate("Super cool", 0)) # "Truncation must be at least 3 characters."
print(truncate("Hello World", 6) )# "Hel..."
print(truncate("Problem solving is the best!", 10)) # "Problem..."
print(truncate("Another test", 12)) # "Another t..."
print(truncate("Woah", 4)) # "W..."
print(truncate("Woah", 3)) # "..."
print(truncate("Yo",100)) # "Yo"
print(truncate("Holy guacamole!", 152)) # "Holy guacamole!"