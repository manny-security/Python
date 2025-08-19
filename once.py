#returns a new function that can only be invoked once.
def once(function):
    #If the function is invoked more than once, it should return None.
    count = 0
    def inner_function(*args,**kwargs):
        nonlocal count
        if count == 0:
            count += 1
            return function(*args,**kwargs)
        else:
            return None
    return inner_function


def add(a,b):
    return a+b

oneAddition = once(add)

print(oneAddition(2,2)) # 4
print(oneAddition(2,2)) # None
print(oneAddition(12,200)) # None