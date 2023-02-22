from bisect import bisect

stream = [6, 6, 0, 4, 8, 7, 6, 4, 7, 5]

intervals = []

for num in stream:
    if len(intervals) == 0:
        intervals = [num, num]
    else:
        index = bisect(intervals, num)
        if index % 2 == 1:
            continue
        elif index == 0:
            if intervals[0] - 1 == num:
                intervals[0] = num
            else:
                intervals = [num, num] + intervals
        elif index == len(intervals):
            if intervals[-1] == num or intervals[-1] + 1 == num:
                intervals[-1] = num
            else:
                intervals = intervals + [num, num]
        else:
            if intervals[index - 1] + 1 == num and intervals[index] - 1 == num:
                del intervals[index - 1]
                del intervals[index - 1]
            elif intervals[index - 1] == num or intervals[index - 1] + 1 == num:
                intervals[index - 1] = num
            elif intervals[index] == num or intervals[index] - 1 == num:
                intervals[index] = num
            else:
                intervals.insert(index, num)
                intervals.insert(index, num)

        print("hi")

ans = []
for i in range(int(len(intervals) / 2)):
    ind = i * 2
    ans.append([intervals[ind], intervals[ind + 1]])

print("hi")
