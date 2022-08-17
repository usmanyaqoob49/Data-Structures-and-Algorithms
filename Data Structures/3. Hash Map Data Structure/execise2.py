#nyc_weather.csv contains new york city weather for first few days in the month of January. 
#Write a program that can answer following,
    #What was the temperature on Jan 9?
    #What was the temperature on Jan 4?
    
    #Figure out data structure that is best for this problem

#Answer:
#for this best data structure will be hash maps because we have to answer on base of key 

#making hash map
class Hashtable():
    def __init__(self):
        self.MAX = 11
        self.arr = [[] for i in range (self.MAX)]

    
    def get_hash(self,key):
        h = 0
        for characters in key:
            h += ord(characters)
        return h % self.MAX


    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False 
        for index , elements in enumerate(self.arr[h]):
            if len(elements) == 2 and elements[0] == key:
                elements[1][index] = (key,value)

            found = True

        
        if not found:
            self.arr[h].append((key,value))


t = Hashtable()
print(t.arr)
with open("nyc_weather.csv","r") as file:
    for rows in file:
        token = rows.split(',')
        day = token[0]
        try:
            temp = int(token[1])
            t[day] = temp
        except:
            print("Invalide Temperature.")

print("Temperature on Jan9 : ",t['Jan 9'])



print("Temperature on Jan4 : ",t['Jan 4'])