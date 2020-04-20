import INodeYouWantMe
import random
class directedGraph():
    def __init__(self):
        self.vertices = []
        self.adjList = {}
    def addNode(self,value):
        self.vertices.append(value)
    def addDirectedEdge(self,first,second):
        if first not in self.adjList:
            self.adjList[first] = [second]
        else:
            self.adjList[first].append(second)
    def removeDirectedEdge(self,first,second):
        self.adjList[first].remove(second)
    def getAllNodes(self):
        return self.vertices
    def getMat(self):
        return self.adjList

def main():
    def createRandomDagIter(n):
        graph = directedGraph()
        for node in range(n):
            graph.addNode(node)
        for node in graph.vertices:
            randomedge = random.randint(0,n-1)
            if node is not randomedge:
                graph.addDirectedEdge(node,randomedge)
        return graph
    graph = createRandomDagIter(10)
    print(graph.getAllNodes())
    print(graph.getMat())






if __name__ == "__main__":
    main()