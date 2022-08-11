#Let us say your expense for every month are listed below,
#January - 2200
#February - 2350
#March - 2600
#April - 2130
#May - 2190

from cmath import exp


expense = [2200, 2350, 2600, 2130, 2190]

#1. In Feb, how many dollars you spent extra compare to January?

print(f"You spent extra: {expense[1] - expense[0]}")
print("\n")


#2. Find out your total expense in first quarter (first three months) of the year.

i =0
total = 0
for i in range(3):
    total = total + expense[i]

print(f"You spent{total}")
print("\n")



#3. Find out if you spent exactly 2000 dollars in any month

print(f"Did I spent 2000 : {2000 in expense}")


print("\n")
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expense.append(1980)
print(f"Expense at the end of June {expense}")
print("\n")


#You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

expense[3] = expense[3] - 200
print(f"After return {expense}")

