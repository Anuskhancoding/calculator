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
    result=0
    while True:
        a=int(input('Enter number'))
        result-=a
        Check=True
        to_get_result=input("press small y to get result")
        if to_get_result=='y':
            Check=False
            break
    return result
# print("Result is",add())
print("result is",sub())

