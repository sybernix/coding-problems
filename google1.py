S = "bcaaa"

sList = list(S)

insertions = 0

if sList[0] != "a":
    sList.insert(0, "a")
    insertions += 1

def nextLetter(letter):
    if letter == "a":
        return "b"
    elif letter == "b":
        return "c"
    else:
        return "a"

for i in range(len(sList) - 1):
    if sList[i+1] == nextLetter(sList[i]):
        continue
    if sList[i+1] == nextLetter(nextLetter(sList[i])):
        insertions += 1
    if sList[i+1] == sList[i]:
        insertions += 2

print("hi")