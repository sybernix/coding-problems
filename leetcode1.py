nums = [3, 3]
target = 6

hashTable = {}
for i in range(len(nums)):
    num = nums[i]
    if num in hashTable:
        hashTable[num].append(i)
    else:
        hashTable[num] = [i]
    complement = target - num
    if complement in hashTable:
        for idx in hashTable[complement]:
            if idx != i:
                print([i, idx])