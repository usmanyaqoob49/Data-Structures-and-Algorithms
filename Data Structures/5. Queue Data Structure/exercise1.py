#Design a food ordering system where your python program will run two threads,

#Place Order: This thread will be placing an order and inserting that into a queue. 
# This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)


#Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. 
# This thread serves an order every 2 seconds. 
# Also start this thread 1 second after place order thread is started.

from collections import deque
import time
import threading
class order():
    def __init__(self):
        self.queue = deque()

    #we will have method to put thing in queue
    def enqueue(self, food):
        self.queue.appendleft(food)

    #we will use it to serve every order
    def dequeue(self):
        if len(self.queue)==0:
            print("Queue is empty")
            exit()

        return self.queue.pop()


ord = order()

#we will make function for both things so that we can use multi threading
    #psses a list of things you want to order order
def place_order(order):
    for every_order in order:
        print("Placing", every_order)
        order = ord.enqueue(every_order)
        
            #here for the 0.5 seconds our cpu is doing nothing
            #so we can use this time for multithreading
            #doing some other task
            #in this case we have sever order using multithreading
        time.sleep(0.5)



def serve_orders():
    time.sleep(1)
    while True:
        order = ord.dequeue()
        print("serving: ", order)
        time.sleep(2)


#testing

if __name__ == '__main__':
#lets create two threads
    order = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_order, args=(order,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()
