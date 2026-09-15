import turtle
import time
import random

# ==========================================
# 1. Game Configuration & Setup
# ==========================================
DELAY = 0.1  # Speed of the game loop (lower = faster)
score = 0
high_score = 0

# Set up the screen window
wn = turtle.Screen()
wn.title("Snake Game - Python Turtle")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off automatic screen updates for smooth animation

# ==========================================
# 2. Game Entities (Head, Food, Scoreboard)
# ==========================================
# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("limegreen")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("crimson")
food.penup()
food.goto(0, 100)

# Array / List to hold the snake's growing body segments
segments = []

# Score Display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "bold"))


# ==========================================
# 3. Grid Movement & Direction Controls
# ==========================================
def go_up():
    if head.direction != "down":  # Prevent 180-degree turn
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
    # Each step moves by 20 pixels (1 grid unit)
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings (Supports both Arrow keys and WASD)
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_right, "d")


def reset_game():
    """Resets the snake and game state after a collision."""
    global score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide segments off-screen before clearing
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()  # Empty the tail list

    score = 0
    update_score()

def update_score():
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "bold"))


# ==========================================
# 4. Main Game Loop
# ==========================================
while True:
    wn.update()

    # --- A. Wall Collision Detection ---
    # Screen is 600x600 (-300 to 300)
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_game()

    # --- B. Food Collision (Eating & Growing) ---
    if head.distance(food) < 20:
        # Move food to a random position aligned to 20px grid
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        # ARRAY MANIPULATION: Add a new segment to the snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("forestgreen")
        new_segment.penup()
        segments.append(new_segment)

        # Update scores
        score += 10
        if score > high_score:
            high_score = score
        update_score()

    # --- C. Array Manipulation: Move Body Segments ---
    # Move each segment to the position of the segment ahead of it in reverse order
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move segment 0 to where the head was
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    # Move head forward
    move()

    # --- D. Self-Collision Detection ---
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    time.sleep(DELAY)