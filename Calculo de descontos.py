price = float(input('Qual é o preço do produto em euros?'))
new_price = price - (price * 5 / 100)
print('O produto que custava {:.2f} euros, agora com a promoção custa {:.2f} euros'.format(price, new_price))
