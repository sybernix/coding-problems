n = 5
connections = [[4,3],[2,3],[1,2],[1,0]]

connected_nodes = {0}
changes = 0
i = 0
while True:
    if i >= len(connections):
        i = 0
    if len(connected_nodes) == n:
        break
    if connections[i][1] in connected_nodes:
        connected_nodes.add(connections[i][0])
        connections.remove(connections[i])
        continue
    elif connections[i][0] in connected_nodes:
        connected_nodes.add(connections[i][1])
        changes += 1
        connections[i] = [connections[i][1], connections[i][0]]
        connections.remove(connections[i])
    i += 1

print("hi")