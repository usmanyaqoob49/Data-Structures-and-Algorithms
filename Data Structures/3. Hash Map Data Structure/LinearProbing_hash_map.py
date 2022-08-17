#In this code collision problem is solved using Linear Probing techique

#------------------------------------------------------------------------
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]


    #Method for hash function
    def get_hash(self, key):
        h = 0
        for char in key:
            #finding ascii codes and adding them
            h += ord(char)
        return h % self.MAX


    #this method is for returning the indecies 
    def get_prob_range(self, index):
        #for example if we have total indexes = 9
        #and here in the method we got 7 no index as arguement
        #so this method will return a list that contain
        #[7: max_index, 0: 7-1]
        #so we will get [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
        #these are arranged linearly
        return [*range(index, len(self.arr))] + [*range(0,index)]
        


    #with this methode basically we will get the index of the next empty space
    def find_slot(self,key,index):
        prob_range = self.get_prob_range(index)
        #now we need to check indecies
        for prob_index in prob_range:
            #if we found the empty space
            if self.arr[prob_index] is None:
                return prob_index
            #if we have same key there, we will store it there (modification)
            if self.arr[prob_index][0] == key:
                return prob_index
        #if all spaces are occupied
        raise Exception('HashMap Full.')


    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            #firstly we will store each element of every index and then we will check for our key
            element = self.arr[prob_index]
            if element is None:
                return
            #now we will check for our key
            if element[0] == key:
                return element[1]





    def __setitem__(self, key, val):
        h = self.get_hash(key)
        #case 1: if the sapce is empty
        if self.arr[h] is None:
            #this mean we do not have any key, value at that index
            self.arr[h] = (key,val) 
       
        #case 2 where we need to find the empty space when some other key,value is stored
        else:
            #if it is not empty pass the index to find_slot methode to find next empty space (its index)
            new_h = self.find_slot(key,h)
            #insert key, val at new place
            self.arr[new_h] = (key,val)
        print(self.arr)
             
                


    #Method to delete value in (I would say) Python Style :) :)
    #so pyhton have this operator that will give you the above functionality
    def __delitem__(self, key):
        h = self.get_hash(key)
        #may be the index what we got was not empty so our key, value is stored somewhere else so
        #we have to check every index linearly
        #for that lets get the range
        prob_range = self.get_prob_range(h)
        if self.arr[prob_index] is None:
            return # item not found so return. can also throw exception
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element[0] == key:
                element = None
        print(self.arr)




#Testing

t = HashTable()
print("Index Number for march 6: ", t.get_hash('march 6'))
print("Index Number for march 17: ", t.get_hash('march 17'))

t["march 6"] = 20
print("As we already have march 6 at index 9 are same so march 17 will be at index 0 ")
t["march 17"] =  88

t["march 17"] = 29
t["march 33"] = 234
print("value for this is : ",t["march 33"])
