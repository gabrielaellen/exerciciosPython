import names
from random import randint

jogadores = []

while True:
    nomeJogador = names.get_full_name()
    partidasJogadas = randint(1,5)
    jogador = { 'nome': nomeJogador,
                'partidas': partidasJogadas,
            }
    listaDeGols = []
    for i in range(0,partidasJogadas):
        golsMarcados = randint(0,4)
        listaDeGols.append(golsMarcados)
        somaDeGols = sum(listaDeGols)
    
    jogador['golsMarcados'] = listaDeGols
    jogador['somaDeGols'] = somaDeGols
    
    
    jogadores.append(jogador)

    continuar = input('Deseja continuar: [S/N] ')
    if continuar in 'Nn':
        break

print(jogadores)
print('-='*15)
print(f"{'cod':^2} {'nome':<20} {'gols':<10} {'total':^3}")
contador = 0
for c in jogadores:
    lista = c["golsMarcados"]
    lista.__format__
    print(f'{contador:^2} {c["nome"]:<20} {lista:<10} {c["somaDeGols"]:^3}')
    contador+=1