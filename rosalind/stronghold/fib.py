def rabbits(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return k

    oneGen = rabbits(n - 1, k)
    twoGen = rabbits(n - 2, k)

    if n <= 4:
        return oneGen + twoGen
    return oneGen + (twoGen * k)


print(rabbits(33, 5))
