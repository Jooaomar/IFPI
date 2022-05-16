def main():
    
    
    idades = [] 

    while True:
        i = int(input())

        if i == 0 and len(idades) == 0:
            break
        
        elif i == 0 and len(idades)>0:
            qtd = len(idades)
            media = sum(idades)/qtd
            menor = min(idades)
            maior = max(idades)
            
            print(f'{qtd}')
            print(f'{media:.2f}')
            print(f'{menor}')
            print(f'{maior}')
            break

        else:
            idades.append(i)



if __name__ == '__main__':
    main()
