cells = [0, 1, 0, 1, 1, 0, 0, 1]
n = 700

def nextDayCells(cells):
    newCells = cells.copy()
    newCells[0] = 0
    newCells[-1] = 0
    for i in range(1, len(cells) - 1):
        if cells[i - 1] == cells[i + 1]:
            newCells[i] = 1
        else:
            newCells[i] = 0
    return newCells

states = set()
states.add(''.join(map(str, cells)))

for i in range(n):
    newCells = nextDayCells(cells)
    pattern = ''.join(map(str, newCells))
    if pattern in states:
        print(len(states))
        cycleLength = len(states)
        break
    else:
        states.add(pattern)
        cells = newCells
    print(cells)

print(''.join(map(str, cells)))
