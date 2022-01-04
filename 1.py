# q1
a = int(input("년도를 입력하시오.  "))
if a%4 == 0 and a%100 != 0 or a%400:
    print(1)
else:
    print(0)


# q2
a = int(input())
a=a+1
j = 0
for i in range(1, a):
    for j in range(a-i):
        print(' ', end="")
    for j in range(i):
        print("*", end="")
    print('')

# q3
a = input()

if (a.isdigit()) == True:
    print(chr(a))
else:
    print(ord(a))

