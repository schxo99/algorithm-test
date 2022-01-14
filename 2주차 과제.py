# Q1
number = int(input("숫자의 개수: "))
numbers = list(map(int, input("숫자들을 입력하세요 : ").split()))
def aa(number, numbers):
    numbers = sorted(numbers)
    print(numbers[0], " ", numbers[number-1])

aa(number, numbers)
#######################################################

#Q2
k = int(input("테스트 케이스의 수를 입력하시오. "))
n, m=[], []
for j in range(k):
    ox = input("답을 입력하세요. : ")
    s, sum=0, 0 #s는 이어진 o 의 점수, sum
    for i in range(len(ox)):
        if ox[i] == 'o':
            s += 1
            n.append(s)        
        else: 
            s = 0
    for i in range(len(n)): #한 줄 점수 합하기
        sum =sum + n[i]
    m.append(sum) #점수를 m에 저장
    n.clear()
for l in range(k):
    print(m[l])
#######################################################

#Q3
number = int(input("총 수를 이력하세요.: "))

def score(number):
    everage, sum, eeverage, every,s  = [], 0, 0, 0, 0
    for i in range(number):
        everage = list(map(int, input("점수를 입력하세요.: ").split()))
        for k in range(1, everage[0]+1):
            sum += everage[k]
        eeverage = sum/everage[0]
        for j in range(1, len(everage) ):
            if eeverage<everage[j]:
                s+=1
        every = s/everage[0]*100
        print("%.3f" %every)
        everage, sum, eeverage, every,s  = [], 0, 0, 0, 0

score(number)
#######################################################

#Q4
number = int(input("입력하세요.: "))
def star(number):
    print(" "*(number-1) + "*")
    for i in range(number-1):
        print(" "*(number-2-i) + "*" + " "*(i*2+1) + "*")
star(number)

#Q5
size = int(input("크기 : "))
def star(size):
# size = 24
        for k in range(size-1, int(size/2), -11):
            for i in range(size-1, int(size/2), -6):
                if (i)==23:
                    print(" "*(k-1)+"*")
                    print(" "*(k-2)+"*"+" "+"*")
                    print(" "*(k-3)+"*"*5)
                    print(" "*(k-4)+"*"+" "*5+"*")
                    print(" "*(k-5)+"*"+" "+"*"+" "*3+"*"+" "+"*")
                    print(" "*(k-6)+"*"*5+" "+"*"*5)
                else: 
                    print(" "*(k-7)+"*"+" "*11+"*")
                    print(" "*(k-8)+"*"+" "+"*"+" "*9+"*"+" "+"*")
                    print(" "*(k-9)+"*"*5+" "*7+"*"*5)
                    print(" "*(k-10)+"*"+" "*5+"*"+" "*5+"*"+" "*5+"*")
                    print(" "*(k-11)+"*"+" "+"*"+" "*3+"*"+" "+"*"+" "*3+"*"+" "+"*"+" "*3+"*"+" "+"*")
                    print(" "*(k-12)+"*"*5+" "+"*"*5+" "+"*"*5+" "+"*"*5)
star(size)



