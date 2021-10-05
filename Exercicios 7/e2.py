from random import sample
import random

def embaralha(nome):
    a = sample(nome,len(nome))
    d = ''.join(a)
    return d.lower()

times = open('times.txt', 'r')
lista = []

for time in times:
    lista.append(time)

index = random.randint(0, len(lista)-1)
t = lista[index]
vdd = str(t).removesuffix('\n')
anagrama = embaralha(vdd)

rodadas = 5

print('Bem vindo ao Adivinhe Qual O Time!')
print('Aqui você deve adivinhar de qual time do Brasileiro Série A é o anagrama.')
print('Vamos ao jogo!')

while rodadas > 0:
    print(f'Tentativas restantes: {rodadas}')
    print(anagrama)
    r = input('Qual a resposta? ')

    if(r.lower() == vdd.lower()):
        print('Você acertou!')
        break
    else:
        rodadas-=1

print(f'A resposta era {vdd}!')
print('Fim de jogo! Obrigado por jogar!')