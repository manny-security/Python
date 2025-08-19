#returns the most frequent number in the list of numbers.
def mode(number_list):
    for n in number_list:
        if number_list.count(n) > round(len(number_list)/3):
            return n
        
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4