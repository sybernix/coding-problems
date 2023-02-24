import math

weights = [3,2,2,4,1,4]
days = 3

end = sum(weights)
start = max(weights)

# start_capacity = max(average_weight, max_weight)
start_capacity = int((start + end) / 2)

while True:
    ships = 1
    daily_weight = 0
    broke = False
    for w in weights:
        if w + daily_weight > start_capacity:
            ships = ships + 1
            if ships > days:
                start = start_capacity
                start_capacity = math.ceil((start + end) / 2)
                broke = True
                break
            daily_weight = w
        else:
            daily_weight = daily_weight + w
    if not broke:
        if end - start <= 1:
            break
        end = start_capacity
        start_capacity = int((start + end) / 2)


print("hi")