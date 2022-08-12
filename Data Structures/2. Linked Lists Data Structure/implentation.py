class Node:
    def __init__(self, data = None, next = None):
        #number stored
        self.data = data
        #pointer to next number
        self.next = next


class linked_list:
    def __init__(self):
        #points to head of linked list
        self.head = None

    
    #to insert the value at the beggining if the linked list
    def insert_at_beginning(self, data):
        #making a node via creating a object
        node = Node(data, self.head)
        #as we insert in begging the node will become our head  (as head points to first element in this case)
        self.head = node




    #Methode for printing linked list
    def print(self):
        #if linked list is empty
        if self.head is None:
            print("Linked List is empty.")
            return

        #creating temporary variable and assigning head to it
        itr = self.head

        #string to store linked list
        llstr = ''

        #iterating in linked list using variable
        while itr:
            #put the data of that data in the string
            llstr += str(itr.data) + '---->'
            #moving head to next address
            itr = itr.next

        #printing linked list
        print(llstr)





    #for inserting at end we have to define a another methode
    def insert_at_end(self,data):
        #if linked list is empty
        if self.head is None:
            #just insert and give Null value as next address (as inserting at end)s
            node = Node(data,None)
            #head will point to that node now
            self.head = node
            return

        #if linked list is not blank
        #make a iter variable to iterate in the linked list

        iter = self.head

        #if the next address is not null means we have not reached the end of linked list 
        while iter.next:
            #so we have to keep iterating
            iter = iter.next

        #when it will get out of that loop it means we have reached to null means at last
        #so here we need to insert the new node in next address

        iter.next = Node(data, None)


    

    #methode that will take a list and will create a linked list
    def insert_values(self, data_list):
        #remove all the values to insert new ones
        self.head = None
        #we have to iterate throgh the list
        for data in data_list:
            #and simple insert every data one after other so we can use our insert at end function
            self.insert_at_end(data)



    #methode to get the length of the linked list
    def get_length(self):
        count = 0
        iter = self.head
        #while we do not reach end
        while iter:
            #for every entery inrement 1
            count += 1
            #giving next address of entery
            iter = iter.next

        return count




    #methode to remove a element when its index is given
    def remove_at(self,index):
        #if index is out of bound
        if index < 0 or index >= self.get_length():
            raise Exception("Invalide Index.")


        #if the index is 0 means we want to remove first element we can just our head to next address
        if index == 0:
            self.head = self.head.next
            return


        count = 0
        iter = self.head
        while iter:
            #we have to stop at the element before the index so that we can change address there
            #so thats why we will do
            if count == index - 1:
                #point to the next of next element means skipping the one we want to delete
                iter.next = iter.next.next
                break
            
            #traversing
            iter = iter.next
            count += 1

            #consider if we give 2 as index --> it will stop at 1 and then it will go to next of next
            #means at index 3




    #methode that will insert any value at specific index
    def insert_at(self,index,data):
        #if index is out of bound
        if index < 0 or index >= self.get_length():
            raise Exception("Invalide Index.")

        #if you give 0 index means you want to insert at beginning so we can use our function
        if index == 0:
            self.insert_at_beginning(data)
            return

        #for other cases
        count = 0
        iter = self.head
        while iter:
            #we have to stop at the element before the index so that we can change address there
            #so thats why we will do
            if count == index - 1:
                #making a node
                node = Node(data,iter.next)
                #as we are on a previous element so here the next address will be of node we made up ther
                iter.next = node
                break

            iter = iter.next
            count += 1

if __name__ == '__main__':
    ll = linked_list()
    #first insert 5
    ll.insert_at_beginning(5)
    #then insert at 89 at the beginning
    ll.insert_at_beginning(89)

    #insertin at end
    ll.insert_at_end(14)
    

    #it will delete all the above enteries and will enter 1 2 3 4 in linked list
    ll.insert_values([1,2,3,4])
    print(f"Length of the linked list is: {ll.get_length()}")
    print("Before Removing: ")
    ll.print()
    #testing removing
    ll.remove_at(2)
    print("After Removing: ")
    ll.print()

    #inserting 0 in the beginning
    ll.insert_at(0,0)
    print("Afetr insertion at the beginning: ")
    ll.print()

    #inserting 3 in the 4th position (3 index)
    ll.insert_at(3,3)
    print("Afetr insertion at the index 2: ")
    ll.print()