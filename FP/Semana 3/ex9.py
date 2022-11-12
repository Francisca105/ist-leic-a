from math import floor

def dia_da_semana(dia,mes,ano):
    if mes < 1 or mes > 12:
        raise ValueError("Invalid month")
    if mes <= 2:
        mes += 12
    
    if mes > 12:
        ano -= 1

    def execFormula(q, m, K, J):
        return (q + floor(13 * (m + 1) / 5) + K + floor(K / 4) + floor(J / 4) - 2 * J) % 7

    h = execFormula(dia, mes, ano % 100, floor(ano / 100))

    def weekdayToString(weekday):
        if weekday == 0:
            return "sabado"
        if weekday == 1:
            return "domingo"
        if weekday == 2:
            return "segunda"
        if weekday == 3:
            return "terca"
        if weekday == 4:
            return "quarta"
        if weekday == 5:
            return "quinta"
        if weekday == 6:
            return "sexta"
        raise ValueError("Invalid weekday")

    return weekdayToString(h)

print( dia_da_semana(18, 1, 2014) )