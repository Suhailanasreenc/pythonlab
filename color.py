'''color=["yellow","blue","red","black"]
print(color[0],",",color[-1])'''

clr = input("Enter color names separated by commas: ")
color_list = [color.strip() for color in clr.split(',')]
if color_list:
    print(f"First color: {color_list[0]}")
    print(f"Last color: {color_list[-1]}")
