stack = []

def append():
    element = input("Enter the element: ")
    stack.append(element)
    print(element,"is added successfully!")

def pop():
    if not stack:
        print("Stack is empty")
    else:
        e = stack.pop()
        print("Removed element: ",e)

def display():
    print(stack)


while True:
    print("Operations \n1.add \n2.delete \n3.show \n4.quit")

    choice = int(input())

    if choice == 1:
        append()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter the correct operation!")


