# Faça um programa que leia algo pelo teclado e mostre ja tela o seu tipo primitivo  e  todas as informaçoes possiveis sobre ele.

n = input('Digite algo: ')

print('O tipo primetivo desse valor é: ', type(n))
print('Só tem espaços: ',n.isspace())
print('um numero inteiro: ',n.isnumeric())
print('é um numero decimal: ',n.isdecimal())
print('é alfabrtico: ',n.isalpha())
print('é alfanumerico: ',n.isalnum()) 
print('esta em maisculo: ',n.isupper())
print('esta em minuscula: ' ,n.islower())
print('esta capitalizada: ',n.istitle())
print('é um digito: ',n.isdigit())