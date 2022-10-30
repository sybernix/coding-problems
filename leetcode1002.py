from collections import Counter

words = ["bella","label","roller"]

wordsAsLists = []
intersection = []

intersection = list(words[0])

for i in range(1, len(words)):
    intersection = list((Counter(intersection) & Counter(list(words[i]))).elements())

print("hi")