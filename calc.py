""" number1=int(input('Enter the number: '))
number2=int(input('Enter the number: '))
Operator=input('Enter the operator: ')

if (Operator=='+'):
    print(number1+number2)
elif(Operator=='-'):
    print(number1-number2)
elif(Operator=='*'):
    print(number1*number2)
elif(Operator=='/'):
    print(number1/number2)
else:
    print('Enter a valid Operator: ') """

""" def add(a, b):
    answer=a + b
    print(str(a)+' + '+str(b)+' = '+str(answer)+"\n")

def sub(a, b):
    answer=a+b
    print(str(a)+' - '+str(b)+' = '+str(answer)+"\n")

def mul(a, b):
    answer=a*b
    print(str(a)+' * '+str(b)+' = '+str(answer)+"\n")

def div(a, b):
    answer=a/b
    print(str(a)+' / '+str(b)+' = '+str(answer)+"\n")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("input your choice: ")

    if choice=="a" or choice=="A":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a, b)
    elif choice=="b"or choice=="B":
        print("Subtraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        sub(a, b)   
    elif choice=="c"or choice=="C":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        mul(a, b)   
    elif choice=="d"or choice=="D":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        div(a, b) 
    elif choice == "e"or "E":
        print("Program ended")
        quit()  """

def add(a, b):
    answer=int(a+b)
    print(str(a)+ ' + '+str(b)+' = ', answer+'\n')
def sub(a, b):
    answer=int(a-b)
    print(str(a)+ ' - '+str(b)+' = ', answer+'\n')
def mul(a, b):
    answer=int(a*b)
    print(str(a)+ ' * '+str(b)+' = ', answer+'\n')
def div(a, b):
    answer=int(a/b)
    print(str(a)+ ' / '+str(b)+' = ', answer+'\n')

while True:
    print('A. Addition')
    print('B. Subtraction')
    print('C. Division')
    print('D. Multiplication')
    print('E. Exit')

    choice=input('Enter your choice here: ')

    if(choice=='a'or choice=='A'):
        print('Addition')
        a=int(input('Enter first number: '))
        b=int(input('Enter second number: '))
        add(a, b)
    elif(choice=='b'or choice=='B'):
        print('Subtraction')
        a=int(input('Enter first number: '))
        b=int(input('Enter second number: '))
        sum(a, b)
    elif(choice=='c'or choice=='C'):
        print('Division')
        a=int(input('Enter first number: '))
        b=int(input('Enter second number: '))
        div(a, b)
    elif(choice=='d'or choice=='D'):
        print('Multiplication')
        a=int(input('Enter first number: '))
        b=int(input('Enter second number: '))
        mul(a, b)
    elif(choice=='e'or choice=='E'):
        print('Terminate problem')
        quit()