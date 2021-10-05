import random
import string

def adivinha_senha(chars=string.ascii_lowercase + string.digits):
    i = ''.join(random.choice(chars))
    return i

def get_adivinha(senha):
    i = 0
    index = len(senha)-1
    tentativas = 0

    while(i <= index):
        adivinha_senha()
        tentativas+=1

        if(adivinha_senha() == senha[i]):
            i += 1

    print(f'Sua senha é {senha_usuario}.')
    print(f'Foram necessárias {tentativas} tentativas para o computador descobrir a senha')

senha_usuario = input('Insira sua senha: ')

get_adivinha(senha_usuario.lower())