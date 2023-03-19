class V:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return V(self.x + other.x, self.y + other.y)
    
v1 = V(1, 2)
v2 = V(3, 4)
v3 = v1 + v2

print(v3.x + v3.y)

# ================

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1