def bubble_sort(elements):
    size = len(elements)
    #we have to start comparing elements from start to second last element
    
    #this loop will run n - 1 times so that all the elements are arranged
    for k in range(size -1):


        #this loop will get the highest element in the end
        for i in range(size - 1):
            #we can also do this to save time as its always going till end even end elements are sorted
            #for i in range(size - 1 - i):
            
            #a variable that will turn true if element is swapped
            swapped = False
            if elements[i] > elements[i+1]:
                #so swap
                temp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = temp
                swapped = True
            
            #if we already give sorted list instead of running complete process we can check that if we have any element that was swapped
            #if there is no element swapped after inner loop that means list is already sorted
            
            #so we can break the oouter loop
            if not swapped:
                break


if __name__ == '__main__':
    elements = [23,45,64,1,3,5]
    bubble_sort(elements)
    print(elements)

