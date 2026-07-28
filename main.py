import turtle as tur
from random import randint
from time import sleep
#window creation
window = tur.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=800, height=600)
#it let the screen update and refresh after manual updating with update()
window.tracer(0)
#creating turtles
Head = tur.Turtle()
Head.shape("square")
Head.color("black")
Head.penup()
Head.goto(0, 0)
Head.direction = "stop"
body = []
#food
food = tur.Turtle()
food.shape("circle")
food.color("red")
food.penup()
x = randint(-16, 16)*20
y = randint(-11, 11)*20
food.goto(x,y)
#score
score = tur.Turtle()
score.penup()
score.hideturtle()
score.goto(0,210)
score.color("white")
score.write(f"Score : 0 | High score : 0", align="center", font=("Arial", 20, "normal"))


#functions
def move_up():
    Head.direction = "Up"
def move_down():
    Head.direction = "Down"
def move_left():
    Head.direction = "Left"
def move_right():
    Head.direction = "Right"

#event lestning to keyboard arrows
window.listen()
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.onkey(move_right,"Right")
window.onkey(move_left,"Left")

#changing dir
def changeDir():
    if(Head.direction == "Up"):
        y = Head.ycor()
        Head.sety(y+20)
    if(Head.direction=="Down"):
        y = Head.ycor()
        Head.sety(y-20)
    if(Head.direction=="Left"):
        x = Head.xcor()
        Head.setx(x-20)
    if (Head.direction == "Right"):
        x = Head.xcor()
        Head.setx(x + 20)
scorenum = 0
highscore = 0
while(True):
    window.update()
    #check for border collision
    if Head.xcor()==400 or Head.ycor()==300 or Head.xcor()==-400 or Head.ycor()==-300 :
        for elem in body :
            elem.hideturtle()
        scorenum = 0
        body.clear()
        Head.direction = "stop"
        Head.goto(0,0)
        score.clear()
        score.write(f"Score : {scorenum} | High score : {highscore}", align="center", font=("Arial", 20, "normal"))
    #checking for body coll
    for i in range(0,len(body)):
        x_head = Head.xcor()
        y_head = Head.ycor()
        if(x_head == body[i].xcor() and y_head == body[i].ycor()):
            for elem in body:
                elem.hideturtle()
            Head.direction = "stop"
            scorenum = 0
            Head.goto(0, 0)
            score.clear()
            score.write(f"Score : {scorenum} | High score : {highscore}", align="center", font=("Arial", 20, "normal"))
            body.clear()
            break
    #eating food
    if (Head.distance(food)<20):
        x = randint(-16, 16)*20
        y = randint(-11, 11)*20
        food.goto(x,y)
        elem = tur.Turtle()
        elem.shape("square")
        elem.penup()
        elem.color("gray")
        body.append(elem)
        scorenum += 10
        if highscore < scorenum :
            highscore = scorenum
        score.clear()
        score.write(f"Score : {scorenum} | High score : {highscore}", align="center", font=("Arial",20,"normal"))
    for i in range(len(body)-1,0,-1):
        y = body[i-1].ycor()
        x = body[i-1].xcor()
        body[i].goto(x,y)
    if len(body) != 0:
        x_head= Head.xcor()
        y_head= Head.ycor()
        body[0].goto(x_head,y_head)
    sleep(0.09)
    changeDir()

