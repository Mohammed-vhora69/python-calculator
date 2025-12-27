import math
print("1.ADDITION--\"(+)\"")
print("2.SUBSTRACTION--\"(-)\"")
print("3.MULTIPLICATION--\"(x)\"")
print("4.DIVISION--\"(/)\"")
print("5.SQAURING--\"(x²)\"")
print("6.SQUARE ROOT--\"(√)\"")
print("7.CUBE ROOT--\"(∛)\"")
print("8.EXIT")
print()
choose = int(input("CHOOSE A ARiTHMATIC VALUE BETWEEN (1-8):- "))
print()
if (choose == 1):
    print("YOU HAVE CHOOSEN ADDITION \"+\"🤩") 
    a = int(input("ENTER A VALUE:- "))
    b = int(input("ENTER A VALUE:- "))
    print(f"YOUR ANSWER IS:- {a+b}")

elif (choose == 2):
    print("YOU HAVE CHOOSEN SUBSTRACTION \"-\"🤩")
    a = int(input("ENTER A VALUE:- "))
    b = int(input("ENTER A VALUE:- "))
    print(f"YOUR ANSWER IS:- {a-b}")

elif (choose == 3):
    print("YOU HAVE CHOOSEN MULTIPLICATION \"x\"🤩")
    a = int(input("ENTER A VALUE:- "))
    b = int(input("ENTER A VALUE:- "))
    print(f"YOUR ANSWER IS:- {a*b}")

elif (choose == 4):
    print("YOU HAVE CHOOSEN DIVISION \"%\"🤩")
    a = int(input("ENTER A VALUE:- "))
    b = int(input("ENTER A VALUE:- "))
    if(b==0):
        print("❌ ERROR ❌")
    else:
        print(f"YOUR ANSWER IS:- {a/b}")    

elif (choose == 5):
    print("YOU HAVE CHOOSEN SQUARING \"x²\"🤩")
    a = int(input("ENTER A VALUE:- "))
    print()
    if(a == 0):
        print("IT'S ALWAYS A ZERO 😏😐")
    else:
        print(f"YOUR ANSWER IS:- {math.pow(a , 2)}")
    
elif (choose == 6):
    print("YOU HAVE CHOOSEN SQUARE ROOT \"√\"🤩")
    a = int(input("ENTER A VALUE:- "))
    print()
    if(a < 0):
        print("❌ Square root of negative number not possible")
    if(a == 0):
        print("IT'S ALWAYS A ZERO 😏😐")
    else:
        print(f"YOUR ANSWER IS:- {math.sqrt(a)}")
    
elif (choose == 7):
    print("YOU HAVE CHOOSEN CUBE ROOT \"√\"🤩")
    a = int(input("ENTER A VALUE:- "))
    print()
    if(a == 0):
        print("IT'S ALWAYS A ZERO 😏😐")
    else:
        print(f"YOUR ANSWER IS:- {math.ceil(math.pow(a , 1/3))}")

elif (choose==8):
    print("👋 CALCULATOR CLOSED. THANK YOU! 😊")

else:
    print("❌INVALID CHOICE. PLEASE SELECT BETWEEN (1-8)")

print()
print("THANKS FOR CHOOSING US🥰❗")





   



