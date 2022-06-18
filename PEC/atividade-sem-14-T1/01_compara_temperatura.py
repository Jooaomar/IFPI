def celsius(v):
    return (v - 32) * (5/9)


def fahrenheit(v):
    return (v * (9/5)) + 32


def compara_temperatura(tmp_1, tmp_2):
    if tmp_1[1] == tmp_2[1]:    # Verifica se primeiro escala é a mesma
        return max(tmp_1, tmp_2)
    else:
        if tmp_2[1] == 'F':
            # Convertendo em Fahren e recriando tupla
            convert_temp_1 = (fahrenheit(tmp_1[0]), 'F')  
            result = analise(convert_temp_1[0], tmp_2[0]) 
            if result == '1':
                return tmp_1
            else:
                return tmp_2
        else:
            # Convertendo em Celsius e recriando tupla
            convert_temp_1 = (celsius(tmp_1[0]), 'F')  
            result = analise(convert_temp_1[0], tmp_2[0]) 
            if result == '1':
                return tmp_1
            else:
                return tmp_2

def analise(prim_valor, seg_valor):
    if prim_valor > seg_valor:
        return '1'
    else:
        return '2'

def main():
    
    temp_1 = (float(input()), input().upper()[0])
    temp_2 = (float(input()), input().upper()[0])

    print(compara_temperatura(temp_1, temp_2))


if __name__ == '__main__':
    main()
