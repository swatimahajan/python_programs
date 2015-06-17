import turtle
#draw triangle
def draw_triangle(shape):
     #for i in range(0,3):
        shape.right(45)  
        shape.forward(100)
	shape.right(90)
	shape.forward(100)
	shape.right(90)
	shape.right(45)
	shape.forward(140)
	
def draw():
    window = turtle.Screen()
    window.bgcolor("red")

    arrow = turtle.Turtle()
    arrow.shape("turtle")
    arrow.color("yellow")
    arrow.speed(3)
    #for i in range(0,36):
    draw_triangle(arrow)
    #arrow.right(50)
    window.exitonclick()
draw()
