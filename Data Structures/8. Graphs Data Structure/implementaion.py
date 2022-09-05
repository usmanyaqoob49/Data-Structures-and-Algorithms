class Graph:
    #edges will recieve the pairs(Interconnected Nodes)
    def __init__(self, edges):
        self.edges = edges
        #representing routes in the form of list of tupeles would be expensive job while processing 
        #so we can represent all of them in the form of dictionary
        self.graph_dict = {}


        #our dictionay will look like:
        #so from islamabad we have two interconnected nodes
        #that we will pass as list to the key
        #"Islamabad" : ["Paris", "Dubai"], 
        #"Pais" : ["Dubai", "New York"]



        #as we are getting list of tupples that represents routes
        #so we have to iterate over it and we have to store things in dictionary
        
        for start, end in self.edges:
            #right now our dictionay is blank
            #but if the first key is there in our dictionary in this case that is Islamabad
            if start in self.graph_dict:
                #it this comes true it means we have a value list for node that comes now
                #so we will simply append that value
                #like Islamabad has two values "Paris" and "Dubai"
                #This condition turning true means we have start (key) names Islamabad already in dictionary
                #with its one vlaue consider it as Paris


                #so we will append its other value that is Dubai
                self.graph_dict[start].append(end)
            
            else:
            #now it means we do not have key that matches the start key word  in dictionary
                #insert that key values in dictioanry

                                        #values of dictionay will be list of routes connected to specific route
                self.graph_dict[start] = [end]

        #printing the graph dictionary
        print("Graph Dictionary: ", self.graph_dict)




    #method that takes start and the end and gives us all the path from start to end
    def get_path(self, start, end, path = []):
        path = path + [start]
        #if start and the end are the same we will just retrun start and that will be our path
        if start == end:
            return [path]

        #if we enter the starting point that do not have further nodes
        #like in routes example toronto is end of graph
        #so we have to check in the dictionary as we have values of only thos node taht has further nodes
        if start not in self.graph_dict:
            #it means we do not have any further node hence there is no path
            return []


        #now we use recursion to find the path
        paths = []
        #with below for loop we will get every node that is connected to our staring point
        #it means values of the dictionary for the specific start key

        for node in self.graph_dict[start]:
            #if we do not have that path node in our path
            if node not in path:
                #measn we have not visited the path

                #we have to recursively find the further paths from node to our ending point
                #so that we can return the complete path
                new_path = self.get_path(node, end, path)
                #we will append every path in between our node and endinf point
                for p in new_path:
                    paths.append(p)

        return paths
        


    

    #method to get the shortest distance between two nodes/routes
    #based on the minimum nodes in between
    def shortest_path(self,start,end, path = []):
        path = path + [start]
        #if start and the end are the same we will just retrun start and that will be our path
        if start == end:
            return path

            
        if start not in self.graph_dict:
            #it means we do not have any further node hence there is no path
            return None

        
        

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.shortest_path(node,end, path)
                #if sp is returning something
                if sp:
                    #now we have to check shoteest path list
                    #and we will compare their lengths to get shortest one

                    #if the shortest path array is empty or it has a path which has more nodes
                    if shortest_path is None or len(sp) < len(shortest_path):
                        #replace it with sp thats new shortest path
                        shortest_path = sp
        return shortest_path


if __name__ == "__main__":
    #so we can represent the two routes in the form of tuple
    routes = [
        ('Islamabad', 'Paris'),
        ('Islamabad', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris' , 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto')    
        ]
    
    Route_graph = Graph(routes)
    #representing routes in the form of list of tupeles would be expensive job while processing 
    #so we can represent all of them in the form of dictionary
    #like
    d = {
        #so from islamabad we have two interconnected nodes
        #that we will pass as list to the key
        "Islamabad" : ["Paris", "Dubai"], 
        "Pais" : ["Dubai", "New York"]
    }
    print('path: ', Route_graph.get_path('Islamabad','Toronto'))
    print('shortes path: ', Route_graph.shortest_path('Paris','New York'))