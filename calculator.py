def add():
    result=0
    while True:
        a=int(input('Enter number'))
        result+=a
        Check=True
        to_get_result=input("press small y to get result")
        if to_get_result=='y':
            Check=False
            break
    return result
def sub():
    result=int(input('enter number from which you want to subtract'))
    while True:
        a=int(input('Enter number'))
        result=result-a
        Check=True
        to_get_result=input("press small y to get result")
        if to_get_result=='y':
            Check=False
            break
    return result
def mul():
    result=1
    while True:
        a=int(input('Enter number'))
        result=result*a
        Check=True
        to_get_result=input("press small y to get result")
        if to_get_result=='y':
            Check=False
            break
    return result
def div():
    result=0
    a=int(input('Enter qoutient'))
    b=int(input('enter divisor'))
    result=a/b
    return result
def modolus():
    result=0
    a=int(input('Enter qoutient'))
    b=int(input('enter divisor'))
    result=a%b
    return result
while True:
    print('1 to do add')
    print('2 to do subtract')
    print('3 to do multiply')
    print('4 to do div')
    print('5 to do modulous')
    print('6 to exit')
    choice=int(input('enter choice what you want to do'))
    if choice ==1:
        print("result",add())
    if choice == 2:
        print("result",sub())
    if choice==3:
        print("result",mul())
    if choice==4:
        print("result",div())
    if choice==5:
        print("result",modolus())
    if choice==6:
        break
    else:
        print('enter valid number')
