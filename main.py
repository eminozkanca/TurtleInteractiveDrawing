import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor('lightblue')
drawing_board.title('Interactive Board')

turtleE =turtle.Turtle()
turtleE.pensize(3)
turtleE.pencolor('darkblue')


def turtle_forward():
    turtleE.forward(100)
def turtle_backward():
    turtleE.backward(100)
def turtle_left():
    turtleE.left(10)
def turtle_right():
    turtleE.right(10)

def clear_screen():
    turtleE.clear()

def turn_home():
    turtleE.penup()
    turtleE.home()
    turtleE.pendown()

def turtlepen_up():
    turtleE.penup()
def turtlepen_down():
    turtleE.pendown()


drawing_board.onkey(turtle_forward, 'Up')
drawing_board.onkey(turtle_backward, 'Down')
drawing_board.onkey(turtle_left, 'Left')
drawing_board.onkey(turtle_right, 'Right')
drawing_board.onkey(clear_screen, 'c')
drawing_board.onkey(turn_home, 'f')
drawing_board.onkey(turtlepen_up, 'w')
drawing_board.onkey(turtlepen_down, 's')

drawing_board.listen()

turtle.mainloop()