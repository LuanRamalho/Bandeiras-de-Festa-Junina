import turtle
import random

def desenhar_bandeira(x, y, largura, altura, cor):
    """Desenha uma bandeira retangular em formato triangular invertido"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(cor)
    turtle.begin_fill()

    # Desenhar um retângulo com a base triangular invertida
    turtle.goto(x + largura, y)  # Linha de cima
    turtle.goto(x + largura, y - altura * 0.6)  # Desce para o ponto da base
    turtle.goto(x + largura / 2, y - altura)  # Ponto do triângulo invertido
    turtle.goto(x, y - altura * 0.6)  # Sobe para a esquerda
    turtle.goto(x, y)  # Volta para o ponto inicial
    turtle.end_fill()

def criar_bandeiras(quantidade):
    """Cria bandeiras com posições e cores aleatórias"""
    largura_tela = turtle.window_width()
    altura_tela = turtle.window_height()

    for _ in range(quantidade):
        largura = random.randint(30, 80)
        altura = random.randint(50, 120)
        x = random.randint(-largura_tela // 2 + largura, largura_tela // 2 - largura)
        y = random.randint(-altura_tela // 2 + altura, altura_tela // 2 - altura)
        cor = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])

        desenhar_bandeira(x, y, largura, altura, cor)

# Configuração inicial da tela
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Bandeiras de Festa Junina")

turtle.speed(0)
turtle.hideturtle()

# Gerar uma quantidade aleatória de bandeiras
quantidade_bandeiras = random.randint(5, 15)
criar_bandeiras(quantidade_bandeiras)

# Finalizar a execução
screen.mainloop()
