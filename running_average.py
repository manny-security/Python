#function returned is passed a value,returns the current average of all previous function calls.
def running_average():
    nl = []
    def inner_funtion(n):
        nl.append(n)
        return sum(nl) / len(nl)
    return inner_funtion


rAvg = running_average()
print(rAvg(10)) # 10.0
print(rAvg(11)) # 10.5
print(rAvg(12)) # 11.0