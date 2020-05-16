import turtle
import time
import random
delay = 0.15
score = 0
high_score = 0



#Set up screen
wn = turtle.Screen()
wn.title("VINTAGE Snake Game")
wn.setup(width=600, height=600)
wn.bgcolor("green")
wn.tracer(0) #turns off screen updates

#Make snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.penup()#does not leave a trail behind
head.goto(0,0)
head.direction = "stop"

segments = []

#make snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.penup()#does not leave a trail behind
food.goto(0,100)
food.color("red")

#make score card

pen = turtle.Turtle()
pen.penup()
pen.shape("square")
pen.goto(0,260)
pen.color("white")
pen.hideturtle()
pen.write("Score: 0  Highscore: 0", align="center",font=("Courier", 24, "normal"))
pen.direction = "stop"




#function

def go_up():
    if head.direction != "down" :
        head.direction = "up"
def go_down():
    if head.direction != "up" :
        head.direction = "down"
def go_right():
    if head.direction != "left" :
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction=="up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction=="down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction=="right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction=="left":
        x = head.xcor()
        head.setx(x - 20)

#Key mapping
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_down, "s")

#Main game loop
while True:
    wn.update()
    time.sleep(delay)

    #check for collision with border
    if head.xcor()> 290 or head.xcor()< - 290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.direction = "stop"
        head.goto(0,0)
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write("Score: {}  Highscore: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        delay = 0.15

    # check for collision with itself
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score: {}  Highscore: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))
            delay = 0.15


    #check for collision of snake with food
    if head.distance(food) < 20:
        #move food to random place
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        #add segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)

        #add score
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  Highscore: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))

        #add speed
        delay -= 0.0001

    #move end segment first in revers order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segment 0 i.e. first to where head is
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()






wn.mainloop()





