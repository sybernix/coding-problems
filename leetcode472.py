words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]

words_set = set(words)
concat_words = []

def checkConcat(word, isInitial):
    if not isInitial and word in words_set:
        words_set.add(word)
        return True
    isInitial = False
    for i in range(1, len(word)):
        left = word[:i]
        right = word[i:]

        if left in words_set:
            if checkConcat(right, isInitial):
                return True
    return False


for word in words_set:
    if checkConcat(word, True):
        concat_words.append(word)

print("hi")