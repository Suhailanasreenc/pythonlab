print("1=occurence")
print("2=frequency")
print("3=factor of number")
print("4=exit")
n=int(input("enter the number of choice: "))
for i in range(1,4):
    if i==1:
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
        n=int(input("enter the number of choice: "))
    elif i==2:
        s = input("Enter a line of word: ")
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        for chari in freq:
            print(chari,":",freq[chari])
        n=int(input("enter the number of choice: "))
    elif i==3:
        fact=1
        num=int(input("enter a number: "))
        for i in range(1,num+1):
            fact*=i
            print("factorial=",fact)
        n=int(input("enter the number of choice: "))
    elif i==4:
        exit
