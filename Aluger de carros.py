d = int(input('Quantos dias o carro foi usado? '))
km = float(input('Quantos km o carro percorreu? '))
ppd = d * 60
ppkm = km * 0.15
pf = d + km
print('O preço final a pagar é de {:.2f} euros.'.format(pf))