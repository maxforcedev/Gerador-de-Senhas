"""
Gerador de Senhas - MaxForce.dev

Descrição:
Este programa gera senhas com base nas preferências do usuário, permitindo a criação de senhas fortes e fáceis de lembrar.

Instruções de Uso:
1. Execute o programa e escolha a opção desejada no menu.
2. Siga as instruções do programa para configurar a geração de senhas.
3. O programa fornecerá senhas conforme as opções escolhidas.

Opções Disponíveis:
[ 1 ] - TODOS OS CARACTERES: Gere senhas contendo letras maiúsculas, letras minúsculas, números e símbolos.
[ 2 ] - FACIL DE LER: Gere senhas que são fáceis de ler e digitar, excluindo caracteres confusos (I, l, O, 0, o).
[ 3 ] - FACIL DE PRONUNCIAR: Crie senhas que são fáceis de pronunciar, usando letras maiúsculas ou minúsculas.

Exemplos:
- Para gerar senhas que incluem letras maiúsculas, minúsculas e números, escolha "1" no menu.
- Para gerar senhas fáceis de ler, escolha "2" e siga as instruções.
- Para criar senhas fáceis de pronunciar com letras maiúsculas e minúsculas, selecione "3".

Requisitos:
- Python 3.x
- Nenhuma biblioteca externa necessária.

Créditos:
- Este programa foi desenvolvido por Luis Felipe Cavalini Vieira Silva como um projeto de código aberto.

Histórico de Versões:
- v1.0 (05/11/2023): Versão inicial do programa.
"""

import os
import string
import random


