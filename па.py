d = 70
i = 0


def t_f(a):
    if a == d:
        return True
    else:
        return False


while i < 3:
    a = int(input("how many feet?: "))
    p = t_f(a)
    print(p)
    if p:
        break
    i += 1

a = 0
s = 120
while s <= 1060:
    s *= 2
    a += 1
print("Гене надо", a, "месяцев, чтобы побить мировой рекорд.")

n = int(input("how many days?: "))
for i in range(n+1):
    b = i * 2
print(n, "-days", b, "-bees")
