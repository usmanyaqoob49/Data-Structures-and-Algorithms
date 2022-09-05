#so first we will find number in array with linear serach

def linear_serach(num_list, num):
    #to retrun index as well as element we will use enumerate()
    for index,element in enumerate(num_list):
        if element == num:
            return index
        else:
            return -1
        

#Now we will implement binary search
def binary_search(num_list, num):
    #we have to find the mid index
    #for that first index will be left
    left_index = 0
    #right index will be the last one
    right_index = len(num_list) - 1
    #mid index
    mid_index = 0


    #we have to find mid element until the left index become equal or less than right
    while left_index <= right_index:
    #initially mid index will be
                    #with // you will get integer value
        mid_index = (left_index + right_index) // 2

        #as we have the mid index so middle element will be
        mid_element = num_list[mid_index]

        #now comparing mid number

        #if the middle number is the number we want to find
        if mid_element == num:
            #just return its index
            return mid_index


        #now if mid number is less than number we are finding so it means
        #our number is in right so we have to reset left index
        #we will mode left index from 0 to mid + 1

        if mid_element < num:
            left_index = mid_index + 1

        else:
            #else means mid_element is greater than number we want to find
            #so we will ignore right part as our num is in left
            right_index = mid_index - 1

    #if we dont find number
    return -1



number_list = [1,3,4,5,6,67,89]
num = 67
print(f"{num} is at index{binary_search(number_list, num)}")


        

