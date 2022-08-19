stack = []
stack.append('page 1')
stack.append('page 2')
stack.append('page 3')
stack.append('page 4')

print(stack)
#so we when we want the last entery (here page 4)
#we will use pop(), but it will also remove that from list

print(stack.pop())


#if we dont want to remove the element and just want last element
print(stack[-1])

#using list for stack is not recomended because list are dynamic so it will be costly if the space ended
#as it will copy all the elements to other place

#so we will implement stack with collection.deque() --> predefined in python
#deque is based on doubly linked lists