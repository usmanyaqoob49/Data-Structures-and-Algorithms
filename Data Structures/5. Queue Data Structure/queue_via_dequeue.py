from collections import deque
q = deque()

#use appendleft() to append values to left side of queue (At zeroth location always (In start))
q.appendleft(131)
q.appendleft(132)
q.appendleft(133)

#now we can use pop() to get the last entery 
#as queue is fifo
#and here most right side enetery will be the one that is entered very first time
#so we are good with this 

print(q.pop())
print(q.pop())