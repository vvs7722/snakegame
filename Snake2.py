from turtle import Turtle
import random,time
SET_POSITION=[(0,0),(-20,0),(-40,0)]
class Snk():
    def __init__(self):
        self.segments=[]
        self.create()
        self.head1=0
        self.count=0
        self.head=self.segments[0]
        self.lastsegpos=()
        
    def create(self):
        
        for p in SET_POSITION:
            ns= Turtle("square")
            ns.color("white")
            ns.penup()
            ns.goto(p)
            self.segments.append(ns)
  
    def move(self):
        self.lastsegpos=self.segments[-1].position()
        for seg in range(len(self.segments)-1,0,-1):
            x=self.segments[seg-1].xcor()
            y=self.segments[seg-1].ycor()
            self.segments[seg].goto(x,y)
        #print(int(x),self.segments[0].heading())
        x,y=self.segments[0].pos()
    
        if int(self.segments[0].heading())==0 and x>290:
            self.segments[0].goto(-x,y)
            
        elif int(self.segments[0].heading())==90 and y>290:
            self.segments[0].goto(x,-y)
            
        elif int(self.segments[0].heading())==270 and y<-290:
            self.segments[0].goto(x,-y)
            
        elif int(self.segments[0].heading())==180 and x<-290:
            self.segments[0].goto(-x,y)
            
        else:
            self.segments[0].forward(20)
        return self.segments[0]
    def new(self):
        for i in self.segments:
            i.goto(350,350)
        self.segments.clear()
        self.create()
        self.head=self.segments[0]
        
        
        
    def up(self):
        if self.head1!=270:
            self.segments[0].setheading(90)
            self.head1=90
    def d(self):
        if self.head1!=90:
            self.segments[0].setheading(270)
            self.head1=270
    def l(self):
        if self.head1!=0:
            self.segments[0].setheading(180)
            self.head1=180
    def r(self):
        if self.head1!=180:
            self.segments[0].setheading(0)
            self.head1=0
    def increase_size(self):
        ns= Turtle("square")
        ns.color("white")
        ns.penup()
        ns.goto(self.lastsegpos)
        self.segments.append(ns)
        
        
class Food():
    def __init__(self):
        self.food=Turtle()
        self.food.shape("circle")
        self.food.penup()
        self.food.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.food.color("green")
        self.food.speed("fastest")
        self.x=random.randint(-270,270)
        self.y=random.randint(-270,270)
        self.food.goto(self.x,self.y)
    def refresh(self):
        self.x=random.randint(-270,270)
        self.y=random.randint(-270,275)
        self.food.goto(self.x,self.y)
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,290)
        try:
            with open("snakescore.txt") as data:
                self.highscore=int(data.read())
        except:
            with open("snakescore.txt") as data:
                data.write("0")
                self.highscore=int(data.read())

        self.write(f"Score-{self.score} \t High Score-{self.highscore}",align="center",font=("Ärial",14,"normal"))
    def refresh(self):
        self.clear()
        self.write(f"Score-{self.score} \t High Score-{self.highscore}",align="center",font=("Ärial",14,"normal"))
    def restart(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("snakescore.txt","w") as data:
                data.write(str(self.highscore))
        self.score=0
class Wall():
        
    def hit(self,snake,score):
       
                
        for i in snake.segments[1::]:
            if snake.head.distance(Turtle.pos(i))<5:
                #Wall.gameover()
                score.restart()
                snake.new()
                
                
                #return False
        return True

        
                   

