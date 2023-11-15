from turtle import Turtle,Screen,distance,textinput
import time
from Snake2 import Snk,Food,Score,Wall

sn=Screen()
sn.bgcolor("black")
sn.setup(640,640)
sn.title("Snake game")
sn.tracer(0)
snake=Snk()
wl=Wall()
snake.create()
paused = False
sn.listen()
sn.onkey(snake.up,"Up")
sn.onkey(snake.d,"Down")
sn.onkey(snake.l,"Left")
sn.onkey(snake.r,"Right")

game= True
eat=Food()
sco=Score()
while game:
    sn.update()
    time.sleep(0.14)
    dis=snake.move()
    if snake.head.distance(Turtle.pos(eat.food))<15:
        #print("nom nom nom")
        snake.increase_size()
        eat.refresh()
        sco.score+=10
        sco.refresh()
    game=wl.hit(snake,sco)
sn.exitonclick()


