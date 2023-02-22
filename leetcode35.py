nums = [1,3,5,6]
target = 7

def binarySearch(nums, target, start, end):
    if start >= end:
        return start
    midIdx = int((start + end)/2)
    midElement = nums[midIdx]
    if midElement == target:
        return midIdx
    elif midElement < target:
        return binarySearch(nums, target, midIdx + 1, end)
    else:
        return binarySearch(nums, target, start, midIdx)

sol = binarySearch(nums, target, 0, len(nums))

print("hi")