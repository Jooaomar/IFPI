anos = int(input("Quantos anos de serviço? "))
valor_por_ano = float(input("Denina o valor do bônus anual: "))
bonus = anos * valor_por_ano
print(f'A bonificação referente ao(s) {anos} anos trabalhado(s) é: %1.2f'%(bonus))
