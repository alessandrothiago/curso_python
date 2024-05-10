nome = 'Alessandro Thiago'
altura = 1.85
peso= 115
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

#Alessandro Thiago tem 1.85 de altura,
#pesa 115 quilos e seu IMC é
#33.60116873630387