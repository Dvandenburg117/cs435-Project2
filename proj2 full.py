import random
class Vertex:
    def __init__(self,n):
        self.id = n
        self.vertices = []
        self.adjacencyList = {}

class Graph(Vertex):
    def getNeighbors(self,n):
        idlst = []
        lst = []
        for key,val in self.adjacencyList:
            if key == n.id:
                for num in val:
                    idlst.append(num)
        for nodes in idlst:
            lst.append(Vertex(nodes))
        return lst
    #check to see if key is in adj list first, if so add to existing list
    def insertIntoAdj(self,key,value):
        if key in self.adjacencyList.keys():
            self.adjacencyList[key].append(value)
        else:
            self.adjacencyList[key] = []
            self.adjacencyList[key].append(value)
    #check to see if node was already made, if not then make it and add it to vertices
    def addNode(self,nodeVal):
        if nodeVal not in self.vertices:
            Vertex(nodeVal)
            self.vertices.append(nodeVal)
    def addUndirectedEdge(self,a,b):
        if  a.id in self.vertices and b.id in self.vertices:
            self.insertIntoAdj(a.id, b.id)
            self.insertIntoAdj(b.id, a.id)
    def addDirectedEdge(self,a,b):
        if a.id in self.vertices and b.id in self.vertices:
            self.insertIntoAdj( a.id, b.id)
    def removeUndirectedEdge(self,a,b):
        if a.id in self.vertices and b.id in self.vertices:
            self.adjacencyList[a.id].remove(b.id)
            self.adjacencyList[b.id].remove(a.id)
    def getAllNodes(self):
        return self.vertices
    def createRandomUnweightedGraphIter(self,n):
        #create n nodes
        for i in range(n):
            self.addNode(i)
        #go through all the nodes and link them randomly
        for i in range(n):
            node1 = Vertex(i)
            randomNode = random.random(0,n)
            node2 = Vertex(randomNode)
            self.addUndirectedEdge(node1,node2)
    def createLinkedList(self,n):
        #modify addDirectedEdge to only go in one direction
        for i in range(n):
            self.addNode(i)
        for i in range(1,n):
                node1 = Vertex(i-1)
                node2 = Vertex(i)
                self.addDirectedEdge(node1, node2)

class GraphSearch(Graph):
    def DFSRec(self,start,final):
        #keep track of nodes visited
        visited = []
        #all nodes were visited but no match found
        if visited.count(start.id) > 0:
            return None
        visited.pop(start.id)
        #check to see if node was found
        if start.id == final.id:
            return visited
        #preform the aformentioned operations with all of the nodes neighbors
        for child in start.getNeighbors():
            if self.DFSRec(child,final):
                return visited
        return None
    def DFSIter(self,start,final):
        visited = []
        DFSLst = []
        #get start node
        DFSLst.append(start)
        while len(DFSLst) != 0:
            #get next node of iteration
            child = DFSLst.pop()
            #check for visit, if not, then visit and get its neighbors
            if child.id not in visited:
                visited.append(child.id)
                tempLst = child.getNeighbors()
                #add neigbor nodes to stack
                for child2 in tempLst:
                    DFSLst.insert(0,child2)
        #check to see if final was found
        if final.id == visited[len(visited)- 1]:
            return visited
        else:
            return None
    def BFSRec(self,start,final):
        visited = []
        if visited.count(start.id) > 0:
            return None
        visited.insert(0,start.id)
        if start.id == final.id:
            return visited
        for child in start.getNeighbors():
            if self.BFSRec(child,final):
                return visited
        return None

    def BFSIter(self,start,final):
        visited = []
        BFSList = []
        BFSList.append(start)
        while len(BFSList) != 0:
            node = BFSList.pop()
            if node.id == final.id:
                visited.append(node.id)
                return visited
            if node.id in visited:
                continue
            visited.append(node.id)
            for child in node.getNeighbors():
                BFSList.insert(0,child)
        return None
class directedGraph(Graph):
    #addNode functions the same as it does in Graph so i left it as it
    #addDirectedEdge was also implemented in Graph
    def removeDirectedEdge(self,first,second):
        if first.id in self.vertices and second.id in self.vertices:
            for key,val in self.adjacencyList:
                if key == first.id:
                    for pair in val:
                        if len(pair) > 0:
                            if pair[0] == second.id:
                                pair.clear()
