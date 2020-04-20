import random
class gridGraph:
    def __init__(self):
        self.vertices = {}
        self.adjList = {}
    def addGridNode(self,x,y,nodeVal):
        self.vertices[nodeVal] = [x,y]
    def addUndirectedEdge(self,first,second):#make sure nodes are neighbors and check to see if node already has a neigbor
        firstnode = self.vertices[first]
        secondnode = self.vertices[second]
        if abs(firstnode[0]-secondnode[0]) == 1 or abs(firstnode[1]-secondnode[1]) == 1:
            if first in self.adjList.keys():
                if second not in self.adjList[first]:
                    self.adjList[first].append(second)
            else:
                self.adjList[first] = [second]
            if second in self.adjList.keys():
                if first not in self.adjList[second]:
                    self.adjList[second].append(first)
            else:
                self.adjList[second] = [first]
    def removeUndirectedEdge(self,first,second):
        self.adjList[first].remove(second)
        self.adjList[second].remove(first)
    def getAllNodes(self):#return list of nodevals
        ret = []
        for key in self.vertices.keys():
            ret.append(key)
        return ret
    def getAlllNodes(self):#return nodevals with their respective coordinates
        return self.vertices
    def getNeighbors(self,node):
        return self.adjList[node]
    def getMat(self):#used for testing
        return self.adjList
def main():
    def createRandomGridGraph(n):
        graph = gridGraph()
        val = 0
        #coordinates will go up from 0,0 to n-1,n-1; val will go from 0 to n^2-1
        for x in range(n):
            for y in range(n):
                graph.addGridNode(x,y,val)
                val = val+1
        vertices = graph.getAllNodes()
        for node in vertices:
            if node+1 in vertices:#check for node above
                if (node+1)%n != 0:#check for graph edgecase Example: 0,5 and 1,0
                    if random.randint(0,1) == 1:
                        graph.addUndirectedEdge(node,node+1)
            if node-1 in vertices:#check for node below
                if (node%n) != 0:#check for graph edgecase Example: 1,0 and 0,5
                    if random.randint(0,1) == 1:
                        graph.addUndirectedEdge(node,node-1)
            if node+n in vertices:#check for node to right
                if random.randint(0,1) == 1:
                    graph.addUndirectedEdge(node,node+n)
            if node-n in vertices:#check for node to left
                if random.randint(0,1) == 1:
                    graph.addUndirectedEdge(node,node-n)
            return graph
    def modifiedPop(lst,number):#combines functionality of remove and pop
        for node in lst:
            if node == number:
                lst.remove(number)
                return number
    def heuristic(lst,finalNode):#determins node that is closest to finalNode using manhatten distance
        minval = 10000
        ret = 0
        nodeList = graph.getAlllNodes()
        for node in lst:
            nodeCoor = nodeList[node]
            finalCoor = nodeList[finalNode]
            if abs(finalCoor[0]-nodeCoor[0]) + abs(finalCoor[1]-nodeCoor[1]) < minval:
                minval = abs(finalCoor[0]-nodeCoor[0]) + abs(finalCoor[1]-nodeCoor[1])
                ret = node
        return ret
    def aStar(sourceNode,finalNode):#after running astar multiple times with different inputs for the graph size, i found that often times it couldn't find a path even though i checked all 4 directions when adding edges to any given node
        stack = []
        visited = []
        stack.append(sourceNode)
        curr = sourceNode
        while len(stack) != 0:#run while all connected nodes havent been visited
            if sourceNode in stack:
                stack.remove(sourceNode)
            if curr in stack:
                stack.remove(curr)
            visited.append(curr)#set curr as visited
            if curr == finalNode:
                return visited
            if curr not in graph.getMat():
                continue
            else:
                for node in graph.getNeighbors(curr):
                    if node not in visited:
                        stack.append(node)
            nextnodeup = heuristic(stack,finalNode)
            curr = modifiedPop(stack,nextnodeup)
        return "No Path Possible"


    graph = createRandomGridGraph(100)
    print(graph.getMat())
    print(aStar(0,9999))


if __name__ == "__main__":
    main()