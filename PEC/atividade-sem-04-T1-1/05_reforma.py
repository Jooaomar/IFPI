def reforma(a,c,l):
    area_piso = l * c
    volume = l * c * a
    area_paredes = 2*(a * l) + 2*(a * c)
    
    return area_piso, volume, area_paredes


def main():
    v1 = int(input('Altura: '))
    v2 = int(input('Comprimento: '))
    v3 = int(input('Largura: '))
    
    r_apiso, r_volume, r_aparedes = reforma(v1, v2, v3)

    print(f'Área do piso da sala: {r_apiso}')
    print(f'Volume da sala: {r_volume}')
    print(f'Área das paredes da sala: {r_aparedes}')


if __name__ == '__main__':
    main()
