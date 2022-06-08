import os  
import random

jogarNovamente = "s" 
jogadas = 0
quemJoga = 2  #1 = CPU e 2 - JOG
maxjogadas = 9
vit = "n"
velha = [
    [' ', ' ',' '],     #L0C0 L0C1 L0C2
    [' ', ' ',' '],     #L1C0 L1C1 L1C2 
    [' ', ' ',' ']      #L2C0 L2C1 L2C2
]

def tela():
    global velha
    global jogadas
    os.system('cls')   # linha para limpar o jogo quando reniciado
    print('    0   1   2')  # formato da grade do jogo.
    print('0:  ' + velha[0][0] + ' | ' + velha[0][1] + ' | ' + velha[0][2])
    print('   -----------')
    print('1:  ' + velha[1][0] + ' | ' + velha[1][1] + ' | ' + velha[1][2])
    print('   -----------')
    print('2:  ' + velha[2][0] + ' | ' + velha[2][1] + ' | ' + velha[2][2])

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxjogadas
    if quemJoga == 2 and jogadas < maxjogadas:
       
        
        try:
             l = int(input('Linha..: '))
             c = int(input('Coluna...: '))
             while velha [l][c] != ' ':
                l = int(input('Linha..: '))
                c = int(input('Coluna...: '))
            
             velha[l][c] = 'X'
             quemJoga = 1
             jogadas += 1
        except:
            print('Jogada inválida.')
            os.system('pause')

def cpuJoga():
    global jogadas
    global quemJoga
    global maxjogadas
    if quemJoga == 1 and jogadas < maxjogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while velha [l][c] != ' ':
            l = random.randrange(0,3)
            c = random.randrange(0,3)
        velha[l][c] = 'O'
        jogadas +=1
        quemJoga = 2


def verificarVitoria():
    global velha
    vitoria = 'n'
    simbolos = ['X', 'O']
    for s in simbolos:
        vitoria = 'n'
        #Verificar linhas
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if(velha[il][ic] == s):
                    soma +=1
                ic +=1
            il +=1
            if(soma == 3):
                vitoria = s
                break
        if(vitoria != 'n'):
            break
        #Verficar Colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if(velha[il][ic] == s):
                    soma +=1
                il +=1
            if(soma == 3):
                vitoria = s
                break
            ic +=1
        if(vitoria != 'n'):
            break
        #Verfica Diagonal 1

        soma = 0
        idiag = 0
        while idiag < 3:
            if(velha[idiag][idiag] == s):
                soma +=1
            idiag +=1
        if(soma == 3):
            vitoria = s
            break
        #Verfica Diagonal 2

        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if(velha[idiagl][idiagc] == s):
                soma +=1
            idiagl +=1
            idiagc -=1
        if(soma == 3):
            vitoria = s
            break
    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxjogadas
    global vit
    jogadas = 0
    quemJoga = 2  #1 = CPU e 2 - JOG
    maxjogadas = 9
    vit = "n"
    velha = [
        [' ', ' ',' '],     #L0C0 L0C1 L0C2
        [' ', ' ',' '],     #L1C0 L1C1 L1C2 
        [' ', ' ',' ']      #L2C0 L2C1 L2C2
    ]


while(jogarNovamente == 's'):
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit = verificarVitoria()
        if(vit != 'n') or (jogadas >= maxjogadas):
            break


    print('Fim de Jogo')
    if(vit == ' X ' or vit == ' O '):
        print('Resultado: Jogador'  +vit+  'Venceu.')
    else:
        print('Resultado: Empate.')

    jogarNovamente = input('Jogar Novamente? [s/n]: ')
    redefinir()

    

    


