#DESAFIO 05 FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR. 

n1 = int(input('Digite um numero: '))
suc = n1 - 1
ant = n1 + 1 

print('Seu numero é {}! , Seu sucessor é {}! , Seu antecessor é {}! '.format(n1, suc, ant))