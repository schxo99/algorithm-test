def solution():
    a = int(input("수열의 수를 입력. : "))
    b = list(map(int, input("수를 입력. ").split()))
    for i in range(a):
        result = True
        for k in range(i+1, a):
            if b[i] < b[k]:
                print (b[k])
                break
            elif b[i] > b[k]:
                result = False                
                if result == False and k+1 == a:
                    print(-1)
    if b[-1] == b[a-1]:
            print(-1)
solution() 