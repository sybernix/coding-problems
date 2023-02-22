ideas = ["coffee","donuts","time","toffee"]

ideas_set = [set() for _ in range(26)]
distinct = 0

for word in ideas:
    ideas_set[ord(word[0]) - ord('a')].add(word[1:])

for i in range(26):
    for j in range(i+1, 26):
        common = len(ideas_set[i].intersection(ideas_set[j]))
        distinct += (len(ideas_set[i]) - common) * (len(ideas_set[j]) - common) * 2

print("hi")
