# class V:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return V(self.x + other.x, self.y + other.y)
    
# v1 = V(1, 2)
# v2 = V(3, 4)
# v3 = v1 + v2

# print(v3.x + v3.y)

# ================

# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     i += 1

# ================

# list1= {22, 35, 51}
# list1.add((5,1))
# # print(list1) pour voir/tricher
# list2 = {4,51,5,1}
# list2.intersection_update(list1)
# print(list2)

# ================

numbers=[0,1,2,3,4,5]
print({n: n**2 for n in numbers if n%2==0})

# ================

def multipliers():
    return [lambda x : i * x for i in range(4)]
# Rien compris
print([m(2) for m in multipliers()])

# ================



