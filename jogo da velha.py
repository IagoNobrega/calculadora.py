# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|", end="")
        for elemento in linha:
            print(elemento, end="|")
        print()

# Função para verificar se alguém venceu
def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == jogador and tabuleiro[1][coluna] == jogador and tabuleiro[2][coluna] == jogador:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False

# Criar tabuleiro vazio
tabuleiro = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

# Variável para controlar o jogador atual
jogador_atual = "X"

# Loop principal do jogo
while True:
    # Imprimir tabuleiro
    imprimir_tabuleiro(tabuleiro)

    # Obter a jogada do jogador atual
    linha = int(input("Digite o número da linha (0-2): "))
    coluna = int(input("Digite o número da coluna (0-2): "))

    # Verificar se a posição está vazia
    if tabuleiro[linha][coluna] == " ":
        # Fazer a jogada
        tabuleiro[linha][coluna] = jogador_atual

        # Verificar se o jogador atual venceu
        if verificar_vencedor(tabuleiro, jogador_atual):
            print(f"Jogador {jogador_atual} venceu!")
            break

        # Verificar se houve empate
        if all(all(elemento != " " for elemento in linha) for linha in tabuleiro):
            print("O jogo terminou em empate!")
            break

        # Trocar o jogador atual
        jogador_atual = "O" if jogador_atual == "X" else "X"
    else:
        print("Posição inválida. Tente novamente.")