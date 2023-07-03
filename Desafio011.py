L = float(input("Largura da parede: "))
A = float(input('Altura da parede: '))
Li = L*A
LiM = Li/2
print('''Sua parede vai ter a dimensão de {}x{} e sua área é de {}m².
Para pintar essa parede, você precisará de {}l de tinta.'''.format(L, A, Li, LiM))