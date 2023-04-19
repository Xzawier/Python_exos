#19.04.2023
lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
temp = [num for sublist in lst for num in sublist]
print(temp)






# #12.03.2023

# list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]
# sum = 0
# sum1 = 0
# for elem in list1:
#     if (elem % 2 == 0):
#         sum = sum + elem
#         continue
#     if (elem % 3 == 0):
#         sum1 = sum1 + elem

# print(sum , end=" ")
# print(sum1)
# # L'astuce est 2 et 3 divisent 6
# if (6 % 3 == 0):
#     print("OK")
# else:
#     print("Not OK")

# 10.03.20223
# for i in range(1,8,3):
#     print(i,end='')

# def func(x):

#     if(x==0 or x==1):

#         return 1

#     return func(x-1)*x

# func(6) #ça maaarche paaaas
# print("Hellow")

# # Intéressante façon de traiter cette liste
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [i*2 if i%2==0 else i**2 for i in lst1]
# print(lst2)

# r = 'C'
# print(int(r, 16))
# g = {3, 4, 5}
# h = {5, 2, 3}
# print(h - g)

# i = {3, 4}
# j = {5, 2}
# print(j - i)

# m = {4, 5, 4}
# n = {2, 3, 5}
# print(n - m)

# p = {3, 4, 5, 4}
# q = {5, 2, 3, 5}
# print(q - p)
