#Q1
numbers = list(input("숫자를 입력하싱. :"))
def solution(numbers):
    numbers.reverse()
    print(''.join(numbers))
solution(numbers)

#Q2
numbers = int(input("숫자 수. : "))
def a(numbers):
    number = []
    for i in range(numbers):
        inputNumber = input("숫자. : ")
        number.append(inputNumber)
    number.sort()
    for k in range(len(number)):
        print(number[k])
a(numbers)

#Q3
members = int(input("회원 수 입력.: "))
def solution(members):
    member = []
    for _ in range(members):
        age, name = map(str, input("회원정보 입력. : ").split(" "))
        age = int(age)
        member.append((age, name))
    member.sort(key = lambda x:x[0])
    print(member)
    for k in member:
         print(k[0], k[1])
solution(members)
        



def task_3():
    N = int(input('회원의 수를 입력하세요 : '))
    myArr = []
    for i in range(N):
        age, name = input('{}번 째 회원의 나이와 이름을 입력하세요 : '.format(i + 1)).split()
        myArr.append([int(age), name])
    myArr.sort(key = lambda x : x[0])
    for age, name in myArr: print(age, name)
    myArr.sort(key = lambda x : x[0])
task_3()

        
#Q4
number = int(input("입력할 단어의 수. : "))
def word(number):
    words = []
    for _ in range(number):
        w = input("단어를 입력하시오.")
        words.append((len(w), w))
    words.sort()
    for k in range(1, number):
        if words[k]!=words[k-1]:
            print(words[k-1][1])
    if words[number-1]!=words[number-2]:
        print(words[number-1][1])
word(number)

#Q5
a = int(input("입력 수. :"))
def solution(a):
    b = []
    for _ in range(a):
        c = input("좌표를 입력하시오. ")
        b.append(c)
        b.sort()
    for i in range(len(b)):
        print(b[i])
solution(a)


