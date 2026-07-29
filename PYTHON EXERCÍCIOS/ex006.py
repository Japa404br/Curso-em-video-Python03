#DESAFIO 006 - CRIE UM ALGORITMO QUE LEIA UM NUMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA. 

n1 = int(input('Digite um numero: '))
dob = n1*2
tri = n1*3
raiz = n1**(1/2)

print('Seu numero é: {}, O dobro é {}, o triplo dele é {}, e a raiz quadrada é {:.2f}'.format(n1, dob, tri, raiz))