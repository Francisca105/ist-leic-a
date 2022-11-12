def racaman(n):
    res = []
    res.append(0)
    i = 1
    while i < n:
        ant = res[i-1] 
        if ant > i and not ant - i in res:
            res.append(ant - i)
        else:
            res.append(ant+i)
        i += 1
    return res
    
print(racaman(15))