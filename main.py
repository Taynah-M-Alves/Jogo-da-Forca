# Será a variavel responsável por armazenar a palavra que será usada na forca
palavra = "vida"
#Transforma cada letra da palavra em um elemento da lista
letras_palavra= list(palavra)
#Armazena a linha onde mostrará o jogo da forca
linha = list("_"*len(palavra))
#Variavel responsável por verificar quantos erros já foram cometidos pelo usuário
erros = 0 

forca=['''
    ______
    |    |
    |    
    |   
    |      
    |
'''
,'''
    ______
    |    |
    |   
    |   
    |     
    |
'''
,'''
    ______
    |    |
    |    0
    |    |
    |     
    |
'''
,'''
    ______
    |    |
    |    0
    |   /|
    |      
    |
'''
,'''
    ______
    |    |
    |    0
    |   /|\\
    |      
    |
'''
,'''
    ______
    |    |
    |    0
    |   /|\\
    |   /    
    |
'''
,'''
    ______
    |    |
    |    0
    |   /|\\
    |   / \\   
    |
''']

def letra_encontrada():
     print(f"A letra {tentativa} foi encontrada na palavra!")

def letra_errada():
     print(f"A letra {tentativa} não foi encontrada na palavra!")

def jogo_finalizado():
     print("--------------- Parabens jogo finalizado com sucesso!---------------")
     

while "_" in linha and erros <= 6:
    encontrou= False
    tentativa = input(str("Digite a letra que deseja tentar:"))

# Verifica se a letra está na palavra e caso esteja mostra em qual posição
    for indice, letra in enumerate(palavra):
            if letra == tentativa:
                linha[indice] = letra
                encontrou= True


    if encontrou == True:
         letra_encontrada()

    elif encontrou == False: 
         letra_errada()
         erros+= 1
         if erros == 0:
              print(forca[0])
         if erros == 1:
              print(forca[1])
         if erros == 2:
              print(forca[2])
         if erros == 3:
              print(forca[3])
         if erros == 4:
              print(forca[4])
         if erros == 5:
              print(forca[5])
         if erros==6:
              print(forca[6])
       

    print(" ".join(linha))
    print(f"erros: {erros}")

jogo_finalizado()