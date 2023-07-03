S = float(input('Qual é o salário dofuncionário: R$ '))
print('''Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'''
      .format(S, S + (S*15/100)))

