#so here we have giaven aditional arguements
#so role of this function to find num from num_list in between left_index and right index

def binary_search_recursive(num_list, num, left_index, right_index):
    #if index is not appropriate
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= right_index or mid_index < 0:
        return -1

        #as we have the mid index so middle element will be
    mid_element = num_list[mid_index]

    #if the middle number is the number we want to find
    if mid_element == num:
            #just return its index
        return mid_index

    
    if mid_element < num:
            left_index = mid_index + 1

    else:
            #else means mid_element is greater than number we want to find
            #so we will ignore right part as our num is in left
        right_index = mid_index - 1

    #now as we have new left and right indexes we can call this function again
    return binary_search_recursive(num_list,num, left_index, right_index)




number_list = [1,3,4,5,6,67,89]
num = 67
print(f"{num} is at index {binary_search_recursive(number_list, num, 0, len(number_list))}")

