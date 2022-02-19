#Q1
def solution():
    _over, _under, score = 0, 0, []
    number = int(input("논문 수를 입력하시오.: "))
    numbers = list(map(int, input("논문의 인용횟수를 입력하시오.").split()))
    for i in range(number):
        for k in range(number):
            if numbers[i] >= numbers[k]:
                _over+=1
            if numbers[i]<=numbers[k]:
                _under+=1
        score.append([numbers[i], _over, _under])
        _over, _under = 0,0     
    for j in range(number):
        if score[j][0] == score[j][1] == score[j][2]:
            print(score[j][0])


solution()


#Q2
def solution1():
    number = int(input("숫자를 입력하시오.: "))
    numbers_array, times = [], 0
    numbers_array.append(number)
    while True:
        if number == 1:
            break
        elif number % 3 == 0:
            number/=3
        elif (number-1) % 3 == 0:
            number-=1
            numbers_array.append(number)
            times+=1
            number/=3
        elif number % 2 == 0:
            number/=2 
        elif (number-1) % 2 == 0:
            number-=1
            numbers_array.append(number)
            times+=1
            number/=2
        else:
            number-=1
        numbers_array.append(number)
        times+=1
    print(times)
    for i in range(len(numbers_array)):
        print(int(numbers_array[i]), end = " ")
solution1()
