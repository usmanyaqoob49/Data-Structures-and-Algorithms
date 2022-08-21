from collections import deque

class Queue():
    def __init__(self):
        self.buffer = deque()

    #to enter a value in queue (remember at 0th location so every entery will be pushed forwarded)
    def enqueue(self,val):
        self.buffer.appendleft(val)

    #FIFO --> to pop out value that was enterd first
    def dequeue(self):
        return self.buffer.pop()

    #to check if queue is empty or not
    def is_empty(self):
        return len(self.buffer) == 0

    #to return size of queue
    def size(self):
        return len(self.buffer) 

#testing
q = Queue()
#enterin some stock prices according to notes
q.enqueue({
    'Company' : 'WMT',
    'TimeStamp': '11:01 am',
    'Price' : '131 $'
})

q.enqueue({
    'Company' : 'WMT',
    'TimeStamp': '11:02 am',
    'Price' : '132 $'
})

q.enqueue({
    'Company' : 'WMT',
    'TimeStamp': '11:03 am',
    'Price' : '133 $'
})

q.enqueue({
    'Company' : 'WMT',
    'TimeStamp': '11:04 am',
    'Price' : '134 $'
})

q.enqueue({
    'Company' : 'WMT',
    'TimeStamp': '11:05 am',
    'Price' : '135 $'
})

#check size
print(q.size())

#now as every finance plot form will try to get the data as it is posted (first one first)
#they will use dequeue()

print(q.buffer)
print('\n')
print(q.dequeue())
print('\n')

print(q.buffer)
