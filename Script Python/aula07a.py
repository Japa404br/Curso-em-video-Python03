#nome = str(input('Qual é seu nome?'))
#print('Prazer em te conjecer{:=^20}!'.format(nome)) // Centralizado em 20

#print('Prazer em te conhecer {:<20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ') # {:.3f} = estou pedido para colocar somente 3 casa decimais flutuante e end= e para não quebrar a linha
print('Divisão inteira {}, \n e potência {}'.format(di, e)) # \n = para quebrar a linha S