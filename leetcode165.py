version1 = "1.0.0.1.0"
version2 = "1.0.0.1.0.2"

version1_array = version1.split(".")
version2_array = version2.split(".")

length = max(len(version1_array), len(version2_array))
return_val = 0

for i in range(length):
    if i >= len(version1_array):
        val1 = 0
        val2 = int(version2_array[i])
    elif i >= len(version2_array):
        val2 = 0
        val1 = int(version1_array[i])
    else:
        val1 = int(version1_array[i])
        val2 = int(version2_array[i])
    if val1 > val2:
        return_val = 1
        break
    elif val1 < val2:
        return_val = -1
        break

print("hi")

