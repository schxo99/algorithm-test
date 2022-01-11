# Q1
# number = list(map(int, input().split())) #0 : A의 개수 / 1 : x
# numbers = list(map(int, input().split()))

# def fun(number, numbers):
#     for i in range(number[0]):
#         if numbers[i] < number[1]:
#             print(number[i], end=" ")

# fun(number, numbers)


######################################################################
# Q2
# k = int(input("학생 수 :  "))
# def cute(k):
#     y =0
#     n =0
#     for i in range(0, k, 1):
#         a = int(input())
#         if a == 1:
#             y = y + 1
#         else:
#             n = n + 1 
#     if n < y:
#         print("Junhee is cute!")
#     else:
#         print("Junhee is not cute!")
        

#cute(k)
###################################################################

# Q3
# a= int(input())

# def star(a):
#     for i in range(1, a+1):
#         print(" "*(a-i), "*"*i)
#     for i in range(a-1, 0, -1):
#         print(" "*(a-i), "*"*i)
# star(a)