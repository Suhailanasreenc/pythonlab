n1 = int(input("Enter number of elements in First list: "))
list1 = []

for i in range(n1):
    val = int(input(f"Enter element [{i+1}] for first list: "))
    list1.append(val)
    
n2 = int(input("Enter number of elements in Second list: "))
list2 = []

for i in range(n2):
    val = int(input(f"Enter element [{i+1}] for Second list: "))
    list2.append(val)


print("List1: ", list1)
print("List1: ", list2)


if(len(list1) == len(list2)):

    print("Both lists are of the same length: ",len(list1))
else:
    print("Lists are of different lengths")


if sum(list1) == sum(list2):
    print("Both lists sum to the same value: ", sum(list1))
else:
    print("Lists sum to different values")


s1 = []

for i in list1:
    for j in list2:
        if i == j:
            s1.append(i)
            


if s1:
    print("Common elements using: ", s1)
else:
    print("No common elements found.")
