class TreeNode:
    def __init__(self,data,designation):
        #data of that node
        self.data = data
        self.designation = designation
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
        if condition == 'both':
            print(prefix + self.data+ '(' + self.designation + ')')
            if len(self.childeren) > 0: 
                for child in self.childeren:
                    child.print_tree('both')
        
        elif condition == 'name':
            print(prefix + self.data)
            if len(self.childeren) > 0: 
                for child in self.childeren:
                    child.print_tree('name')

        elif condition == 'designation':
            print(prefix + self.designation)
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


def buid_management_team():
    root = TreeNode('Saad','CEO')

    ml = TreeNode('Usman Yaqoob','ML Lead')
    sr = TreeNode('Ahmad','Sr ML Engineer')
    sr.add_child(TreeNode('Ali','Jr ML Engineer'))
    sr.add_child(TreeNode('Agha','Research Engineer'))
    ml.add_child(sr)
    ml.add_child(TreeNode('Shahid','Sr Researcher'))



    hr = TreeNode('Miss Jo bi ha','Lead')
    hr.add_child(TreeNode('Khan','Intern'))
    hr.add_child(TreeNode('hayar','Trainee'))
   




    #so laptop, cellphone and tv will be a childeren of Electronics
    root.add_child(ml)
    root.add_child(hr)

    return root
if __name__ == '__main__':
    root = buid_management_team()
    root.print_tree('both')
    root.print_tree('name')
    root.print_tree('designation')

    