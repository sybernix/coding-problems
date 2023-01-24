values = [1,2,3,7]

def helper(values, i):
    if i >= len(values):
        return 0
    else:
        ans = -10**10
        ans = max(ans, values[i] - helper(values, i+1))
        if i+1 < len(values):
            ans = max(ans, values[i] + values[i+1] - helper(values, i+2))
        if i+2 < len(values):
            ans = max(ans, values[i] + values[i+1] + values[i+2] - helper(values, i+3))
        return ans

alice = helper(values, 0)

if alice > 0:
    print("Alice")
elif alice < 0:
    print("Bob")
else:
    print("Tie")
