from ex3 import area_circulo

def area_coroa (r1,r2):
    if r1 > r2:
        raise ValueError("erro")
    return area_circulo(r2) - area_circulo(r1)