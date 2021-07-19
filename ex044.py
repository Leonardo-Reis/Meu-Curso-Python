print(f"{' LOJAS BRABO ':=^40}")
preco = float(input('Digite o valor a ser pago: R$'))
print('''Opções de pagamento:
[ 1 ] A vista no dinheiro/cheque (10% de desconto)
[ 2 ] A vista no cartão (5% de desconto)
[ 3 ] Parcelar''')
opcao = int(input('Digite a sua opção para pagar: '))
if opcao == 1:
    valor = preco - preco*(10/100)
    print(f'Valor a ser pago: R${valor:.2f}.')
elif opcao == 2:
    valor = preco - preco*(5/100)
    print(f'Valor a ser pago: R${valor:.2f}.')
elif opcao == 3:
    print('''Quantidade de parcelas:
    Duas parcelas (preço normal)
    Três ou mais parcelas (20% de juros)''')
    parcela = int(input('Digite a quantidade de parcelas: '))
    if parcela == 2:
        valor = preco
        print(f'Valor a ser pago: R${valor:.2f}.')
    elif parcela >= 3:
        valor = preco + preco*(30/100)
        print(f'Valor a ser pago: R${valor:.2f}.')
    elif parcela == 1:
        valor = preco - preco*(5/100)
        print(f'valor a ser pago: R${valor:.2f}.')
    else:
        print('Quantidade invalida, tente novamente.')
else:
    print('Opção invalida, tente novamente.')
