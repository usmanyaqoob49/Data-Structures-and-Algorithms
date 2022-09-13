#firstly we need to write function that will find minimum value in array
def selection_sort(elements):
    size = len(elements)
    #first for loop will be used to iterate over the list
    #we are going till the second last element because if we have sorted element till the second last
    #last one will be at its place
    for i in range(size - 1):
        #making it the index of minimum number
        min_index = i
        #second loop will be on unsorted array
        for j in range(min_index + 1, size):
            #and the element in that unsorted will be compared with the minimum number
            if elements[j] < elements[min_index]:
                #if we found the elemet that is less the our minimum number (assumed)
                #we will update the min_index value
                min_index = j
        #after exiting this loop every time we will have a number that will be swaped
        #now we will swap if we find the other minimum number
        #if we have the min_index as i we wont swap 
        if i != min_index:
            #swapping method in python
            elements[i], elements[min_index] = elements[min_index], elements[i]
    return elements



element = [3,4,5,63,24,1]
print(selection_sort(element))