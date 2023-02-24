from heapq import heappush, heappop

k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]

n = len(profits)
projects = list(zip(capital, profits))
projects.sort()
# heapq is a min heap, but we need a max heap
# so we will store negated elements
q = []
ptr = 0
for i in range(k):
    while ptr < n and projects[ptr][0] <= w:
        # push a negated element
        heappush(q, -projects[ptr][1])
        ptr += 1
    if not q:
        break
    # pop a negated element
    w += -heappop(q)

print("hi")
