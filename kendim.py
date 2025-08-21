import turtle
import random

window = turtle.Screen()
window.bgcolor("light blue")
window.setup(width=800, height=600)

score = 0
running = True
total_time = 10

#süre yazısı
timer_pen = turtle.Turtle()
timer_pen.hideturtle()
timer_pen.penup()
timer_pen.goto(0,250)
timer_pen.color("black")

#skor yazısı

score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.goto(0, -250)
score_pen.color("black")

def update_score():
    score_pen.clear()
    score_pen.write(f"Score: {score}", align = "center", font=("Arial", 20, "bold"))

def time_update(sec):
    timer_pen.clear()
    if sec > 0:
        timer_pen.write(f"Süre: {sec}", align = "center", font=("Arial", 20, "bold"))
        window.ontimer(lambda: time_update(sec-1), 1000)
    else:
        global running
        running = False
        timer_pen.clear()
        timer_pen.write("Süre Bitti!" , align = "center", font=("Arial", 20, "bold"))

#kaplumbağa

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()

#skor artışı

def increase_score(x,y):
    global score
    if running:
        score += 1
        update_score()

t.onclick(increase_score)

def move_randomly():
    if running:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        t.goto(x, y)
        window.ontimer(move_randomly, 500)

update_score()
time_update(total_time)
move_randomly()


turtle.done()