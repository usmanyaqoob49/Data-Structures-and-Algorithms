class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    #method to add a child in the tree (it can be root or any node)
    def add_child(self,data):
        #so if data we want to add already exits, it can not be added
        #as its the property of bst
        #self.data represent current node (where we are now)
        if data == self.data:
            return
        
        #if data is less than current node means it will go left of it
        if data < self.data:
            #we have to add data in left subtree


            #if our left node has a value (not empty)
                #means not NULL (or have value)
            if self.left:
                #so we will add its child
                #recursively call the add_child by passing the data
                self.left.add_child(data)
            
            #if left side is empty
            else:
                #make a node on left
                self.left = BinarySearchTree(data)



        #if data is greater than current node 
        else:
            #add data to right subtree

            #if right node is not empty
            if self.right:
                #make its child by recursively calling
                self.right.add_child(data)

            #if right node is empty
            else:
                self.right = BinarySearchTree(data)

    

    #method for traversing tree using in order technique
    def in_order_traversal(self):
        #list to store all the returned elements
        nodes = []
        #In order Technique:
                #visit left -----> root ------> right
        
        if self.left:
            #so add that in list but to fix the thing of more nodes on left to this
            #we have to recursively call this inorder
            nodes += self.left.in_order_traversal()


        #now visit root / base node
        nodes.append(self.data)


        #visit right subtree
        if self.right:
            nodes += self.right.in_order_traversal()

        return nodes




    #method for searching any value in Bst
    def search(self,val):
        #if the current node is the value then
        if self.data == val:
            return True

        
        #if val is less than our current node (root)
        #then value might be left subtree
        if val < self.data:
            #firstly check if we have something in left or not
            if self.left : 
                #so not our root will be left node and we will search recursively
                #in our left sub tree until we reach our node val
                return self.left.search(val)
            
            #if we do not have anything in left it means we do not have that value
            else:
                return False



        #if the value we are looking for is greater than our root 
        #then it might be in right subtree
        if val > self.data:
            #checking if our right subtree exits
            if self.right:
                #recursively call search() in right subtree
                return self.right.search(val)


            #if we do not have anything in right it means we do not have that value
            else:
                return False


def buid_tree(nodes):
    #passing first value of list
    root = BinarySearchTree(nodes[0])

    for i in range(0,len(nodes)):
        root.add_child(nodes[i])
    return root
if __name__ == '__main__':
    #data = [17, 4, 13, 45, 65, 78, 1, 2, 5]
    #tree = buid_tree(data)
    #print(tree.search(4))

    #same can be done passing strings
    data = ['A', 'D', 'E', 'C', 'F', 'D','hello']
    tree = buid_tree(data)
    print(tree.in_order_traversal())
