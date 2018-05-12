import turtle

window = turtle.Screen()
window.bgcolor('lightblue')
window.title('wacky racers')

turtle.speed(100)
turtle.penup()
turtle.goto(-140, 140)

# creates racetrack
for step in range(15):
    turtle.write(step, align='center')
    turtle.right(90)
    for num in range(8):
      turtle.penup()
      turtle.forward(10)
      turtle.pendown()
      turtle.forward(10)
    turtle.penup()
    turtle.backward(160)
    turtle.left(90)
    turtle.forward(20)


# Creates player 1
player1 = turtle.Turtle()

player1.color('red')
player1.shape('turtle')

player1.penup()
player1.goto(-160, 100)
player1.pendown()

# creates player 2
player2 = turtle.Turtle()

player2.color('blue')
player2.shape('turtle')

player2.penup()
player2.goto(-160, 0)
player2.pendown()

# button functions
def k1():
    player1.forward(10)
    if player1.xcor() > 100:
        print("player 1 wins")
        window.bye()

def k2():
    player2.forward(10)
    if player2.xcor() > 100:
        print("player 2 wins")
        window.bye()
def k3():
    window.bye()

#########     
turtle.listen()
turtle.onkey(k1, "Left")
turtle.onkey(k2, "Right")
turtle.onkey(k3, 'q')
    
