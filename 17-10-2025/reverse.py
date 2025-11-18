#Create a function to read a number (minimum 4 digits) from the user and find the reverse of the
#number using loop in another function and display both number and reverse of the number.


def rev(num):
    rev = 0
    while num > 0:
        temp = num % 10
        rev = rev * 10 + temp
        num = num // 10
    return rev

    
def num():
    n = int(input("Enter a Number(minimum 4 digits: "))

    if n > 1000:
        print("Origninal number: ",n)
        print("Reversed number: ",rev(n))
    else:
        print("Enter a Number Greater than 1000")
num()
