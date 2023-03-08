def func(x):

    if(x==0 or x==1):

        return 1

    return func(x-1)*x

func(6) #ça maaarche paaaas
# print("Hellow")

# # Intéressante façon de traiter cette liste
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [i*2 if i%2==0 else i**2 for i in lst1]
# print(lst2)

# r = 'C'
# print(int(r, 16))
