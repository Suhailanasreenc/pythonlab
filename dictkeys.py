i=int(input("enter the numbers between 1 to 15: "))
squares = {}
if i<=15:
    for i in range(1,i+1):
        squares[i] = i * i
    print(squares)
else:
    print("numbers between 1-15 only")
    
