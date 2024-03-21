from time import *
from random import *
from math import *
def titulo_materia(msg):
    print('\033[1;33m_' * 50)
    print(msg)
    print('\033[1;33m_\033[m')


def matematica():
    #Aqui vai sorteia as questoes
    for c in range(1,5+1):
        sorteio_da_questoes =  5 #randint(1,5)
        sleep(1)
        if sorteio_da_questoes == 1: 
            titulo_materia('ADIÇÃO')
            num1.append(randint(0,100))
            num2.append(randint(0,100))
            resultado = (sum(num1) + sum(num2))
            resposta_matematico = int(input(f'{sum(num1)} + {sum(num2)} = '))
            if resposta_matematico == resultado:
                contador+=1
        elif sorteio_da_questoes == 2:
            titulo_materia('MULTIPLICAÇÃO')
            num1.append(randint(0,100))
            num2.append(randint(0,100))
            resultado = (sum(num1) * sum(num2))            
            resposta_matematico = int(input(f'{sum(num1)} x {sum(num2)} = '))
            if resposta_matematico == resultado:
                contador+=1
        elif sorteio_da_questoes == 3:
            titulo_materia('DIVISÃO')
            num1.append(randint(1,100))
            num2.append(randint(1,100))
            resultado = sum(num1) / sum(num2)
            resposta_matematico = int(input(f'{sum(num1)} ÷ {sum(num2)} = '))
            if resposta_matematico == resultado:
                contador+=1
        elif sorteio_da_questoes == 4:
            titulo_materia('SUBTRAÇÃO')
            num1_sub = randint(0,200)
            num2_sub = randint(0,200)
            resultado = num1_sub - num2_sub
            resposta_matematico = int(input(f'{num1_sub} - {num2_sub} = '))
            if resposta_matematico == resultado:
                contador+=1
        elif sorteio_da_questoes == 5:
            titulo_materia('RAIZ QUADRADA')
            num = randint(0,1000)
            resultado = sqrt(num)
            resposta_matematico = float(input(f'Qual é a raiz quadrada de {num}?: '))
            if resposta_matematico == resultado:
                contador+=1
        print('_' * 50)
        num1.clear()
        num2.clear()


