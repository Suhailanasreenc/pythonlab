li = []


n = input("Enter a Number: ")

for i in n:
    word = input("Enter Word: ")
    li.append(word)


def long():
    for i in li:
        a = len(li[0])
        if len(i) > a:
            a = len(i)

    print("length of the longest word is : ",a)


long()
