#conversor de saldo na carteira para dolar e euro

carteira = float(input('Quantos dinheiro você tem na carteira? R$'))
dolar = carteira / 5.13
euro = carteira / 5.88

print('Com R$ {:.2f} você pode comprar US${:.2f} ou {:.2f}€'.format(carteira, dolar, euro))