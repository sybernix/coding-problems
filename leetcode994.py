from collections import deque

grid = [[2,1,1],[1,1,0],[0,1,1]]

q = deque()
fresh = 0
time = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 2:
            q.append([r,c])
        elif grid[r][c] == 1:
            fresh += 1

while q and fresh > 0:
    time += 1
    for i in range(len(q)):
        r, c = q.popleft()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            row = r + dr
            col = c + dc
            if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])):
                continue
            if grid[row][col] == 1:
                grid[row][col] = 2
                q.append([row, col])
                fresh -= 1

print(grid)
if fresh == 0:
    print(time)
else:
    print(-1)
