#returns the sum of the values between (and including) the start and end index.
def range_in_list(a_list,start=0,end=0):
    if end == 0:
        end = a_list[-1]
    print( sum(a_list[start:end+1]))


range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0