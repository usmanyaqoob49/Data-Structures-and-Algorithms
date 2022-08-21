#making a list for stock prices
from tkinter import W


WMT_stock_prices = []

#you can push entery at 0 location using insert() function
WMT_stock_prices.insert(0,131)
#now when we again push the another entry at 0th location the above one will pe pushed forwarded
WMT_stock_prices.insert(0,132)
#lets do another one
WMT_stock_prices.insert(0,133)

#now lets check how it looks like:
print("Queue: ", WMT_stock_prices)

#now as the queue is first in first out data structure
#so when we will try to get a value using pop() 
#we will get 131 and it will be removed from queue

print(WMT_stock_prices.pop())

#List is ok to be used as queue but as lists are dynamic arrays and if they run out of space they will carry that data to new place
#that will be double of first one and if again happen same steps will be taken so it may cost us too much space
#Not Recommended