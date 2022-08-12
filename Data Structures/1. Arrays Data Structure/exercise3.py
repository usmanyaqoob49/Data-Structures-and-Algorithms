#Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

max_number = input("Enter the max number: ")
max_number = int(max_number)

odd_list = []

for i in range(1, max_number):
    if i % 2 != 0:
        odd_list.append(i)
print(odd_list)
