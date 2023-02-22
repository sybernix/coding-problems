fruits = [0,1,1,4,3]

longest = 0

total = 0
cont = 0

twoTrees = set()
lastTree = -1

for tree in fruits:
    if tree in twoTrees:
        total = total + 1
        if lastTree == tree:
            cont = cont + 1
        else:
            lastTree = tree
            cont = 1
    elif len(twoTrees) < 2:
        twoTrees.add(tree)
        lastTree = tree
        cont = 1
        total = total + 1
    else:
        if total > longest:
            longest = total
        twoTrees.clear()
        twoTrees.add(lastTree)
        total = cont + 1
        if tree == lastTree:
            cont = cont + 1
        else:
            twoTrees.add(tree)
            lastTree = tree
            cont = 1

if total > longest:
    longest = total

print("hi")