#using list for stack is not recomended because list are dynamic so it will be costly if the space ended
#as it will copy all the elements to other place

#so we will implement stack with collection.deque() --> predefined in python
#deque is based on doubly linked lists

from collections import deque
stack = deque()

#deque has a function called append() that will add a element to right side
stack.append('page 1')
stack.append('page 2')
stack.append('page 3')
stack.append('page 4')

print(stack)

#now if you want to access and remove last element because you want to be at page 3
print(stack.pop())

#Last implement stack using Class
class Stack():
    def __init__(self):
        self.container = deque()
    
    #so to push element means adding element in end (in right)
    def push(self,element):
        self.container.append(element)

    #to pop
    def pop(self):
        return self.container.pop()
    
    #to check last element without deleting
    def check(self):
        print(self.container[-1])

    #to check size of stack
    def size(self):
        return len(self.container)

    #to check if stack is empty or not
    def is_empty(self):
        return len(self.container) == 0


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.container)
b = Stack()
print(b.is_empty())