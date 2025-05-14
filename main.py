# Será a variavel responsável por armazenar a palavra que será usada na forca
palavra = "viver"
#Transforma cada letra da palavra em um elemento da lista
letras_palavra= list(palavra)
#Armazena a linha onde mostrará o jogo da forca
linha = list("_"*len(palavra))
#Variavel responsável por verificar quantos erros já foram cometidos pelo usuário
erros = 0 
tentativas= []

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
    |    0
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
     tentativas.append(tentativa)

def letra_errada():
     print(f"A letra {tentativa} não foi encontrada na palavra!")
     tentativas.append(tentativa)
     

def jogo_finalizado():
     print("--------------- Parabens jogo finalizado com sucesso!---------------")
     

while "_" in linha and erros <= 6:
    encontrou= False
    tentativa = input(str("Digite a letra que deseja tentar:"))

     #utilizado para garantir que foi digitado apenas um caractere e que o caractere é uma letra
    if tentativa.isalpha()== True and len(tentativa)< 1:
         print("Digite apenas uma letra.")

     #usado para avisar ao usuário que ele já tentou essa letra antes
    if tentativa in tentativas:
         print("letra já digitada! Tente novemente.")

     #garante que só executara o jogo quando a letra ñ for repetida e for apenas um caractere
    if tentativa not in tentativas and tentativa.isalpha() and len(tentativa) == 1:
      
          #Intera a lista verificando se a letra está presente na palavra(que é a lista)
          for indice, letra in enumerate(palavra):
                    # Verifica se a letra está na palavra e caso esteja atribui essa letra a sua respectiva posição
                    if letra == tentativa and len(letra)==1 and letra != tentativas:
                         linha[indice] = letra
                         encontrou= True
                         print(forca[erros])



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
          print(f"erros: {erros}/6")

jogo_finalizado()

jogo_finalizado()