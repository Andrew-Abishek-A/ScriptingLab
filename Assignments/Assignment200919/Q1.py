def setfunc(list1):
    A = set(list1)
    for j in A:
        count = 0
        for i in range(2, j):
            if j % i == 0:
                print(str(j) + " is not a prime number")
                count += 1
                break
        if count == 0:
            print(str(j) + " is a prime number")
    return list(A)

A = [1, 1, 2, 5, 5, 7, 9]
print(setfunc(A))

