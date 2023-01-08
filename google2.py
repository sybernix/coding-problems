segments = [911, 1, 3, 1000, 1000, 2, 2, 999, 1000, 911]

segmentSet = set()
pairs = []

for segment in segments:
    if segment in segmentSet:
        pairs.append(segment)
        segmentSet.remove(segment)
    else:
        segmentSet.add(segment)

if len(pairs) == 0:
    print(-1)

sortedPairs = sorted(pairs)
minDiff = 1001

for i in range(len(sortedPairs) - 1):
    diff = sortedPairs[i+1] - sortedPairs[i]
    if diff < minDiff:
        minDiff = diff

print("hi")