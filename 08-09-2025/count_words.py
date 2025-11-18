sen = input("Enter a Sentence")


clist = sen.split()

dlist = set(clist)


for i in dlist:
    print(i, "=", clist.count(i))
    
