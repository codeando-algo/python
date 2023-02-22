import turtle
import time
import random

delay = 0.1
body_segment = []
score = 0
high_score = 0

windows = turtle.Screen()
#titulo
windows.title('juego snake')
#tamaño de la ventana del juego
windows.setup(width=600, height=600)
#color de fondo
windows.bgcolor('light green')

#cabeza de serpiente

#Head settings
# turtle obj
head = turtle.Turtle()
#para que se quede fija
head.speed(0)
#forma de la cabeza
head.shape('square')
#color de cabeza
head.color('blue')
#para no dejar rastro de la animacion
head.penup()
#centrar
head.goto(0, 0)
#Para hacer que el programa espero a que le de otra dieccion
head.direction = 'stop'

#configuracion de la comida
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)
food.direction = 'stop'

# Marcador
text = turtle.Turtle()
text.speed(0)
text.color('black')
text.hideturtle()
text.goto(0 ,260)
text.write(f'Score 0      High Score: 0',align='center', font=('arial', 24))


def mov():
    if head.direction == 'up':
        # almacena el valor actual de la coor Y:
        y = head.ycor()
        head.sety(y + 10)

    if head.direction == 'down':
        # almacena el valor actual de la coor Y:
        y = head.ycor()
        head.sety(y - 10)

    if head.direction == 'right':
        # almacena el valor actual de la coor X:
        y = head.xcor()
        head.setx(y + 10)

    if head.direction == 'left':
        # almacena el valor actual de la coor X:
        y = head.xcor()
        head.setx(y - 10)

def dirUp():
    head.direction = 'up'
def dirDown():
        head.direction = 'down'
def dirLeft():
        head.direction = 'left'
def dirRight():
        head.direction = 'right'
    
#conectar con teclado
windows.listen()
windows.onkeypress(dirUp, 'Up')
windows.onkeypress(dirDown, 'Down')
windows.onkeypress(dirLeft, 'Left')
windows.onkeypress(dirRight, 'Right')


while True:
    windows.update()

    #colisiones con la ventana
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'


        #esconder segmentos
        for segment in body_segment:
            segment.goto(1000,1000)
        
        #Limpiar os segmentos luego de reiniciar el juego
        body_segment.clear()

        

    #colisiones con la comida
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x , y)
        #confifuracion de segmento
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup()
        body_segment.append(new_segment)
        
        score += 10
        if score > high_score:
            high_score = score

        text.clear()    
        text.write(f'Score {score}      High Score:{high_score}',align='center', font=('arial', 24))



    totalSeg = len(body_segment)


    for i in range(totalSeg - 1, 0, -1):
        x = body_segment[i-1].xcor()
        y = body_segment[i-1].ycor() 
        body_segment[i].goto(x,y)

    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body_segment[0].goto(x, y)


    mov()
    time.sleep(delay)



turtle.done()

