import turtle
import time

screen = turtle.Screen()
screen.title('Snake Game')
screen.bgcolor('Black')
screen.setup(width=600, height=600)


head =turtle.Turtle()
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 100)

head.direction = 'stop'
segments=[]
score = 0
h_score = 0

sd = turtle.Turtle()
sd.speed(0)
sd.color('white')
sd.penup()
sd.hideturtle()
sd.write(f'Score: {score} Highest Score: {h_score}', align='center')


def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'


def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        y = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

screen.listen()
screen.onkey(go_up, 'w')
screen.onkey(go_down, 's')
screen.onkey(go_left, 'a')
screen.onkey(go_right, 'd')


while True:
    move()
    screen.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'
    

        













input()