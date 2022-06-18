"""
Utilizando a definição de valor da temperatura com tupla da questão anterior, desenvolva uma função que soma
duas temperaturas que podem estar em Celsius ou em Fahrenheit. Se as duas temperaturas estiverem na mesma
escala, a resposta deve estar na mesma escala. Se as temperaturas estiverem em escalas diferentes, a resposta deve
ser dada na escala da segunda temperatura. Considere até 4 (quatro) casas decimais.
"""

def celsius(v):
    return (v - 32) * (5/9)


def fahrenheit(v):
    return (v * (9/5)) + 32




def analise(prim_valor, seg_valor):
    if prim_valor > seg_valor:
        return '1'
    else:
        return '2'


def soma(tmp_1, tmp_2):
    if tmp_1[1] == tmp_2[1]:    # Verifica se primeiro escala é a mesma
        # rescrevendo tupla
        return (tmp_1[0] + tmp_2[0], tmp_1[1])
    else:
        if tmp_2[1] == 'F':
            # Convertendo em Fahren e recriando tupla
            tmp_1 = (fahrenheit(tmp_1[0]), 'F')  
            somado = tmp_1[0] + tmp_2[0]
            return (round(somado,4), tmp_1[1])

        else:
            # Convertendo em Celsius e recriando tupla
            tmp_1 = (celsius(tmp_1[0]), 'C')  
            somado = tmp_1[0] + tmp_2[0]
            return (round(somado,4), tmp_1[1])


def main():
    temp_1 = (float(input()), input().upper()[0])
    temp_2 = (float(input()), input().upper()[0])

    print(soma(temp_1, temp_2))


if __name__ == '__main__':
    main()