class weightedGraph(directedGraph):
    def __init__(self, n):
        super().__init__(n)
        self.adjancencyList = {}
        self.vertices = []
    def getwNeighbors(self,n):
        idlst = []
        lst = []
        for key,val in self.adjacencyList:
            if key == n.id:
                for pair in val:
                    if len(pair) > 0:
                        idlst.append(pair[0])
        for nodes in idlst:
            lst.append(Vertex(nodes))
        return lst
    def winsertIntoAdj(self,key,value):
        if key in self.adjacencyList.keys():
            self.adjancencyList[key].append(value)
        else:
            self.adjancencyList[key] = []
            self.adjancencyList[key].append(value)
    def addWeightedEdge(self,first,second,edgeWeight):
        if first.id in self.vertices and second.id in self.vertices:
            lst1 = [second.id,edgeWeight]
            self.winsertIntoAdj(first.id, lst1)

    #removeDirectedEdge was implemented in directedGraph

    def getAllNodes(self):
        return self.vertices
    def createRandomCompleteWeightedGraph(self,n):
        for i in range(n):
            self.addNode(i)
        index = n*(n-1)
        weight = random.random(1,10)
        for ii in range(index):
            node1 = Vertex(random.randint(1,n))
            randomNode = random.random(0, n)
            node2 = Vertex(randomNode)
            self.addWeightedEdge(node1,node2,random.randint(1,index))
    def createLinkedList(self, n):
        for i in range(n):
            self.addNode(i)
        for i in range(1,n):
            node1 = Vertex(i - 1)
            node2 = Vertex(i)
            self.addWeightedEdge(node1, node2, 5)
    #helper function for dijkstras
    def getWeightedEdge(self,first,second):
        for key,val in self.adjacencyList:
            if key == first.id:
                for pair in val:
                    if len(pair) > 0:
                        if pair[0] == second.id:
                            return pair[1]
    #helper function2 for dijkstras
    def noZeroMin(self,dic):
        minDis = 50000
        ret = []
        minDis = ""
        minVal = ""
        for key,val in dic:
            if val < min and val != 0:
                minDis = val
                minVal = key
        ret.append(minVal)
        ret.append(minDis)
        return ret

    def dijkstras(self,start):
        visited = []
        retDic = {}
        #set up distance array to infinity aka very big number
        for nodeVal in self.vertices:
            retDic[nodeVal] = 10000
        #manually set distance of start node to 0
        retDic[start.id] = 0
        #create node and assign it to start
        curr = start
        #keep going until all nodes are visited
        while len(self.vertices) != len(visited):
            #get neighbors of curr
            for node in self.getwNeighbors(curr):
                if node.id not in visited:
                    #find min between path from curr to neigbor, and the associated value for retDic
                    cost = min(retDic[curr.id]+self.getWeightedEdge(curr,node),retDic[node.id])
                    #if the path is shorter than whats stored, replace it
                    if cost < retDic[node.id]:
                        retDic[node.id] = cost
                    #add curr to visited
                    visited.append(curr.id)
                    #set curr to the smallest element in retDic that isnt stored in visited
                    nextNode = self.noZeroMin(retDic)
                    curr = Vertex(nextNode)
        return retDic

class gridVertex():
    def gridNode(self,x,y,nodeVal):
        self.x = x
        self.y = y
        id = nodeVal

class gridGraph(gridVertex):
    gridVertices = []
    gridAdList = {}
    #helper function for adding to adjList
    def addToAdList(self,first,second):
        lst1 = (first.id,first.x,first.y)
        lst2 = (second.id,second.x,second.y)
        self.gridAdList[first.id].append(lst1)
        self.gridAdList[second.id].append(lst2)
    def addGridNode(self,x,y,nodeVal):
        node = self.gridNode(x,y,nodeVal)
        self.gridVertices.append(node)
    def addUndirectedEdge(self,first,second):
        #make sure coordinates are neighbors
        if abs(first.x-second.x) == 1 and abs(first.y-second.y) == 1:
            self.addToAdList(first,second)
            self.addToAdList(second,first)
    def removeUndirectedEdge(self,first,second):
        #locate the 'first 'key in the dictionary and then delete the sublist that contains second and vice versa
        for key,val in self.gridAdList:
            if key == first.id:
                for pair in val:
                    if pair[0] == second.id:
                        pair.clear()
            elif key == second.id:
                for pair in val:
                    if pair[0] == first.id:
                        pair.clear()
    def getAllNodes(self):
        return self.gridVertices
    def createRandomGraph(self,n):
        nodeNum = 0
        #create n^2 nodes with nodeVal nodeNum
        for i in range(n+1):
            for ii in range(n+1):
                self.addGridNode(ii,i,nodeNum)
                nodeNum = nodeNum + 1
        #connect neighbors based on 50/50
        for node in self.gridVertices:
            for node2 in self.gridVertices:
                #check to find adjacent nodes
                if (abs(node.x - node2.x) == 1 and abs(node.y-node2.y) == 0) or (abs(node.x - node2.x) == 0 and abs(node.y-node2.y) == 1):
                    choice = random.randint(0,1)
                    if choice == 0:
                        self.addUndirectedEdge(node,node2)
    def getNeighbors(self,n):
        idlst = []
        lst = []
        for key,val in self.gridAdList:
            if key == n.id:
                for set in val:
                    idlst.append(val)
        for nodeVals in idlst:
            lst.append(nodeVals[0])
        return lst
    def noZeroMin(self,dic):
        minDis = 50000
        ret = []
        minDis = ""
        minVal = ""
        for key, val in dic:
            if val < minDis and val != 0:
                minDis = val
                minVal = key
        ret.append(minVal)
        ret.append(minDis)
        return ret
    def astar(self,sourceNode,destNode):
        visited = []
        retDic = {}
        parent = {}
        retList = []
        # set up distance array to infinity aka very big number
        for nodeVal in self.gridVertices:
            retDic[nodeVal] = 100000
            parent[nodeVal] = None
        # manually set distance of start node to 0
        retDic[sourceNode.id] = 0
        # create node and assign it to start
        curr = sourceNode
        # keep going until all nodes are visited
        while destNode.id not in visited:
            # get neighbors of curr
            for node in self.getNeighbors(curr):
                if node.id not in visited:
                    # find min between path from curr to neigbor, and the associated value for retDic
                    cost = min(retDic[curr.id] + 1, retDic[node.id])
                    # if the path is shorter than whats stored, replace it
                    if cost < retDic[node.id]:
                        retDic[node.id] = cost
                        parent[node.id] = curr.id
                    # add curr to visited
                    visited.append(curr.id)
                    # calculate hueristic and add to elements of retDic then set curr to the smallest element in retDic that isnt stored in visited
                    huehue = abs(curr.x-destNode.x) + abs(curr.y-destNode.y)
                    for val in retDic.values():
                        val = val + huehue
                    nextNode = self.noZeroMin(retDic)
                    curr = Vertex(nextNode)
        #setup ordered list to be returned
        while sourceNode.id not in retList:
            for key,val in parent:
                if key == destNode.id:
                    retList.append(key)
                    destNode = val
        return retList.sort()























