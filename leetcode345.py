s = "leetcode"

sList = list(s)

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vowelInstances = []

for i in range(len(sList)):
    if sList[i] in vowels:
        vowelInstances.append(sList[i])
        sList[i] = "*"

vowelInstances.reverse()

j = 0

for i in range(len(sList)):
    if sList[i] == "*":
        sList[i] = vowelInstances[j]
        j += 1

print("".join(sList))

