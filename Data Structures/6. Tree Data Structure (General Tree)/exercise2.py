class TreeNode:
    def __init__(self,data):
        #data of that node
        self.data = data
        self.childeren = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.childeren.append(child)


    def print_tree(self,condition): 
        level = self.get_level()
        prefix = ""
        if level == 0:  
            prefix = ""

        elif level == 1:
            prefix = "|-- "  

        elif level == 2:
            prefix = "|---- "   

        elif level == 3:
            prefix = "|------ " 
        #to print root
 
        if condition ==0 :
            print(prefix + self.data)
        
        elif condition == 1:
            if len(self.childeren) > 0: 
                for child in self.childeren:
                    child.print_tree('designation')


    def get_level(self):
        level = 0
        p = self.parent


        while p:
            level += 1
            p = p.parent
        return level


def buid_location():
    root = TreeNode('Global',)

    pak = TreeNode('Pakistan')
    kp = TreeNode('KPK')
    kp.add_child(TreeNode('Abbottabad'))
    kp.add_child(TreeNode('Peshawar'))
    pak.add_child(kp)
    sindh = TreeNode('Sindh')
    pak.add_child(sindh)
    sindh.add_child('Karachi')
    sindh.add_child('Malirs')



    usa= TreeNode('USA')
    ng = TreeNode('New Jersey')
    usa.add_child(ng) 
    ng.add_child(TreeNode('Princeton'))
    ng.add_child(TreeNode('Trenton'))
    cl = TreeNode('California')
    usa.add_child(cl) 
    cl.add_child(TreeNode('San Fransisco'))
    ng.add_child(TreeNode('Mountain'))




    root.add_child(pak)
    root.add_child(usa)

    return root
if __name__ == '__main__':
    root = buid_location()
    root.print_tree(0)


    