#NxN-list of lists and sums the two main diagonals in the array
def sum_up_diagonals(list_of_list):
    left_right_diagonal = []
    right_left_diagonal = []
    #the one from the upper left to the lower right
    count = 0
    for a in list_of_list:
        left_right_diagonal.append(a[count])
        count += 1
    # the one from the upper right to the lower left.
    count = 1
    for a in list_of_list:
        right_left_diagonal.append(a[-count])
        count += 1

    result = left_right_diagonal + right_left_diagonal 

    return sum(result)


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
list3 = [
  [ 4, 1, 0 ],
  [-1,-1, 0 ],
  [ 0, 0, 9 ]
]

list4 = [
  [ 1,  2,  3,  4 ],
  [ 5,  6,  7,  8 ],
  [ 9, 10, 11, 12 ],
  [13, 14, 15, 16 ]
]


sum_up_diagonals(list1) # 10
sum_up_diagonals(list2) # 30
sum_up_diagonals(list3) # 11
sum_up_diagonals(list4) # 68