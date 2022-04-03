def reforma(a,c,l):
    area_piso = l * c
    volume = l * c * a
    area_paredes = 2*(a * l) + 2*(a * c)
    
    return area_piso, volume, area_paredes


def main():
    v1 = int(input())
    v2 = int(input())
    v3 = int(input())
    
    r_apiso, r_volume, r_aparedes = reforma(v1, v2, v3)

    print(r_apiso)
    print(r_volume)
    print(r_aparedes)


if __name__ == '__main__':
    main()
