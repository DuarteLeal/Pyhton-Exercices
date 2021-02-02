larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area = larg * alt
tinta = area / 2
print('A tua parede tem uma dimensão de {} x {} e a tua área é de {:.3} m^2.\n'
      'Para pintar a parede de tinta é preciso {}L de tinta.'
      .format(larg, alt, area, tinta))
