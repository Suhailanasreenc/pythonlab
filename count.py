text = input("Enter a line of text: ")
words = text.split()
count = {}
for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
for word in count:
    print(word, ":", count[word])

