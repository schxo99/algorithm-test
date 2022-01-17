#Q1
# a3 = []
# sum = 0
# a1 = int(input("크기 : "))
# a2 = list(map(int, input("입력. : ")))
# for i in range(a1):
#     sum += a2[i]
# print(sum)


#Q2
# list=[]
# while True:
#     temp=float(input("온도 : "))
#     if temp == 999:
#         break
#     list.append(temp)
# for i in range(len(list)-1):
#     print("%.2f" %(list[i+1]-list[i]))

#Q3
# while True:

#     a = list(map(int, input("세 변의 길이: ").split(" ")))
#     a.sort()
#     if a[0] == 0:
#         break
#     elif a[0] + a[1] <= a[2]:
#         print("Invalid")
#     elif a[0] == a[1] == a[2]:
#         print("Equilateral")
#     elif a[0] != a[1] != a[2]:
#         print("Scalene")
#     elif a[0] == a[1] != a[2] or a[0] == a[2] != a[1] or a[0] != a[0] == a[2]:
#         print("Isosceles") 