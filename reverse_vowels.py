#reverse the vowels in a string.
def reverse_vowels(a_string):
    wl = list(a_string)
    vl = []
    for w in wl:
        if w in "aeiouAEIOU":
            vl.append(w)

    rvl = vl[::-1]
    print(rvl)
    count1 = -1
    count2 = -1

    for rw in wl:
        count1 += 1
        if rw in "aeiouAEIOU":
            count2 += 1
            wl[count1] = rvl[count2]

    return_word = ''.join(wl)   
    
    return return_word


reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"