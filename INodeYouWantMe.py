import random
class weightedGraph():
    def __init__(self):
        self.vertices = []
        self.adjList = {}
    def addNode(self,value):
        self.vertices.append(value)
    def addWeightedEdge(self,first,second,edgeWeight):
        if first not in self.adjList:
            self.adjList.setdefault(first,[])
            lst = [second,edgeWeight]
            self.adjList[first].append(lst)
        else:
            lst = [second,edgeWeight]
            self.adjList[first].append(lst)
    def removeDirectedEdge(self,first,second):
        for adj in self.adjList[first]:
            if len(adj) > 1:
                if adj[0] == second:
                    adj.clear()
    def getAllNodes(self):
        return self.vertices
    def getMat(self):
        return self.adjList
    def getNeighborNodes(self,first):
        return self.adjList[first]


def main():
    def createLinkedList(n):
        graph = weightedGraph()
        for node in range(0,n):
            graph.addNode(node)
            if node > 0:
                graph.addWeightedEdge(node-1,node,3)
        return graph
    def createRandomCompleteWeightedGraph(n):
        graph = weightedGraph()
        for node in range(n):
            graph.addNode(node)
        #create n*(n-1) edges with random weight
        for firstnode in range(0,n):
            for secondnode in range(0,n):
                if firstnode != secondnode:
                    weightededge = random.randint(1,20)
                    graph.addWeightedEdge(firstnode,secondnode,weightededge)
        return graph
    def djikstra(first):
        graph = createRandomCompleteWeightedGraph(10)
        amountofnodes = graph.getAllNodes()
        visited = []
        ret = {}
        ret[first] = 0#set distance of start node to 0
        for curr in amountofnodes:#initialize distance of all nodes to large #
            if curr != first:
                ret[curr] = 10000
        node = first
        while len(visited) != len(amountofnodes):#go through graph until all nodes are visited
            #minval used for finding next node
            minval = 100000
            for pair in graph.getNeighborNodes(node):
                #compare distance with old value where pair[0] is the node and pair[1] is the distance to that node
                if min(ret[node]+pair[1],ret[pair[0]]) < ret[pair[0]]:
                    ret[pair[0]] = min(ret[node]+pair[1],ret[pair[0]])
            if node not in visited:
                visited.append(node)
            #get the next node by finding the min among the unvisited nodes
            dictlist = ret.items()
            for item in dictlist:
                if item[1] < minval and item[0] not in visited:
                    minval = item[1]
                    node = item[0]
        return ret


    graph = createLinkedList(10)
    print(graph.getMat())
    print(djikstra(0))

if __name__ == "__main__":
    main()