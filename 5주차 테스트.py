def solution():
    while True:
        array = []
        result = 'yes'
        a = input("입력 : ")
        if a == '.': break
        for i in a:
            if i == '(' or i == '[':
                array.append(i)
            elif i == ')':
                if len(array) != 0 and array[-1] == '(':
                    array.pop()
                else:
                    result = 'no'
                    break
            elif i ==']':
                if len(array)!= 0 and array[-1] == '[':
                    array.pop()
                else:
                    result = 'no'
                    break
        if len(array) == 0:
            print(result)
        else:
            print('no')
solution()