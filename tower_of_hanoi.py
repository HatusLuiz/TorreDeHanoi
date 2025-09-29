import turtle
import time
import random

CORES_DISCOS = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFBE0B', '#FB5607', '#8338EC', '#3A86FF', '#38B000']
COR_HASTES = '#2F2F2F'
COR_BASE = '#E9ECEF'
COR_TEXTO = '#212529'
VELOCIDADE_ANIMACAO = 0.2
MAX_DISCOS = 8

screen = turtle.Screen()
screen.setup(1000, 800)
screen.title("Torre de Hanói - Hatus Luiz e Luiz Fernando")
screen.bgcolor('#2C3E50')

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

posicoes_hastes = {'A': -350, 'B': 0, 'C': 350}
discos = []
discos_info = []
hastes = {'A': [], 'B': [], 'C': []}
passo_atual = 0
total_passos = 0
num_discos = 0

def fundo():
    t.penup()
    t.goto(-500, 400)
    t.fillcolor('#34495E')
    t.begin_fill()
    for _ in range(2):
        t.forward(1000)
        t.right(90)
        t.forward(800)
        t.right(90)
    t.end_fill()

    t.color('#2C3E50')
    for i in range(20):
        t.penup()
        t.goto(random.randint(-500, 500), random.randint(-400, 400))
        t.pendown()
        t.dot(random.randint(2, 8))

def obter_discos():
    while True:
        try:
            print("╔" + "═" * 48 + "╗")
            print("║          TORRE DE HANÓI - RECURSIVIDADE        ║")
            print("║               IFPE Campus Igarassu             ║")
            print("╚" + "═" * 48 + "╝")
            n = int(input(f"\n Digite o número de discos (1 a {MAX_DISCOS}): "))

            if 1 <= n <= MAX_DISCOS:
                return n
            else:
                print(f"  Por favor, digite um número entre 1 e {MAX_DISCOS}!\n")
        except ValueError:
            print("  Por favor, digite um número válido!\n")

def plataforma():
    t.penup()
    t.goto(-400, -180)
    t.fillcolor(COR_BASE)
    t.begin_fill()
    for _ in range(2):
        t.forward(800)
        t.right(90)
        t.forward(30)
        t.right(90)
    t.end_fill()

    t.goto(-400, -180)
    t.pencolor('#D6D6D6')
    for i in range(2):
        t.pendown()
        t.forward(800)
        t.penup()
        t.goto(-400, -180 + (i * 30))

def desenhar_hastes():
    t.penup()
    for haste, x in posicoes_hastes.items():
        t.goto(x - 35, -180)
        t.fillcolor('#DEE2E6')
        t.begin_fill()
        for _ in range(2):
            t.forward(70)
            t.right(90)
            t.forward(15)
            t.right(90)
        t.end_fill()

        t.goto(x, -180)
        t.pendown()
        t.pensize(8)
        t.color(COR_HASTES)
        t.goto(x, 150)
        t.penup()

        t.goto(x - 15, -210)
        t.color(COR_TEXTO)
        t.write(haste, font=("Arial", 18, "bold"))

def criar_discos(n):
    global total_passos, discos_info, hastes
    total_passos = 2**n - 1
    discos_info = []
    hastes = {'A': list(range(n - 1, -1, -1)), 'B': [], 'C': []}

    for i in range(n):
        disco = turtle.Turtle()
        disco.shape("square")
        largura = (i + 1) * 25
        altura = 20
        disco.shapesize(altura / 20, largura / 20)

        cor_principal = CORES_DISCOS[i % len(CORES_DISCOS)]
        disco.color(cor_principal)
        disco.penup()

        posicao_vertical = n - 1 - i
        y_pos = -165 + 20 * posicao_vertical
        disco.goto(posicoes_hastes['A'], y_pos)

        discos.append(disco)
        discos_info.append({'indice': i, 'haste': 'A', 'posicao': posicao_vertical})

def contador():
    t.penup()
    t.goto(-450, 250)
    t.color('white')
    t.begin_fill()
    t.goto(-450, 280)
    t.goto(-250, 280)
    t.goto(-250, 250)
    t.goto(-450, 250)
    t.end_fill()

    t.goto(-440, 260)
    t.color('#2C3E50')
    t.write(f"MOVIMENTO: {passo_atual}/{total_passos}", 
            font=("Courier", 12, "bold"))

def atualizar_ordem(haste):
    for pos, idx in enumerate(hastes[haste]):
        x = posicoes_hastes[haste]
        y = -165 + 20 * pos
        discos[idx].goto(x, y)

def mover_disco(origem, destino):
    global passo_atual

    if not hastes[origem]:
        print(f" Movimento inválido: Haste {origem} está vazia!")
        return

    disco_idx = hastes[origem][-1]

    if hastes[destino] and hastes[destino][-1] < disco_idx:
        print(f" Movimento inválido: Não é permitido colocar disco {disco_idx+1} sobre disco {hastes[destino][-1]+1}!")
        return

    hastes[origem].pop()
    hastes[destino].append(disco_idx)

    passo_atual += 1
    contador()

    for info in discos_info:
        if info['indice'] == disco_idx:
            info['haste'] = destino
            break

    disco = discos[disco_idx]
    x_orig = posicoes_hastes[origem]
    x_dest = posicoes_hastes[destino]

    for y in range(3):
        disco.goto(x_orig, -140 + y * 20)
        time.sleep(VELOCIDADE_ANIMACAO / 4)

    disco.goto(x_dest, 60)
    time.sleep(VELOCIDADE_ANIMACAO / 2)

    atualizar_ordem(origem)
    atualizar_ordem(destino)

    time.sleep(VELOCIDADE_ANIMACAO / 2)
    print(f" Passo {passo_atual}: Disco {disco_idx+1} de {origem} → {destino}")

def resolver(n, origem, destino, auxiliar):
    if n == 1:
        mover_disco(origem, destino)
        return

    resolver(n-1, origem, auxiliar, destino)
    mover_disco(origem, destino)
    resolver(n-1, auxiliar, destino, origem)

def titulo():
    t.penup()
    t.goto(0, 300)
    t.color('white')
    t.write("TORRE DE HANÓI",
            align="center", font=("Arial", 24, "bold"))

    t.goto(0, 270)
    t.write("Demonstração de Recursividade em Python", 
            align="center", font=("Arial", 16, "italic"))

    t.goto(0, -280)
    t.write("IFPE Campus Igarassu - Algoritmos e Estruturas de Dados", 
            align="center", font=("Arial", 12, "normal"))

    t.goto(0, -310)
    t.write(f"Discos: {num_discos} | Movimentos mínimos: {total_passos}", 
            align="center", font=("Arial", 10, "italic"))

if __name__ == "__main__":
    fundo()
    num_discos = obter_discos()

    print(f"\n Iniciando Torre de Hanói com {num_discos} discos...")
    print(f" Total teórico de movimentos: {2**num_discos - 1}")
    print("Renderizando visualização gráfica...")
    print("╔" + "═" * 50 + "╗")

    plataforma()
    desenhar_hastes()
    criar_discos(num_discos)
    titulo()
    contador()

    time.sleep(1)
    resolver(num_discos, 'A', 'C', 'B')

    print("╚" + "═" * 50 + "╝")
    print(f"Concluído! Movimentos executados: {passo_atual}")
    print("Demonstração de recursividade finalizada!")
    print("\n Dica: Feche a janela para encerrar.")

    turtle.done()