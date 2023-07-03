D = float(input('Uma distância em metros: '))
print('''A medida de {}m corresponde a:
{} km - quilômetro
{} hm - hectometros
{} dam - decametros
{:.0f} dm - decímetros
{:.0f} cm - centímetros
{:.0f} mm - milímetros'''.format(D, D/1000, D/100, D/10, D*10, D*100, D*1000))
