class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_path(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def shortest_path(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        shortest_paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.shortest_path(node,end,path)
                for p in new_path:
                    if len(shortest_paths)==0 or len(p) < len(shortest_paths[0]):
                        shortest_paths = [p]
                    elif len(p) == len(shortest_paths[0]):
                        shortest_paths.append(p)
        return shortest_paths

if __name__=="__main__":
    routes = [('Mumbai','Paris'),('Mumbai','Dubai'),('Paris','Dubai'),('Paris','NewYork'),('Dubai','NewYork'),('Dubai','Qatar'),('NewYork','Toronto')]
    flight_route = Graph(routes)
    print(flight_route.graph_dict)
    start = 'Mumbai'
    end = 'Toronto'
    print(f'Routes between {start} and {end} :-')
    for sl,paths in enumerate(flight_route.get_path(start,end)):
        print(f' {sl+1}.{" -> ".join(paths)}')
    print(f'Shortest Routes between {start} and {end} : -')
    for sl,paths in enumerate(flight_route.shortest_path(start,end)):
        print(f' {sl+1}.{" -> ".join(paths)}')