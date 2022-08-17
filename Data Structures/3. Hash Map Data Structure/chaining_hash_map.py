#In this code collision problem is solved using chaining techique

#---------------------------------------------------------------------
#creating hash table class
class HashTable:
    def __init__(self):
        #defining array size
        self.MAX = 10
        #defining a array/ list with list comprehension
        #this means we have array with size 100 storing array means evry entery is a array now
        #we are using array inside every element because every element will now have a key and a value
        self.arr = [[] for i in range(self.MAX)]


    #Method for hash function
    def get_hash(self, key):
        h = 0
        for char in key:
            #finding ascii codes and adding them
            h += ord(char)
        return h % self.MAX



    def __getitem__(self, key):
        h = self.get_hash(key)
        #now we have the index
        #now we have to iterate the specific index as it could be a linked list and we have to identify the key that we are searching

        #return self.arr[h] --> this will now retrun e a list
        #and we have to go through that list
        for elements in self.arr[h]:
            #as key placement is at 0 index so we are comparing
            if elements[0] == key:
                #value placement is at 1 index
                return elements[1]





    #Method to add value in hash table in (I would say) Python Style :) :)
    #so pyhton have this operator that will give you the above functionality
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        #now we will check at if we have a already existed key,value at that index
        #and also we  have to check if we have same key that already exits or not

        found = False
                                #we use enumrate() to iterate the elements in array
            #we are using this index to iterate the inner array(array with in element (that stores key and value))                    
        for index, element in enumerate(self.arr[h]):
            #checking if we have key and value at particular element(index)
            #and also checking if the key that we entered already exits or not
            if len(element) == 2 and element[0] == key:
                #if this is true it means we have the same key with different value in the same index
                #so for this scenario we will insert a new tupple with key and value at that index
                #so we will simply insert that value at that index 
                #or we can say we are just modifying that key, value pair
                self.arr[h][index] = (key,val)
                found = True
 
            
            #if we do not have that key in hash table
        if not found:
            #we will simply append the entry in that element thats an array
            self.arr[h].append((key,val))

                


    #Method to delete value in (I would say) Python Style :) :)
    #so pyhton have this operator that will give you the above functionality
    def __delitem__(self, key):
        h = self.get_hash(key)
        #now we have the index of the array where our key is located
        for index,element in enumerate(self.arr[h]):
            #if key matches
            if element[0] == key:
                #it will remove the complete tuple stored in that index of array/element
                del self.arr[h][index]



#Testing

t = HashTable()
print("Index of the element / array that will be used to store march 6: ",t.get_hash('march 6'))
print("Index of the element / array that will be used to store march 17: ",t.get_hash('march 17'))


t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63

print("value for march 6 key: ",t["march 6"])
print("value for march 17 key: ",t["march 17"])

del t["march 17"]
print(t.arr)