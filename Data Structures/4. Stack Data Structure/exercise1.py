#Write a function in python that can reverse a string using stack data structure.
#  Use Stack class from the tutorial.
#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from collections import deque
class Stack:
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

  

def reverse_string(string):
    s = Stack()
    for char in string:
        s.push(char)
        
    reversed = ''
    while s.size() != 0:
        reversed += s.pop()
    return reversed



reversed = reverse_string('We will conquere COVID-19')
print(reversed)
