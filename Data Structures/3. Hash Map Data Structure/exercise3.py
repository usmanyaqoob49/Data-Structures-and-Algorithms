#poem.txt Contains famous poem "Road not taken" by poet Robert Frost.
#You have to read this file in python and print every word and its count as show below. 
# Think about the best data structure that you can use to solve this problem and figure out
# why you selected that specific data structure.


dic = {}
with open ('poem.txt' , 'r') as file:
    #this time we will directly use python dictionaries
    for rows in file:
        words = rows.split(' ')
        for word in words:
            word = word.replace('\n','')
            if word in dic:
                dic[word] += 1

            else:
                dic[word] = 1

print(dic)
