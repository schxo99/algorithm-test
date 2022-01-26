##Q1
def solution():
    numbers, result3 = [], 0
    N = int(input("입력할 수의 개수.:  "))
    for _ in range(N):
        number = int(input("숫자를 입력하시오. : "))
        numbers.append(number)
    result1 = sum(numbers)/N
    print("산술평균 : ",round(result1)) #평균반올림
    numbers.sort()
    print("중앙값 : ",numbers[int(N/2)])  #중앙값 
    for i in range(1,N):
        if numbers[0]==numbers[i]:
            result3 += 1
        else: 
            result3 = 0
    if result3 == 0:
        print("최빈값 or 두번쨰 수 : ",numbers[1])
    result4 = numbers[N-1]-numbers[0]
    print("범위 : ",result4)
solution()

#Q2
def solution():
    array_result = []
    array = list(map(int, input("배열을 입력하시오. : ").split(",")))
    commands = int(input("추출할 배열 수 : "))
    for _ in range(commands):
        command = list(map(int, input("배열을 입력하시오.: ").split(",")))
        array_list = array[command[0]-1:command[1]]
        array_list.sort()
        array_result.append(array_list[command[2]-1])
    print(array_result)
solution()


#Q3
def solution():
    N, sum = [], ''
    n = list(map(str, input("수들을 입력하시오. : ").split()))
    for i in range(len(n)):
        N.append([n[i]*2, n[i]])
    N.sort(reverse = True)
    for k in range(len(N)):
        sum+=N[k][1]
    print(sum)
solution()    