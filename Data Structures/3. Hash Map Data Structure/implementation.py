#firstly we have to write a hash function
#which will take a string (key) and will give us a index (int)

#---------------------------------------------------------------------

#we will implement hash function using ascii method
#In this we basically finds every character ascii --> here we will do this via ord() function
#then we sum all the ascii's
#then take mod of sum with size of array


#============================================================================

#In this code for hash map I did not solved the collision probelm

#-----------------------------------------------------------------------------  
def get_hash(key):
    h = 0
    for char in key:
        #finding ascii codes and adding them
        h += ord(char)
    return h % 100
    #here we took list size = 100



#now creating hash table class
class HashTable:
    def __init__(self):
        #defining array size
        self.MAX = 100
        #defining a array/ list with lsit comprehension
        #this means we have array with size 100 storing None
        self.arr = [None for i in range(self.MAX)]


    #Method for hash function
    def get_hash(self, key):
        h = 0
        for char in key:
            #finding ascii codes and adding them
            h += ord(char)
        return h % self.MAX


    #Method for adding a new key and value in hash table
    def add(self,key,val):
        #first thing we need to this is:
        # we have to get the index for this key so we will pass this key to hash function
        h = self.get_hash(key)
        #now h will have that index
        #then we have to store the value at that particular index
        self.arr[h] = val
        #this will store the value at that specific index that was returned by the hash function



    #Method for getting  value using a key in hash table
    def get(self,key):
        #first thing we need to this is:
        # we have to get the index for this key so we will pass this key to hash function
        h = self.get_hash(key)
        #now we have the index
        #we can now simply return the array value using the index
        return self.arr[h]



    #Method for deleting  value using a key in hash table
    def delete(self,key):
        # we have to get the index for this key so we will pass this key to hash function
        h = self.get_hash(key)
        #just access that value of array and make it None
        self.arr[h] = None



    #Now we will implement something about the hash tables that we use in python
    #so to acess value via key in python what we do is:
    #dict_name[key] and it gives you this
    #so instead of get methode we can implement this too

    #Method to get value in (I would say) Python Style :) :)
    #so pyhton have this operator that will give you the above functionality
    def __getitem__(self, key):
        #first thing we need to this is:
        # we have to get the index for this key so we will pass this key to hash function
        h = self.get_hash(key)
        #now we have the index
        #we can now simply return the array value using the index
        return self.arr[h]





    #Now we will implement something about the hash tables that we use in python
    #so to enter new key, value pair in python what we do is:
    #dict_name[key] = value ---> and it enters that value corresponding to key
    #so instead of add methode we can implement this too


    #Method to add value in hash table in (I would say) Python Style :) :)
    #so pyhton have this operator that will give you the above functionality
    def __setitem__(self, key, val):
        #first thing we need to this is:
        # we have to get the index for this key so we will pass this key to hash function
        h = self.get_hash(key)
        #now h will have that index
        #then we have to store the value at that particular index
        self.arr[h] = val
        #this will store the value at that specific index that was returned by the hash function






    #Now we will implement something about the hash tables that we use in python
    #so to delete value via key in python what we do is:
    #del dict_name[key] and it deletes that value and key (whole entery)
    #so instead of delete method we can implement this too

    #Method to delete value in (I would say) Python Style :) :)
    #so pyhton have this operator that will give you the above functionality
    def __delitem__(self, key):
        h = self.get_hash(key)
        #now we have the index
        self.arr[h] = None



#Testing

t = HashTable()
#it will give us index value where we the value for this key will be stroed
print("Value of this will be stroed at index : ",t.get_hash('march 6')) 


#adding a key value pair in hash table
t.add('march 6',130)

#getting the value via key
print("Value of march 6 is: ",t.get('march 6'))


#using normal python style to to add a key and a value
t['march 7'] = 131

#now accessing the value in python style
print("Value of March 7 is: ",t['march 7'])

del t['march 7']
#now t['march 7'] should show none
print("After deleting march 7 entery value of march 7 is: ", t['march 7'])
