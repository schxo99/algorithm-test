# Q1
# i = int(input("점수를 입력하시오.  "))
# def score(i):
#     if 95 < i:
#         return 'A+'
#     elif 90 < i:
#         return 'A'
#     elif 85 < i:
#         return 'B+'
#     elif 80 < i:
#         return 'B'
#     elif 75 < i:
#         return 'C+'
#     elif 70 < i:
#         return 'C'
#     elif 65 < i:
#         return 'D+'
#     elif 60 < i:
#         return 'D'
#     else:
#         return 'F'

# score(i) 
# print(score(i)) 

###########################################################

# #Q2
# def time(i):
#     m = i/60
#     m = int(m)
#     s = i%60
#     h = m/60
#     h = int(h)
#     m = m%60
#     print(h,'시간', m,'분', s,'초')

# i = int(input("초를 입력하세요"))
# time(i)

###########################################################

#Q3
# a= input()
# def quadrant(a):
#     b = a.split()
#     x = b[0]
#     y = b[1]
#     x = int(x)
#     y = int(y) 
#     # print(x, y)
#     if 0<= x and 0<= y:
#         return 'Quadrant 1'
#     elif 0<= x and 0>=y:
#         return 'Quadrant 4'
#     elif 0>= x and 0<= y:
#         return 'Quadrant 2'
#     else:
#         return 'Quadrant 3'

# print(quadrant(a))

###########################################################

#Q4
# for i in range(1, 10):
#     for k in range(1, 4):
#         print(k,"*",i,"=", k*i, end="\t")
#     print()
# print()
# for i in range(1, 10):
#     for k in range(4, 7):
#         print(k,"*",i,"=", k*i, end="\t")
#     print()
# print()
# for i in range(1, 10):
#     for k in range(7, 10):
#         print(k,"*",i,"=", k*i, end="\t")
#     print()

#############################################################

#Q5
# n = input("입력")
# def star(n):
#     n = int(n)
#     for i in range(n, 0, -2):
#         print(" "*int(((n-i)/2)), "*"*i)

# star(n)
