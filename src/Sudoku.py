# -*- coding: utf-8 -*-
cont= 0
espaco = 0
jorge = [
             ['5','3',' ','7',' ',' ',' ',' ',' '],
             ['6',' ',' ','1','9','5',' ',' ',' '],
             [' ','9','8',' ',' ',' ',' ','6',' '],
             ['8',' ',' ',' ','6',' ',' ',' ','3'],
             ['4',' ',' ','8',' ','3',' ',' ','1'],
             ['7',' ',' ',' ','2',' ',' ',' ','6'],
             [' ','6',' ',' ',' ',' ','2','8',' '],
             [' ',' ',' ','4','1','9',' ',' ','5'],
             [' ',' ',' ',' ','8',' ',' ','7','9']
    ]

def hojesim():
    for j in range(9):
        for i in range(9):
            cont = 0
            for c in range(9):
                if jorge[j][i] == jorge[j][c]: 
                    cont += 1
            if cont != 1 :
                return 'perdeu'
    return 'ganhou'
    # TODO: verificar em colunas

def completo():
    for i in range(9):
        if jorge[i].count(' ') == 0:
            espaco += 1
        if espaco == 9:
            return True
        return False
            

def tab():
        
    print('''+-----------------------+
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
|-------+-------+-------|
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
|-------+-------+-------|
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
| {} {} {} | {} {} {} | {} {} {} |
+-----------------------+'''.format(jorge[0][0],jorge[0][1],jorge[0][2],jorge[0][3],jorge[0][4],jorge[0][5],jorge[0][6],jorge[0][7],jorge[0][8],
                                    jorge[1][0],jorge[1][1],jorge[1][2],jorge[1][3],jorge[1][4],jorge[1][5],jorge[1][6],jorge[1][7],jorge[1][8],
                                    jorge[2][0],jorge[2][1],jorge[2][2],jorge[2][3],jorge[2][4],jorge[2][5],jorge[2][6],jorge[2][7],jorge[2][8],
                                    jorge[3][0],jorge[3][1],jorge[3][2],jorge[3][3],jorge[3][4],jorge[3][5],jorge[3][6],jorge[3][7],jorge[3][8],
                                    jorge[4][0],jorge[4][1],jorge[4][2],jorge[4][3],jorge[4][4],jorge[4][5],jorge[4][6],jorge[4][7],jorge[4][8],
                                    jorge[5][0],jorge[5][1],jorge[5][2],jorge[5][3],jorge[5][4],jorge[5][5],jorge[5][6],jorge[5][7],jorge[5][8],
                                    jorge[6][0],jorge[6][1],jorge[6][2],jorge[6][3],jorge[6][4],jorge[6][5],jorge[6][6],jorge[6][7],jorge[6][8],
                                    jorge[7][0],jorge[7][1],jorge[7][2],jorge[7][3],jorge[7][4],jorge[7][5],jorge[7][6],jorge[7][7],jorge[7][8],
                                    jorge[8][0],jorge[8][1],jorge[8][2],jorge[8][3],jorge[8][4],jorge[8][5],jorge[8][6],jorge[8][7],jorge[8][8]))

jogo = 1
                                    

while jogo == 1:
    tab()
    coluna = int(input('Digite a coluna em que você quer jogar: '))
    fila = int(input('Digite a fila em que você quer jogar: '))
    num = str(input('Digite o número que você quer jogar nesse lugar: '))

    jorge[fila-1][coluna-1] = num
    
    if completo():
        jogo = 0

    
    
      
    
print(hojesim())
        


    
    
