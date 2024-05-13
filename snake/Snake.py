import turtle
import time
import random

score = 0
high_score = 0

#Configuración de la ventana
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=500)
wn.tracer(0)

#Cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#Comida
meal = turtle.Turtle()
meal.speed(0)
meal.shape("circle")
meal.color("red")
meal.penup()
meal.goto(0, 0)

segments = []

#Texto
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 210)
text.write("Score: 0  High Score: 0", align="center", font=("Courier", 15, "normal"))

#Funciones
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

delay = 0.1

# Reiniciar juego
def reset_game():
    global score
    score = 0
    update_scoreboard()
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

# Agregar un segmento nuevo
def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

# Colisión con los bordes de la pantalla
def border_collision():
    return (
        head.xcor() > 280
        or head.xcor() < -280
        or head.ycor() > 230
        or head.ycor() < -230
    )

#Colisión del la serpiente con sigo misma
def self_collision():
    for segment in segments:
        if head.distance(segment) < 20:
            return True
    return False

#Actualizar marcador
def update_scoreboard():
    text.clear()
    text.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 15, "normal"))


# Pantalla de Game Over
def game_over():
    text.clear()
    text.goto(0, 0)
    text.write("GAME OVER", align="center", font=("Courier", 30, "normal"))
    time.sleep(1)
    text.clear()
    reset_game()


# Bucle principal
while True:
    wn.update()

    

    if border_collision() or self_collision():
        reset_game()

    if head.distance(meal) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-230, 230)
        meal.goto(x, y)
        add_segment()
        score += 10
        if score > high_score:
            high_score = score
        update_scoreboard()

    total_segments = len(segments)
    for index in range(total_segments - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if total_segments > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    time.sleep(delay)
