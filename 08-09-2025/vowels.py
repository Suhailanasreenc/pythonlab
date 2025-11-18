word = input("Enter a Word: ")

vlist = []

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for i in word:

    for j in vowels:

        if i == j:

            vlist.append(i)



print(set(vlist))
    
