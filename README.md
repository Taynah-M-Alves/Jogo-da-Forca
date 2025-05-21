# 🕹️ Jogo da Forca em Python
## 📋 Sumário
- Descrição
- Requisitos
- Funcionalidades
- Como Jogar
  -  Estrutura do Código
  -  Categorias e Palavras
  -  Modo de Jogo
  -  Funções Principais
  -  Loop Principal
- Melhorias Futuras

## 📖 Descrição
Este projeto é uma implementação simples do clássico *jogo da forca* em Python. O usuário pode escolher entre dois modos de jogo:
1. Digitar a palavra manualmente.
2. Escolher uma categoria para o sistema selecionar uma palavra aleatória.

O jogo termina quando o jogador acerta a palavra ou comete 6 erros.

## ⚙️ Requisitos
- Python 3.x
- Terminal ou prompt de comando

## 🎯 Funcionalidades
- Modo de jogo personalizável (manual ou por categoria)
- Sistema de categorias (animais, frutas e cores)
- Validação de entradas do usuário
- Histórico de tentativas para evitar repetições
- Exibição gráfica da forca (ASCII art)
- Mensagens de sucesso e erro interativas

## 🕹️ Como Jogar
1. Escolha o modo de jogo:
  - Digitar uma palavra
  - Selecionar uma categoria
2. Tente adivinhar a palavra, letra por letra.
3. Você tem até 6 erros antes que a forca seja completada.
4. O jogo termina com uma mensagem de vitória ou derrota.

## 🧱 Estrutura do Código
### 📂 Categorias e Palavras
```
python

list_categorias = {
    "animais": ["elefante", "gato", "cachorro", "leão", "tigre"],
    "frutas": ["maçã", "banana", "laranja", "uva", "melancia"],
    "cores": ["azul", "vermelho", "verde", "amarelo", "roxo"]
}
```
- Armazena categorias e listas de palavras.
- Usado no modo de jogo automático.

### 🧩 Modo de Jogo
O usuário pode escolher:

- Modo 1: Digita a palavra a ser adivinhada.

- Modo 2: Escolhe uma categoria e o sistema sorteia uma palavra automaticamente.

```python

def escolher_modo()
def escolher_categoria()
def executar_modo_jogo()
```

### ⚙️ Funções Principais
✅ ```letra_encontrada()```
<br>Adiciona a letra ao histórico e informa que ela está na palavra.

❌ ```letra_errada()```
<br>Adiciona a letra ao histórico, informa o erro e aumenta o número de erros.

🏁 ```jogo_finalizado()```
<br>Mostra uma mensagem de encerramento do jogo.

### 🔁 Loop Principal
```
python

while "_" in linha and erros < 6:
    tentativa = input(...)
```

- Recebe uma letra do usuário.
- Verifica se é válida (uma única letra não repetida).
- Atualiza a palavra e o estado do jogo com base no acerto/erro.
- Finaliza o jogo após acertos completos ou 6 erros.

## 📌 Validações Incluídas
- Apenas uma letra por tentativa
- Apenas letras (sem números ou símbolos)
- Ignora letras já tentadas
- Case-insensitive (```.lower()```)

## 🚀 Melhorias Futuras
- Implementar interface gráfica (usando Tkinter ou Pygame)
- Adicionar sistema de pontuação
- Permitir jogar novamente ao final
- Mostrar letras já tentadas no jogo
- Melhorar tratamento de acentos

## 💻 Executando o Projeto

1. Instale o Python 3 em seu computador, se ainda não tiver.
2. Clone este repositório ou copie o arquivo `.py` para sua máquina.
3. No terminal, execute:

``` python nome_do_arquivo.py ```
