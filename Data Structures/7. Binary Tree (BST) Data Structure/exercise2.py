#Delete the Node with Technique 2:
                #find max from left and replace it with node you want to delete



class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    

    #method to find maximum node in tree
    def max(self):
        #max node will be always at right side
        #so if right subtree does not exits, it means root is greates
        if self.right is None:
            return self.data

        #if right subtree exits we have to traverse to last right most node 
        #that does not have any further childs
        return self.right.max()



    #method to find minimum node in the bst
    def min(self):
        #min node will be in left side (last node on left)
        #so if left side does not exists means root is the min
        if self.left is None:
            return self.data

        #if left side exits

        return self.left.min()



    
    #method to calculate sum of all nodes
    def cal_sum(self):
        #we have to calculate sum on each side
        #if and only if sides exits
        left_sum = 0
        right_sum = 0
        if self.left:
            left_sum = self.left.cal_sum()

        #now calculating right side sum
        if self.right:
            right_sum = self.right.cal_sum()

        return self.data + left_sum + right_sum


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




    #method to implement post order traversal technique
    def post_order(self):
        nodes = []
        #left side --- > right side ---> root node
        #if left side exits go there
        #it will recursivley run until we reach end of node that does not have any node on left side
        #so when a node wont have anything on left side and right side 
        #it will be simply appended to nodes list
        if self.left:
            nodes += self.left.post_order()
            


        #after left side we have to go to right subtree   
        if self.right:
            #go right
            nodes += self.right.post_order()

        
        
        #at the end we will visit root node
        nodes.append(self.data)

        return nodes



    

    #method to implement pre order traversal texhnique
    def pre_order(self):
        #root ---> left subtree ----> right subtree

        nodes = []

        #firstly simply append root node
        nodes.append(self.data)

        # now go left
        if self.left:
            nodes += self.left.pre_order()

        #lastly go right
        if self.right:
            nodes += self.right.pre_order()

        return nodes




    #method to delete a node from binary tree
    def delete(self,value):
        if value < self.data:
            #means its on left side
            #so recursively call delete() on left side
            if self.left:
                self.left = self.left.delete(value)

        
        elif value > self.data:
            #means its on right side
            if self.right:
                self.right = self.right.delete(value)

        else:
            #if both subtrees are none
            if self.left and self.right is None:
                return None
            
            #if we have right subtree but no left subtree
            if self.left is None:
                return self.right

            #if we have left subtree but no right subtree
            if self.right is None:
                return self.left


            #Here we have reached the node that we want to delete

            #so if we have found the value to be deleted 
            #according to  technique we have to replace it with maximum node on the left side of that node
            max_value = self.right.max()
            #putting that value in current node(to be deleted)
            self.data = max_value
            #now delete that minimum node
            self.left.delete(max_value)
        return self



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
    data = [4,3,5,6,7,3,110,34,33, 12]
    tree = buid_tree(data)
    print("Inorder traversal:", tree.in_order_traversal())
    tree.delete(3)
    print("Inorder traversal:", tree.in_order_traversal())

























