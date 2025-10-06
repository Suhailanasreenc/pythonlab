text=str(input("Enter a string: "))
fchar=text[0]
result=fchar + text[1:].replace(fchar, "$")
print(result)
