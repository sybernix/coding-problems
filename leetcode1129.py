n = 3
redEdges = [[0, 1], [1, 2]]
blueEdges = []

class Node:
    def __init__(self, index):
        self.index = index
        self.blueNeighbours = set()
        self.redNeighbours = set()

    def addBlueNeighbour(self, blueNeighbour):
        self.blueNeighbours.add(blueNeighbour)

    def addRedNeighbour(self, redNeighbour):
        self.redNeighbours.add(redNeighbour)

    def getBlueNeighbours(self):
        return self.blueNeighbours

    def getRedNeighbours(self):
        return self.redNeighbours

    def getIndex(self):
        return self.index

nodesBlueStart = []
nodesRedStart = []

for i in range(n):
    newNode = Node(i)
    nodesBlueStart.append(newNode)
    nodesRedStart.append(newNode)

for redEdge in redEdges:
    nodesBlueStart[redEdge[0]].addRedNeighbour(nodesBlueStart[redEdge[1]])

for blueEdge in blueEdges:
    nodesBlueStart[blueEdge[0]].addBlueNeighbour(nodesBlueStart[blueEdge[1]])

minDistances = [101] * n
minDistances[0] = 0

def findMinDistances(nodes, minDistances, lastColor):
    distance = 0
    while len(nodes) > 0:
        currentNode = nodes.pop(0)
        distance = distance + 1
        if lastColor == 'b':
            neighbours = currentNode.getRedNeighbours()
            for neighbour in neighbours:
                if distance < minDistances[neighbour.getIndex()]:
                    minDistances[neighbour.getIndex()] = distance
            lastColor = 'r'

        elif lastColor == 'r':
            neighbours = currentNode.getBlueNeighbours()
            for neighbour in neighbours:
                if distance < minDistances[neighbour.getIndex()]:
                    minDistances[neighbour.getIndex()] = distance
            lastColor = 'b'
    return minDistances


minDistancesBlueStart = findMinDistances(nodesBlueStart, minDistances, 'b')
minDistancesFinal = findMinDistances(nodesRedStart, minDistancesBlueStart, 'r')

print("hi")