from datetime import datetime

atual = datetime.now().year
maiores = 0
menores = 0

for c in range(1,8):
    nasc = int(input('Em Que Ano Você Nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('{} pessoa(s) é(são) de maior(es)'.format(maiores))
print('{} pessoa(s) é(são) de menor(es)'.format(menores))
    