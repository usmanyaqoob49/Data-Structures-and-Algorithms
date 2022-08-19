#Write a function in python that checks if paranthesis in the string are balanced or not. 
# Possible parantheses are "{}',"()" or "[]". Use Stack class.

#is_balanced("({a+b})")     --> True
#is_balanced("))((a+b}{")   --> False
#is_balanced("((a+b))")     --> True
#is_balanced("))")          --> False
#is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True


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
        return self.container[-1]

    #to check size of stack
    def size(self):
        return len(self.container)

    #to check if stack is empty or not
    def is_empty(self):
        return len(self.container) == 0


def is_match(ch1,ch2):
    dict = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    #return True if ch1 matches with ch2
    return dict[ch1] == ch2

def is_balance(string):
    stack = Stack()
    for char in string:
        if char == '(' or char == '[' or char == '{':
            stack.push(char)
        
        if char == ')' or char == ']' or char == '}':
            #if these are the characters it is necessary to have their starting part
            #and there starting part will be in stack
            if stack.size() == 0:
                return False

            #now as we have starting part in stack we have to check for their match
                        #match every char with (, [, {
            if not is_match(char,stack.pop()):
                return False
    
    return stack.size() == 0
       


balance = is_balance("({a+b})")
print(balance)
print(is_balance("))((a+b}{"))
print(is_balance("((a+b))"))
print(is_balance("((a+g))"))
print(is_balance("))"))
print(is_balance("[a+b]*(x+2y)*{gg+kk}"))





