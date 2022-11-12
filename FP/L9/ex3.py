from random import random

def baralho():
    np = ["esp", "copas", "ouros", "paus"]
    vlr = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    res = []
    for n in np:
        for v in vlr:
            res.append({"np": n, "vlr": v})
    return res

def baralha(baralho):
    i = 0
    while i < len(baralho):
        baralho[int(random() * 50) + 1] = baralho[i]
        i+=1
    return baralho

#print(baralha(baralho()))

def distribui(baralho):
    return baralho[:len(baralho)/4 + 1], baralho[len(baralho)/4 + 1: 2 * (len(baralho)/4) + 1], baralho[2 * (len(baralho)/4) + 1: 3*(len(baralho)/4) + 1], baralho[4*(len(baralho)/4):]
