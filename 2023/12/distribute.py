# To distribute n objects over k places which can hold 0 or more objects and print it
# distribute(n,k)


def distribute(n, k, l=[]):
    print((n, k))
    if n == 0:
        return [0 for _ in range(k)]
    if k == 1:
        return [n]
    for i in range(n + 1):
        distribute


print(distribute(0, 3))
print(distribute(2, 1))
