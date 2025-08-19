#returns a new string with the string passed to the function repeated the number amount of times.
def repeat(a_string,a_number):
    rptstrng = ''
    for a in range(a_number):
        rptstrng += a_string

    return rptstrng

repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''