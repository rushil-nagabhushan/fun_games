import turtle
import time
import random
import sys

"""
class Snake():
def __init__(self, difficulty="medium"):
    self.difficulty = difficulty

if self.difficulty == "easy" or sys.argv[1] == "easy":
    delay = 0.2
    print("Difficulty: easy")
if self.difficulty == "medium" or sys.argv[1] == "medium":
    delay = 0.1
    print("Difficulty: medium")
if self.difficulty == "hard" or sys.argv[1] == "hard":
    delay = 0.05
    print("Difficulty: hard") """


# create window for snake 
window = turtle.Screen()
window.bgcolor("orange")
window.setup(width=600, height=600)
window.tracer(0)
window.title("snake.py")

# create head of snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

# establish snake's movement to be used in main game loop
def navigate():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_left():
    if head.direction != "right":
        head.direction = "left"

# w-a-s-d movement controls
window.listen()
window.onkey(move_up, "w")
window.onkey(move_down, "s")
window.onkey(move_left, "a")
window.onkey(move_right, "d")

tails = []

# food for snake to consume
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

def border_collision_check():
    # border collision check
    if head.xcor() > 290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # clear tails
        for i in tails:
            i.goto(1000, 1000)

        tails.clear()

def body_collision_check():
    # body collision check
    for i in tails:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # clear tails
            for i in tails:
                i.goto(1000, 1000)

            tails.clear()

def teleport_food():
    # teleport food around screen once snake consumes
    if head.distance(food) < 15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        tail = turtle.Turtle()
        tail.speed(0)
        tail.shape("square")
        tail.color("white")
        tail.penup()
        tails.append(tail)

def tail_append():
    # append tails to end of head
    for index in range(len(tails)-1, 0, -1):
        x = tails[index-1].xcor()
        y = tails[index-1].ycor()
        tails[index].goto(x, y)

    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)

def main():


    # difficulty setting for game
    delay = 0.1
    if sys.argv[0] == "easy":
        delay = 0.2
        print("Difficulty: easy")
    if sys.argv[0] == "medium":
        delay = 0.1
        print("Difficulty: medium")
    if sys.argv[0] == "hard":
        delay = 0.05
        print("Difficulty: hard")


    while True:
        window.update()
        border_collision_check()
        body_collision_check()
        teleport_food()
        tail_append()
        navigate()
        time.sleep(delay)

if __name__ == "__main__":
    # main game
    main()
