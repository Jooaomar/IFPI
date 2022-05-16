def main():
    
    
    idades = [] 

    while True:
        i = int(input('Escreva uma idade: '))

        if i == 0 and len(idades) == 0:
            break
        
        elif i == 0 and len(idades)>0:
            qtd = len(idades)
            media = sum(idades)/qtd
            menor = min(idades)
            maior = max(idades)
            
            print(f'A quantidade de pessoas é: {qtd}')
            print(f'A idade media é: {media:.2f}')
            print(f'A menor idade é: {menor}')
            print(f'A maior idade é: {maior}')
            break

        else:
            idades.append(i)



if __name__ == '__main__':
    main()
