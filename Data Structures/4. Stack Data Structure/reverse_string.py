from stack import Stack
def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push_item(char)
    #once all are pushed
    reverse_str = ''
    while not stack.is_empty():
        reverse_str += stack.pop_item()
    return reverse_str

stack = Stack()
input_str = "emocleW"
print(reverse_string(input_str))