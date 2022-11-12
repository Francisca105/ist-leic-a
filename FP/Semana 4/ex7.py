def amigas(str1, str2):
    if len(str1) != len(str2):
        return False
        
    hit = 0

    for i in range(len(str1)):
        if str1[i] == str2[i]:
            hit += 1
    print(hit * 100/ len(str1))
    return hit / len(str1) > 0.9

amigas("amigas", "amigas")
amigas("amigas", "amigos")
amigas("amigas", "asigos")