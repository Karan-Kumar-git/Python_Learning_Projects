def triangle(element,rows):
    for i in range(rows+1):
        space = " " * (rows - i)
        print(space+(element+" ")*i+space)

def square(element,rows):
    for i in range(rows):
        print((element+" ")*rows)

def rhombus(element,rows):
    for i in range(1,rows+1):
        space = " " * (rows - i)
        print(space+(element+"  ")*i+space)
    for i in range(rows-1,0,-1):
        space = " " * (rows - i)
        print(space+(element+"  ")*i+space)
        
     
element = input("Enter the element for making design : ")
rows = int(input("Enter the number of size of design : "))
while True:
    shape = input("Final process! Choose shape between (Square/triangle/rhombus) : ")
    shape = shape.lower()
    if shape == "square":
        square(element,rows)
    elif shape == "triangle":
        triangle(element,rows)
    elif shape == "rhombus":
        rhombus(element,rows)
    elif shape == "exit":
        break
    else:
        print("Invalid shape! Please enter valid shape")
        continue
    