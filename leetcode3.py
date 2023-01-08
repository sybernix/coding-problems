s = " "

max_length = 0

char_set = set()
substring = []

for i in range(len(s)):
    if s[i] in char_set:
        if len(substring) > max_length:
            max_length = len(substring)
        split_index = substring.index(s[i])
        to_delete = substring[:split_index + 1]
        substring = substring[split_index + 1:]
        char_set = char_set - set(to_delete)
        substring.append(s[i])
        char_set.add(s[i])

    else:
        substring.append(s[i])
        char_set.add(s[i])

if len(substring) > max_length:
    max_length = len(substring)

print(max_length)