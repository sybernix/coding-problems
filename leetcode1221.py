import re

s = "RLRRLLRLRL"

substrings = 0
rCount = 0
lCount = 0
lastChar = None

for i in range(len(s)):
    if s[i] == "R":
        rCount += 1
    else:
        lCount += 1
    if rCount == lCount:
        substrings += 1
        rCount = 0
        lCount = 0

print(substrings)
# regex = re.compile("(%s|%s)" % ("(\w)\1*", "(\w)\1*"))
#
# count = re.findall(regex, s)
# print(count)