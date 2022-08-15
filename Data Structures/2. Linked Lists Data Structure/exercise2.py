#Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. 
# That way you can iterate in forward and backward direction.

class Node:
    def __init__(self, data = None, next = None, prev = None):
        #To store data
        self.data = data
        #To store address of next node
        self.next = next
        #To store address of previous node
        self.prev = prev

class doubly_linked_list:
    def __init__(self):
        self.head = None



    #methode to get the last node of the linked list
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        #will return the address of last
        return itr    
        




    
    #methode that will take a list and will create a linked list
    def insert_values(self, data_list):
        #remove all the values to insert new ones
        self.head = None
        #we have to iterate throgh the list
        for data in data_list:
            #and simple insert every data one after other so we can use our insert at end function
            self.insert_at_end(data)




            
    #to insert at beginning
    def insert_at_beginning(self,data):
        #if linked list is empty
        if self.head is None:
            #first node will not have the previous node    
            node = Node(data,self.head, None)
            self.head = node

        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node



    #to insert at the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)
            




    #Method to return length of the string
    def get_length(self):
        count = 0
        if self.head is None:
            print("Empty linked list")
            return

        iter = self.head
        while iter:
            count += 1
            iter = iter.next
        
        return count



    #Method to insert at specigfic index
    def insert_at(self, index, data):
        #checking range of index
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index.")


        #if index = 0
        if index == 0:
            #we can simply use our beginning function to insert
            self.insert_at_beginning(data)
            return


        count = 0
        iter = self.head
        while iter:
            #we found that index where we will inert at that value
            if count == index - 1: 
                node = Node(data,iter.next, iter)
                #now we have to set this new node as a "previous node" of the next of this
                 #if it has a node in front
                if node.next:
                    node.next.prev = node
                #now set new node as next node of node on which we standing
                iter.next = node
                break

            
            iter = iter.next
            count += 1




    #Method for printing linked list in the forward direction
    def print_forward(self):
        #if linked list is empty
        if self.head is None:
            print("Linked List is empty.")
            return

        #if its not none
        
        iter = self.head
        l_list = ""
        while iter:
            l_list += str(iter.data) + '---->'
            iter = iter.next
        print("linked list in forward direction: ",l_list)


    #Method for printing linked list in the backward direction
    def print_backward(self):
        #if empty return
        if self.head is None:
            print("Linked List is empty.")
            return


        #last_node will store the address of last node
        last_node = self.get_last_node()
        #we will start iteration from the last node
        iter = last_node
        b_list = ""
        while iter:
            b_list += str(iter.data) + '---->'
            iter = iter.prev

        print("linked list is backward direction: ",b_list)




    #Methode to remove any specific index value
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
            

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        
        count = 0
        iter = self.head

        while iter:
            if count == index:
                #i have to skip the next node
                iter.prev.next = iter.next
                #now i have to fix the prev node of next.next 
                if iter.next:
                    iter.next.prev = iter.prev
                break

            iter = iter.next
            count+=1



if __name__ == '__main__':
    ll = doubly_linked_list()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    print("after adding new element: ",ll.print_forward())
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()

