n = 5
k = 0
r_q = 4
c_q = 3
obstacles = [[5, 5], [4,2], [2,3]]
attack_num = 0
obstacles_set = set()

for obs in obstacles:
    coor = str(obs[0]) + "_" + str(obs[1])
    obstacles_set.add(coor)

# check left
for c_left in reversed(range(1, c_q)):
    print(c_left)
    coordinate = str(r_q) + "_" + str(c_left)
    if coordinate in obstacles:
        break
    else:
        attack_num += 1


# check right
for c_right in range(c_q + 1, n + 1):
    print(c_right)
    coordinate = str(r_q) + "_" + str(c_right)
    if coordinate in obstacles:
        break
    else:
        attack_num += 1

# check up
for r_up in range(r_q + 1, n + 1):
    print(r_up)
    coordinate = str(r_up) + "_" + str(c_q)
    if coordinate in obstacles:
        break
    else:
        attack_num += 1

# check down
for r_down in reversed(range(1, r_q)):
    print(r_down)
    coordinate = str(r_down) + "_" + str(c_q)
    if coordinate in obstacles:
        break
    else:
        attack_num += 1

# check up right
up_right_lim = min(n - r_q, n - c_q)
for i in range(1, up_right_lim + 1):
    print(i)
    coordinate = str(r_q + i) + "_" + str(c_q + i)
    if coordinate in obstacles:
        break
    else:
        attack_num += 1

# check up left
up_left_lim = min(n - r_q, c_q - 1)
for i in range(1, up_left_lim + 1):
    print(i)
    coordinate = str(r_q + i) + "_" + str(c_q - i)
    if coordinate in obstacles:
        break
    else:
        attack_num += 1

# check down left
down_left_lim = min(r_q - 1, c_q - 1)
for i in range(1, down_left_lim + 1):
    print(i)
    coordinate = str(r_q - i) + "_" + str(c_q - i)
    if coordinate in obstacles:
        break
    else:
        attack_num += 1

# check down right
down_right_lim = min(r_q - 1, n - c_q)
for i in range(1, down_right_lim + 1):
    coordinate = str(r_q - i) + "_" + str(c_q + i)
    if coordinate in obstacles:
        break
    else:
        attack_num += 1

print(attack_num)