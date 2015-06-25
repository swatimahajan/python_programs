import turtle
def draw_square(shape):
     for i in range(0,4):
        shape.forward(100)
	shape.right(90)
	#shape.forward(100)
	#shape.right(90)
	
    
        
def draw():
    window = turtle.Screen()
    window.bgcolor("red")

    arrow = turtle.Turtle()
    arrow.shape("turtle")
    arrow.color("yellow")
    arrow.speed(3)
    for i in range(0,36):
    	draw_square(arrow)
    	arrow.right(10)
    window.exitonclick()
draw()
