n1 = int(input('Digite um numero: ')) # este é um numero inteiro.
n2 = int(input('Segundo numero:'))
s = n1+n2
# print('A soma entre', n1, 'e', n2, 'é de', n1+n2) : muita virgula e muita poluíção visual.

print('A soma entre {} e {} é de {}'.format(n1, n2, s)) # usa os colchetes como vagas para os objetos que está na string.