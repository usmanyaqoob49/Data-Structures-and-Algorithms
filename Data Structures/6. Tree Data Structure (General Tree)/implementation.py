from re import T
from tkinter.tix import Tree


class TreeNode:
    #this class represent individual node of the tree
    def __init__(self,data):
        #data of that node
        self.data = data
        self.childeren = []
        self.parent = None

    #method for adding a child node in over tree
    def add_child(self,child):
        #whenever you add a child you are adding a child to self object
        #so that self will become parent of child passed in arguement
        #so we are setting parent property of this child to self

        child.parent = self
        self.childeren.append(child)


    #method to print tree
    def print_tree(self): 
        #For printing a Good Tree
        # We need to get level of the node first
        level = self.get_level()
        #prefix will be space that will be added to every node based on the level
        prefix = ""
        #if its a root node
        if level == 0:  
            prefix = ""

        elif level == 1:
            prefix = "|-- "  

        elif level == 2:
            prefix = "|---- "   
        #to print root
        print(prefix + self.data)
        #we have to iterate over the childeren list to print nodes
        #self.childeren represents ----> laptop, cellphone and tv
        if len(self.childeren) > 0: 
            for child in self.childeren:
                #we will recursively call the print fucntion to print childs too
                #childs represents ---> childs of laptop, cellphone and tv
                child.print_tree()


    #method for checking level so that we can add spaces in print fucntion to show hirariachy
    def get_level(self):
        level = 0
        p = self.parent
        #we will be checking the parents a node have and this will igve is level
        #like for MacBook --> 1) Laptop and 2)Electronics
        #so loop will until a node dont have a parent

        while p:
            level += 1
            p = p.parent
        return level


def buid_product_tree():
    #root node will be our tree node
    root = TreeNode('Electronics')
    #Electronic is now stored in self.data
    

    laptop = TreeNode('Laptop')
    #now making childerens of Laptop
    laptop.add_child(TreeNode('MacBook'))
    laptop.add_child(TreeNode('HP'))
    laptop.add_child(TreeNode('Lenovo'))



    #making a tree node that will be a childeren of Electronic
    cellphone = TreeNode('CellPhone')
    #making childs node
    cellphone.add_child(TreeNode('Apple'))
    cellphone.add_child(TreeNode('Oppo'))
    cellphone.add_child(TreeNode('Vivo'))


    tv = TreeNode('TV')
    #making childs node
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Samsung'))


    #so laptop, cellphone and tv will be a childeren of Electronics
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root
if __name__ == '__main__':
    root = buid_product_tree()
    root.print_tree()
    