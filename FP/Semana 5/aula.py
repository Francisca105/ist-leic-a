def linearsearch(l, x):
    for i in range(len(l)):
        if l[i] == x:
            return 1
    return -1

#%timeit -n 1000 linearsearch(list(range(1000)), 700)
print(linearsearch(list(range(1000)), 700))