class Stack:
    def __init__(self):
        self.items = []
    def push_item(self, item):
        self.items.append(item)

    def pop_item(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    #will give last element without deleting
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

stack_1 = Stack()
stack_1.push_item(1)
stack_1.push_item(2)
stack_1.push_item(3)
stack_1.push_item(4)
print(stack_1.get_stack())
print(stack_1.pop_item())
print(stack_1.get_stack())
print(stack_1.is_empty())
print(stack_1.peek())