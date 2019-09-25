A = [12, 24, 35, 70, 88, 120, 155]

b = []

for i in A:
    if i % 2 == 0:
        b.append(i)

print(b)

for i in b:
    if i % 5 == 0:
        print(str(i), "is divisible by 5")
    if i % 7 == 0:
        print(str(i), "is divisible by 7")

