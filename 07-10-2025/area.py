

square = lambda a: a * a


rectangle = lambda l, b: l * b


triangle = lambda h, b:(h*b)/2


s = int(input("Enter the side of Square: "))

l = int(input("Enter the length of the rectangle: "))

b = int(input("Enter the breadth of the rectangle: "))

bt = int(input("Enter the breadth of the triangle: "))

h = int(input("Enter the height of the triangle: "))


print("Area of Square: ",square(s))
print("Area of Rectangle: ",rectangle(l, b))
print("Area of Triangle: ",triangle(bt, h))