# Programa principal
while True:
    # - A VERIFICAÇÃO DO ALUNO: ONDEM O USUARIO IRA DIGITA AS NOTA E O SCRPIT IRAR AVERIGUAR.
    media = 0
    for notas in range(1,4+1):
        nota = float(input('DIGITE SUA {}ª NOTA: '.format(notas)))
        media+=nota
    # - CONTADOR DE NOTA
    contador = 0
    if media >= 24.1:
        print('\033[1;32mPARABENS VOCÉ ESTA APROVADO\033[m')
        print('MEDIA: {}'.format(media))
    elif media == 24.0:
        print('\033[1;32mVOCE TIROU EXATAMENTE 24.0\033[m')
    # - CASO O ALUNO ESTEJA COM ANO ABAIXO DA MEDIA E FALTANDO MENOS DO QUE 10 PONTOS. VAI DIRETO PARA RECUPERAÇÃO.
    else:
        print('\033[1;31mVOCE ESTA REPROVADO\033[m')
        recupera = (24-media)
        sleep(2)
        if recupera <= 10:
            # - TEXTO DE ORIENTAÇÃO
            print('\033[1;33mOU SEJA VOCE ESTA EM RECUPERAÇÃO')
            print('IREMOS LHE PASSA 5 QUESTOES DE CADA')
            print('MATERIA, CADA UMA DELA VALER 1.0')
            print('VAI CAIR 10 QUESTAO NO TOTAL!!!')
            print('VAMOS COMEÇAR')
            print('Materias: Historia e Matematica')
            # A VARIAVEL: 'perguntar' VAI RECEBER A RESPOSTA DO USUARIO SE ELE QUER MESMO FAZER A RECUPERAÇÃO.
            perguntar = str(input('VOCÉ DESEJA FAZER ESSA RECUPERAÇÃO?[sim[S] ou não[N]?]:\033[m ')).strip()[0]
            sleep(2)
            if perguntar in 'Ss':
                print('\033[1;36m▃\033[m'*50)
                print('\033[1;32mCARREGANDO AS PERGUNTAS...\033[m')
                print('\033[1;36m▃\033[m'*50)
                sleep(1)
                print('\033[1;33mQual evento histórico marcou o início da Primeira Guerra Mundial e em que ano ocorreu?')
                sleep(0.5)
                print('(A) Bombardeio de Pearl Harbor (1941)')
                sleep(0.4)
                print('(B) Assassinato do Arquiduque Francisco Ferdinando (1914)')
                sleep(0.3)
                print('(C) Invasão da Polônia pela Alemanha (1939)')
                sleep(0.3)
                print('(D) Tratado de Versalhes (1919)\033[m')
                sleep(0.2)
                # - UM PEQUENO SISTEMA PARA GARANTIR PARA O USUARIO NÃO DIGITAR ERRADO
                while True:
                    resposta1 = str(input('RESPOSTA: ')).strip()[0]
                    if resposta1 in 'ABCDabcd':
                        break
                # - SE A RESPOSTA FOR CORRETA MAIS UM PONTO.
                if resposta1 in 'Bb':
                    contador+= 1
                print('\033[1;36m▃\033[m'*50)
                sleep(1)
                print('\033[1;33mQuem foi o líder da Revolução Cubana em 1959 e como isso impactou a história de Cuba?')
                sleep(0.5)
                print('(A) Che Guevara - Industrialização acelerada')
                sleep(0.4)
                print('(B) Fulgencio Batista - Independência')
                sleep(0.3)
                print('(C) Fidel Castro - Estabelecimento do regime socialista')
                sleep(0.2)
                print('(D) Carlos Prio Socarras - Democratização')
                sleep(0.2)
                while True:
                    resposta2 = str(input('RESPOSTA: ')).strip()[0]
                    if resposta2 in 'ABCDabcd':
                        break
                if resposta2 in 'Cc':
                    contador+= 1
                print('\033[1;36m▃\033[m'*50)
                sleep(1)
                print('\033[1;33mExplique o significado e as consequências do Tratado de Versalhes, assinado após o fim')
                sleep(0.5)
                print('da Primeira Guerra Mundial.')
                sleep(0.5)
                print('(A) Imposição de sanções à Alemanha e territorialmente redefinido o mapa europeu.')
                sleep(0.4)
                print('(B) Aliança entre Alemanha e Rússia.')
                sleep(0.3)
                print('(C) Fundação da Liga das Nações.')
                sleep(0.2)
                print('(D) Acordo para dividir a África entre as potências europeias.') 
                sleep(0.3)
                while True:
                    resposta3 = str(input('RESPOSTA:\033[m ')).strip()[0]
                    if resposta3 in 'ABCDabcd':
                        break
                if resposta3 in 'Aa':
                    contador+= 1
                print('\033[1;36m▃\033[m'*50)
                sleep(1)
                print('\033[1;33mQual foi o papel do Movimento dos Direitos Civis nos Estados Unidos durante a década de 1960?')
                sleep(0.5)
                print('(A) Promoção da segregação racial')
                sleep(0.5)
                print('(B) Defesa dos direitos civis para afro-americanos')
                sleep(0.3)
                print('(C) Apoio à discriminação racial')
                sleep(0.3)
                print('(D) Combate à igualdade de gênero')
                sleep(0.2)
                while True:
                    resposta4 = str(input('RESPOSTA:\033[m ')).upper().strip()[0]
                    if resposta4 in 'ABCDabcd':
                        break
                if resposta4 in 'Bb':
                    contador+= 1
                print('\033[1;36m▃\033[m'*50)
                sleep(1)
                print('\033[1;33mDescreva o que foi o Renascimento, destacando suas principais')
                sleep(0.5)
                print('a) Período de obscurantismo cultural e científico.')
                sleep(0.5)
                print('b) Revivalismo artístico, científico e cultural, estimulando o individualismo.')
                sleep(0.4)
                print('c) Era de expansão territorial e militar na Europa.')
                sleep(0.3)
                print('d) Dominância da filosofia escolástica e teocêntrica.')
                sleep(0.2)
                while True:
                    resposta5 = str(input('RESPOSTA:\033[m ')).upper().strip()[0]
                    if resposta5 in 'ABCDabcd':
                        break
                print('\033[1;36m▃\033[m'*50)
                if resposta5 in 'Bb':
                    contador+= 1
                num1 = []
                num2  = []
                sleep(3)
                print('\033[1;33mMatematica:')
                sleep(2)
                # - O SISTEMA DE PERGUNTA DE MATEMATICA BASICA.
                # - DIFERENTE DAS PERGUNTAS ANTERIORES, ESSA SÃO VARIAVEIS
                # - PARA MAIS DETALHES VA ATE LA EM CIMA PARA AVERIGUAR
                sleep(3)
                print('\033[1;34m*SISTEMA AVERIGUANDO AS RESPOSTA...\033[m')
                sleep(4)
                resultado = (media+contador)
                if resultado >= 24:
                    print('\033[1;32mPARABENS VOCE FOI APROVADO!!!\033[m')
                    print('\033[1;36m▃\033[m'*50)
                else:
                    print('\033[1;31mREPROVADO!!!\033[m')
                    print('\033[1;36m▃\033[m'*50)
            else:
                print('OK, \033[1;32mREPROVADO\033[m')
                print('\033[1;36m▃\033[m'*50)
    repetir = str(input('SE DESEJA REPETIR ESSE PROCESSO TODO DIGITE "S" CASO ALCONTRARIO "N"')).strip()[0]
    if repetir in 'Nn':
        break
    print('\033[1;36m▃\033[m'*50)
    media-=media
