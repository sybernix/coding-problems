from collections import defaultdict, deque

n = 3
redEdges = [[0,1],[1,2]]
blueEdges = []

adj = defaultdict(list)

for redEdge in redEdges:
    adj[redEdge[0]].append([redEdge[1], 0])

for blueEdge in blueEdges:
    adj[blueEdge[0]].append([blueEdge[1], 1])

answer = [-1] * n
visit = [[False, False] for i in range(n)]
q = deque()

q.append([0, 0, -1])
answer[0] = 0
visit[0][0] = visit[0][1] = True

while q:
    element = q.popleft()
    node, steps, prev_color = element[0], element[1], element[2]

    if node not in adj:
        continue

    for nei in adj[node]:
        neighbour, color = nei[0], nei[1]
        if not visit[neighbour][color] and color != prev_color:
            if answer[neighbour] == -1:
                answer[neighbour] = steps + 1
            visit[neighbour][color] = True
            q.append([neighbour, steps+1, color])



print("hi")
