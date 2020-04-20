import random
class Graph():
    def __init__(self):
        self.vertices = []
        self.adjList = {}
    def addNode(self,value):
        self.vertices.append(value)
    def addUndirectedEdge(self,first,second):
        #check to see if nodes already have a neighbor or not
        if first not in self.adjList:
            self.adjList[first] = [second]
        else:
            self.adjList[first].append(second)
        if second not in self.adjList:
            self.adjList[second] = [first]
        else:
            self.adjList[second].append(first)
    def getNeighbors(self,n):
        return self.adjList[n]
    def removeUndirectedEdge(self,first,second):
        self.adjList[first].remove(second)
        self.adjList[second].remove(first)
    def getAllNodes(self):
        return self.vertices
    def getMat(self):#get the adjacency matrix - used for testing
        return self.adjList

class graphSearch(Graph):
    def DFSIter(self,first,second):#DFS uses queues so
        visited = []
        DFS = []
        DFS.append(first)
        while len(DFS) != 0:
            child = DFS.pop()
            if child not in visited:
                visited.append(child)
            if child == second:
                return visited
            else:
                for neighbor in self.getNeighbors(child):
                   if neighbor not in visited:
                       DFS.append(neighbor)
        return None
    def DFSRECHelper(self,second,stack,visited):#helper function so that visited and stack dont reset on recurse
        if len(stack) == 0:
            return None
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)
        if curr == second:
            return visited
        for node in self.getNeighbors(curr):
            if node not in visited:
                stack.append(node)
        return self.DFSRECHelper(second,stack,visited)
    def DFSRec(self,start,end):#finds path from start to end if it exists, returns none if it doesnt
        visited = []
        stack = []
        stack.append(start)
        return self.DFSRECHelper(end,stack,visited)
    def BFSRECHelper(self,graph,queue,visited):#helper function so that so that visited and queue dont reset on recurse
        if len(queue) == 0:
            return visited
        curr = queue.pop(0)
        if curr not in visited:
            visited.append(curr)
        for node in self.getNeighbors(curr):
            if node not in visited:
                queue.append(node)
        return self.BFSRECHelper(graph,queue,visited)
    def BFSRec(self,graph):#returns all connected nodes in graph
        visited = []
        first = self.vertices[0]
        queue = []
        queue.append(first)
        return self.BFSRECHelper(graph,queue,visited)

    def BFSIter(self,graph):#note use of pop(0) since we're using a queue
        visited = []
        first = self.vertices[0]
        DFS = []
        DFS.append(first)
        while len(DFS) != 0:
            child = DFS.pop(0)
            if child not in visited:
                visited.append(child)
                for neighbor in self.getNeighbors(child):
                    DFS.append(neighbor)
        return visited



def main():
    def createRandomUnweightedGraph(n):#keys of adjList will not be sorted
        graph = graphSearch()
        for node in range(n):
            graph.addNode(node)
        for node in graph.vertices:
            randomedge = random.randint(0,n-1)
            if node is not randomedge:#make sure a node cant connect to itself
                graph.addUndirectedEdge(node,randomedge)
        return graph
    def createLinkedList(n):
        graph = graphSearch()
        for node in range(n):
            graph.addNode(node)
        for node in range(1,n):
            graph.addUndirectedEdge(node-1,node)
        return graph
    graph = createRandomUnweightedGraph(10)
    print(graph.getMat())
    print(graph.DFSIter(0,9))
    print(graph.DFSRec(0,9))
    print(graph.BFSIter(graph))
    print(graph.BFSRec(graph))



if __name__ == "__main__":
    main()









