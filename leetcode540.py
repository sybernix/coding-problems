nums = [1, 1, 2]

# def findSingle(nums, start, end):
#     midIdx = int((start + end) / 2)
#     if nums[midIdx - 1] == nums[midIdx]:
#         return findSingle(nums, start, midIdx)
#     elif nums[midIdx] == nums[midIdx + 1]:
#         return findSingle(nums, midIdx, end)
#     else:
#         return nums[midIdx]

start = 0
end = len(nums) - 1
ans = -1

while True:
    midIdx = int((start + end) / 2)
    if end - start <= 1:
        ans = nums[midIdx]
        break
    if nums[midIdx - 1] == nums[midIdx]:
        if midIdx % 2 == 1:
            start = midIdx + 1
        else:
            end = midIdx
    elif nums[midIdx] == nums[midIdx + 1]:
        if midIdx % 2 == 0:
            start = midIdx + 1
        else:
            end = midIdx
    else:
        ans = nums[midIdx]
        break

# single_element = findSingle(nums, 0, len(nums))

print("i")