def verificar_opcao(opcao, tamanho, qntd_senhas, menu):
    opcoes_validas = ['1', '2', '3', '4']
    opcoes = opcao.split(',')
    opcoes_presentes = []
    opcoes_presentes_texto = []

    for o in opcoes:
        if o in opcoes_validas:
            opcoes_presentes.append(o)

    for i in opcoes_presentes:
        if i == '1':
            opcoes_presentes_texto.append('LETRA MAIÚSCULA')
        if i == '2':
            opcoes_presentes_texto.append('LETRA MINÚSCULA')
        if i == '3':
            opcoes_presentes_texto.append('NUMEROS')
        if i == '4':
            opcoes_presentes_texto.append('SIMBOLOS')

    print('OPÇÕES DETECTADAS DA SUA SENHA: "{}"'.format(', '.join(opcoes_presentes_texto)))

    if qntd_senhas == 1:
        senha = ''
        if '1' in opcoes_presentes:
            if menu == 2:
                senha += ''.join(random.SystemRandom().choice(string.ascii_uppercase.replace('I', 'X').replace('O', 'Y'))for _ in range(tamanho//len(opcoes_presentes)))
            else:
                senha += ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(tamanho//len(opcoes_presentes)))
            adicional = random.SystemRandom().choice(string.ascii_uppercase.replace('I', 'X').replace('O', 'Y'))
        if '2' in opcoes_presentes:
            if menu == 2:
                senha += ''.join(random.SystemRandom().choice(string.ascii_lowercase.replace('i', 'k').replace('o', 'l')) for _ in range(tamanho//len(opcoes_presentes)))
            else:
                senha += ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(tamanho//len(opcoes_presentes)))
            adicional = random.SystemRandom().choice(string.ascii_lowercase.replace('i', 'k').replace('o', 'l'))
        if '3' in opcoes_presentes:
            if menu == 2:
                senha += ''.join(random.SystemRandom().choice(string.digits.replace('1', '3').replace('0', '6')) for _ in range(tamanho//len(opcoes_presentes)))
            else:
                senha += ''.join(random.SystemRandom().choice(string.digits) for _ in range(tamanho//len(opcoes_presentes)))
            adicional = random.SystemRandom().choice(string.digits.replace('1', '3').replace('0', '6'))
        if '4' in opcoes_presentes:
            senha += ''.join(random.SystemRandom().choice('!@#$%^*_+=') for _ in range(tamanho//len(opcoes_presentes)))
        if len(senha) < tamanho:
            senha = senha + adicional

        print('Senha : ' + senha)

    else:
        with open('gerador_de_senhas.txt', mode='a', newline='', encoding='utf-8') as file:
            senhas_geradas = set()
            senha_numero = 1
            while len(senhas_geradas) < qntd_senhas:
                senha = ''
                if '1' in opcoes_presentes:
                    if menu == 2:
                        senha += ''.join(random.SystemRandom().choice(string.ascii_uppercase.replace('I', 'X').replace('O', 'Y')) for _ in range(tamanho//len(opcoes_presentes)))
                    else:
                        senha += ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(tamanho//len(opcoes_presentes)))
                    adicional = random.SystemRandom().choice(string.ascii_uppercase.replace('I', 'X').replace('O', 'Y'))
                if '2' in opcoes_presentes:
                    if menu == 2:
                        senha += ''.join(random.SystemRandom().choice(string.ascii_lowercase.replace('i', 'k').replace('o', 'l')) for _ in range(tamanho//len(opcoes_presentes)))
                    else:
                        senha += ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(tamanho//len(opcoes_presentes)))
                    adicional = random.SystemRandom().choice(string.ascii_lowercase.replace('i', 'k').replace('o', 'l'))
                if '3' in opcoes_presentes:
                    if menu == 2:
                        senha += ''.join(random.SystemRandom().choice(string.digits.replace('1', '3').replace('0', '6')) for _ in range(tamanho//len(opcoes_presentes)))
                    else:
                        senha += ''.join(random.SystemRandom().choice(string.digits) for _ in range(tamanho//len(opcoes_presentes)))
                    adicional = random.SystemRandom().choice(string.digits.replace('1', '3').replace('0', '6'))
                if '4' in opcoes_presentes:
                    senha += ''.join(random.SystemRandom().choice('!@#$%^*_+=') for _ in range(tamanho//len(opcoes_presentes)))

                if len(senha) < tamanho:
                    senha = senha + adicional
                if senha not in senhas_geradas:
                    file.write(f'Senha {senha_numero}: ' + senha + '\n')
                    senhas_geradas.add(senha)
                    senha_numero += 1

            print(f'{qntd_senhas} senhas foram geradas no arquivo "gerador_de_senhas.txt".')


def facil_de_pronunciar(opcao, tamanho, qntd_senhas):
    if qntd_senhas > 1:
        with open('senha_facil_de_pronunciar.txt', mode='a', newline='', encoding='utf-8') as file:
            senhas_geradas = set()
            senha_numero = 1
            while len(senhas_geradas) < qntd_senhas:
                if opcao == '1':
                    senha = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(tamanho))
                elif opcao == '2':
                    senha = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(tamanho))
                elif opcao == '3':
                    senha = ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(tamanho))
                if senha not in senhas_geradas:
                    file.write(f'Senha {senha_numero}: ' + senha + '\n')
                    senhas_geradas.add(senha)
                    senha_numero += 1

            print(f'{qntd_senhas} senhas foram geradas no arquivo "senha_facil_de_pronunciar.txt".')
    else:
        if opcao == '1':
            senha = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(tamanho))
        elif opcao == '2':
            senha = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(tamanho))
        elif opcao == '3':
            senha = ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(tamanho))

        print('Senha : ' + senha)


def main():
    while True:
        menu = f'''{'-' * 50}\n\tGerador de senhas - MaxForceDev\n{'-' * 50}\n[ 1 ] - TODOS OS CARACTERES\n[ 2 ] - FACIL DE LER\n[ 3 ] - FACIL DE PRONUNCIAR\n==> '''

        escolha = input(menu)

        if escolha == '1' or escolha == '2':

            os.system('cls')
            print('Escolha a opção para senhas fáceis de ler:\n[ 1 ] - INCLUIR LETRA MAIÚSCULA\n[ 2 ] - INCLUIR LETRA MINÚSCULA\n[ 3 ] - INCLUIR NUMEROS\n[ 4 ] - INCLUIR SIMBOLOS')
            opcao = input('Voce deve colocar as opções na mesma linha e separados por virgula. EX: "1, 2, 3, 4"\n==> ')
            tamanho = input('Digite o número de caracteres que deseja em sua senha: ')
            qntd_senhas = input('Digite a quantidade de senhas que deseja gerar: ')
            if len(opcao.split()) == 0 or len(qntd_senhas.split()) == 0 or len(tamanho.split()) == 0:
                print('Opção inválida. Não deixe nenhuma resposta em branco.')
            else:
                try:
                    tamanho = int(tamanho)
                    qntd_senhas = int(qntd_senhas)
                    if qntd_senhas <= 0:
                        os.system('cls')
                        print('Quantidade de senhas deve ser positiva.')
                    
                    else:
                        if escolha == '1':
                            verificar_opcao(opcao, tamanho, qntd_senhas, menu=1)
                        elif escolha == '2':
                            verificar_opcao(opcao, tamanho, qntd_senhas, menu=2)
                except ValueError:
                    print('OPS! Ocorreu um erro.')

        elif escolha == '3':
            os.system('cls')
            opcao = input('Escolha a opção para senhas fáceis de pronunciar:\n[ 1 ] - SOMENTE LETRA MAIÚSCULA\n[ 2 ] - SOMENTE LETRA MINÚSCULA\n[ 3 ] - LETRA MAIÚSCULA E MINÚSCULA\n==> ')
            if opcao in ('1', '2', '3'):
                tamanho = input('Digite o número de caracteres que deseja em sua senha: ')
                qntd_senhas = input('Digite a quantidade de senhas que deseja gerar: ')
                if len(opcao.split()) == 0 or len(qntd_senhas.split()) == 0 or len(tamanho.split()) == 0:
                    print('Opção inválida. Não deixe nenhuma resposta em branco.')
                else:
                    try:
                        tamanho = int(input('Digite o número de caracteres que deseja em sua senha: '))
                        qntd_senhas = int(input('Digite a quantidade de senhas que deseja gerar: '))
                        if qntd_senhas > 0:
                            facil_de_pronunciar(opcao, tamanho, qntd_senhas)
                        else:
                            os.system('cls')
                            print('Quantidade de senhas deve ser positiva.')
                    except ValueError:
                        print('OPS! Ocorreu um erro.')
            else:
                os.system('cls')
                print('Opção inválida. Por favor, escolha uma opção válida.')
        else:
            os.system('cls')
            print('Opção inválida. Por favor, escolha uma opção válida.')


if __name__ == '__main__':
    main()
