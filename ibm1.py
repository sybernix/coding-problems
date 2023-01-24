n = 5
arr = [3, 7, 5, 6, 6, 2]

tot = sum(arr)

sorted_arr = sorted(arr)
sorted_arr.reverse()

sum_array = []
last_num = - 1

for i in range(len(sorted_arr)):
    if sorted_arr[i] == last_num:
        sum_array[-1].append(sorted_arr[i])
    else:
        sum_array.append([sorted_arr[i]])
    last_num = sorted_arr[i]

A = []
sum_A = 0

for i in range(len(sum_array)):
    sum_A = sum_A + sum(sum_array[i])
    A = A + sum_array[i]
    if sum_A > tot - sum_A:
        break


print("hi")
