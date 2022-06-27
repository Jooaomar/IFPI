"""01.Crie um dicionário e armazene nele os dados de livros: título, isbn, autor e preço. A 
chave do dicionários será um código numérico e sequencial, gerado automaticamente, iniciando 
pelo número 101 (cento e um). A leitura de uma descrição vazia para o título finaliza a leitura. Imprima todos os dados usando o padrão “Nome do Campo: valor”."""


def discionario():    
    
    discio = {}
    indices = 101
    
    while True:
        # Verificar condição
        nome_livro = input().strip()
        if (nome_livro == ''):
            break
            
        # Entradas
        isbn = input().strip()
        autor = input().strip()
        preco = float(input().strip())
        
        # Código
        discio[indices] = {}
        # titulo
        discio[indices]['Título'] = nome_livro
        # isbn
        discio[indices]['ISBN'] = isbn
        # autor
        discio[indices]['Autor'] = autor
        # preço
        discio[indices]['Preço'] = f"{preco:.2f}"
        
        # Indice
        indices +=1
    
    return discio


def main():
    
    dic = discionario()
    
    for chave in dic:
        
        titulo, isbn, autor, preco = dic[chave]
        
        # Info
        titulo = dic[chave][titulo]
        isbn = dic[chave][isbn]
        autor = dic[chave][autor]
        preco = dic[chave][preco]
        
        
        print(f"Código: {chave}")
        print(f"Título: {titulo}")
        print(f"ISBN: {isbn}")
        print(f"Autor: {autor}")
        print(f"Preço: {preco}")
    

if __name__ == '__main__':
    main()