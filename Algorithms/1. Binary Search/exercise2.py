#Find index of all the occurances of a number from sorted list
#numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
#number_to_find = 15  
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


#so to find all indecies
def all_indecies(num_list, num):
    #from this we will get one index where element exist in middle
    index = binary_search(num_list,num)

    #now make an array
    indecies = [index]

    #now find element on left hand side
    i = index - 1
    while i >=0:
        #if we get the number
        if num_list[i] == num:
            indecies.append(i)
            #simply append it
        else:
            break
        i = i-1

        
    #now find element on right side
    i = index + 1
    while i< len(num_list):
        if num_list[i] == num:
            indecies.append(i)
        else:
            break
        i = i+1
    
    return sorted(indecies)

if __name__ == '__main__':
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    indices = all_indecies(numbers, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")