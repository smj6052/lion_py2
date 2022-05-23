def plus(num1,num2):
    result=num1+num2
    return result

def minus(num1,num2):
    result=num1-num2
    return result

def mul(num1,num2):
    result=num1*num2
    return result

def div(num1,num2):
    result=num1/num2
    return result

while(True):
    num1,num2=map(int, input('연산을 진행 할 두 숫자를 입력하시오 : ').split())
    i=input('어떤 연산을 수행할까요? ')
    if i=='+':
       print("{0} {1} {2} = {3}\n".format(num1,i,num2,plus(num1,num2)))
    elif i=='-':
        print("{0} {1} {2} = {3}\n".format(num1,i,num2,minus(num1,num2)))
    elif i=='*':
        print("{0} {1} {2} = {3}\n".format(num1,i,num2,mul(num1,num2)))
    elif i=='/':
        print("{0} {1} {2} = {3}\n".format(num14 5
        ,i,num2,div(num1,num2)))
    else:
        print('해당 연산은 지원하지 않습니다.\n')
