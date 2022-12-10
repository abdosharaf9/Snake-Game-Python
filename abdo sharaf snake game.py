# Abdo Sharaf - Snake Game Task Using Turtle

from turtle import *
from time import *
from random import *
from winsound import *
from threading import *


screen = Screen()
border = Turtle()
score = Turtle()
snakeHead = Turtle()
food = Turtle()
gameOver = Turtle()

snakeBody = []
currentScore = 0
highScore = 0



def initializeScreen():
    screen.screensize(700, 700, "#41AA55")
    screen.title("Abdo Sharaf Snake Game")
    screen.tracer(0)

def setBorders():
    border.ht()
    border.speed(0)
    border.color("white")
    border.width(5)
    border.up()
    border.goto(-300, 250)
    border.down()
    for _ in range(4):
        border.fd(600)
        border.right(90)

def setInitialScore():
    score.ht()
    score.speed(0)
    score.color("white")
    score.up()
    score.goto(0, 300)
    score.write(f"Your Score: {currentScore} - High Score: {highScore}", align= "center", font=["", 32, "bold"])

def updateScore():
    score.color("white")
    score.clear()
    score.write(f"Your Score: {currentScore} - High Score: {highScore}", align= "center", font=["", 32, "bold"])

def initializeSnakeHead():
    snakeHead.speed(0)
    snakeHead.goto(0, 0)
    snakeHead.color("black", "#F89B26")
    snakeHead.shape("circle")
    snakeHead.up()
    snakeHead.currentDirection = "start"

def moveSnakeUp():
    if(snakeHead.currentDirection != "down"):
        snakeHead.currentDirection = "up"

def moveSnakeDown():
    if(snakeHead.currentDirection != "up"):
        snakeHead.currentDirection = "down"

def moveSnakeRight():
    if(snakeHead.currentDirection != "left"):
        snakeHead.currentDirection = "right"

def moveSnakeLeft():
    if(snakeHead.currentDirection != "right"):
        snakeHead.currentDirection = "left"

def moveSnake():
    if snakeHead.currentDirection == "up":
        y = snakeHead.ycor()
        snakeHead.sety(y + 20)

    if snakeHead.currentDirection == "down":
        y = snakeHead.ycor()
        snakeHead.sety(y - 20)

    if snakeHead.currentDirection == "right":
        x = snakeHead.xcor()
        snakeHead.setx(x + 20)

    if snakeHead.currentDirection == "left":
        x = snakeHead.xcor()
        snakeHead.setx(x - 20)

def generateFood():
    food.ht()
    food.up()
    food.speed(0)
    food.shape("circle")
    food.color("black", "red")
    foodX = randint(-290, 290)
    foodY = randint(-340, 240)
    food.goto(foodX, foodY)
    food.st()

def startNewGame():
    global currentScore
    currentScore = 0
    gameOver.ht()
    initializeSnakeHead()
    setInitialScore()
    for tur in snakeBody:
        tur.ht()
    snakeBody.clear()

def increaseBodyTurtles():
    newTurtle = Turtle()
    newTurtle.up()
    newTurtle.speed(0)
    newTurtle.shape("square")
    newTurtle.color("black", "#F89B26")
    snakeBody.append(newTurtle)

def moveAllBody():
    for i in range(len(snakeBody)-1, 0, -1):
        x = snakeBody[i-1].xcor()
        y = snakeBody[i-1].ycor()
        snakeBody[i].goto(x, y)

    if len(snakeBody) > 0:
            x = snakeHead.xcor()
            y = snakeHead.ycor()
            snakeBody[0].goto(x, y)

def checkSelfDying():
    for tur in snakeBody:
        if tur.distance(snakeHead) < 20:
            showGameOver()
            startNewGame()

def setGameOverSound():
    PlaySound("./mixkit-arcade-retro-game-over-213.wav", SND_FILENAME|SND_ASYNC)

def setIncreaseBodySound():
    PlaySound("./mixkit-arcade-game-jump-coin-216.wav", SND_FILENAME|SND_ASYNC)

def showGameOver():
    thread = Thread(target=setGameOverSound)
    thread.start()

    gameOver.ht()
    gameOver.width(5)
    gameOver.color("red", "white")

    gameOver.up()
    gameOver.goto(-150, 50)
    gameOver.down()
    gameOver.begin_fill()
    gameOver.fd(300)
    gameOver.right(90)
    gameOver.fd(100)
    gameOver.right(90)
    gameOver.fd(300)
    gameOver.right(90)
    gameOver.fd(100)
    gameOver.right(90)
    gameOver.end_fill()

    gameOver.up()
    gameOver.goto(0, -20)
    gameOver.write("Game Over!!!", align="center", font=["", 24, "bold"])

    sleep(2.5)
    gameOver.clear()

try:
    listen()
    onkeypress(moveSnakeUp, "Up")
    onkeypress(moveSnakeDown, "Down")
    onkeypress(moveSnakeRight, "Right")
    onkeypress(moveSnakeLeft, "Left")


    initializeScreen()
    setBorders()
    startNewGame()
    generateFood()

    while True:
        screen.update()

        if snakeHead.xcor() > 295 or snakeHead.xcor() < -295 or snakeHead.ycor() > 245 or snakeHead.ycor() < -345:
            showGameOver()
            startNewGame()

        if snakeHead.distance(food) < 20:
            thread = Thread(target=setIncreaseBodySound)
            thread.start()
            increaseBodyTurtles()
            generateFood()
            currentScore += 1
            
            if currentScore > highScore:
                highScore = currentScore


        moveAllBody()
        updateScore()
        moveSnake()
        checkSelfDying()

        sleep(0.1)

except:
    print("The End!")