preco = float(input('Digite o Preço do Produto:'))
p = float(input('Digite o Percentual de Desconto (0-100)%:'))

desconto = preco * (p / 100)
final = preco - desconto

print('O preco do produto é {}. Desconto de {}%.'.format(preco, p))
print('Valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto, final))