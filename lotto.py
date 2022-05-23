import random,time

def lotto():
    lotto=[]
    for i in range(0,6):
        lotto.append(random.randint(1,45))
    lotto.sort()
    return lotto

ans=input("로또번호 추출을 시작합니까?(y/n) : ")
if(ans=='y'or ans=='Y'):
    print("번호 추출중...\n")
    for i in range(1,6):
        print(str(i)+" ...\n")
        time.sleep(1)
    print("로또 번호는!!")
    print(lotto())

elif(ans=='n'or ans=='N'):
    print("로또 추출을 종료합니다.")
else:
    print("잘못 입력하셨습니다.")