def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        for i in range(n - 1):
            a = a + b
            b = a - b
            print(a)


d = int(input("Enter a Number: "))

if d < 1:
    print("Invalid Number!!!")
else:
    fib(d)
                                        


