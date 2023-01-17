import re

pressedKeys = "22233"

# combinations = [1, 2, 4, 8]
#
# presses_array = [m.group(0) for m in re.finditer(r"(\d)\1*", pressedKeys)]
#
# num = 0

n = len(pressedKeys)
dp = [-1] * (n + 1)
dp[0] = 1

mod = 1000000007

for i in range(1, n + 1):
    char = pressedKeys[i-1]

    dp[i] = dp[i-1]

    if i >= 2 and char == pressedKeys[i - 2]:
        dp[i] = dp[i] + dp[i-2] % mod
    else:
        continue

    if i >= 3 and char == pressedKeys[i - 3]:
        dp[i] = dp[i] + dp[i-3] % mod
    else:
        continue

    if char == "7" or char == "9":
        if i >= 4 and char == pressedKeys[i-4]:
            dp[i] = dp[i] + dp[i-4] % mod

    print("dfg")

print("hi")