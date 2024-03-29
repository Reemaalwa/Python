def draw_rocket():
    '''Draws a rocket with turtle graphics'''
    import turtle
    turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor('white')
    turtle.pencolor('black')
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(-60,-150)
    turtle.pendown()
    '''mainbody'''
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.forward(105)
    turtle.setheading(60)
    turtle.circle(500,68)
    turtle.setheading(229)
    turtle.circle(502,68)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-58,-149)
    turtle.setheading(0)
    turtle.pendown()
    
    '''Down nozzle'''
    turtle.fillcolor('orange')
    turtle.begin_fill()
    turtle.forward(100)
    turtle.setheading(-70)
    turtle.forward(100)
    turtle.setheading(180)
    turtle.forward(170)
    turtle.setheading(70)
    turtle.forward(101)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(0,180)
    turtle.setheading(0)
    turtle.pendown()
    '''white circle'''
    turtle.fillcolor('light blue')
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(90,-58)
    turtle.setheading(-40)
    turtle.pendown()
    
    '''right wing'''
    turtle.fillcolor('light grey')
    turtle.begin_fill()
    turtle.forward(90)
    turtle.setheading(-95)
    turtle.forward(190)
    turtle.setheading(-180)
    turtle.forward(40)
    turtle.setheading(92)
    turtle.forward(140)
    turtle.setheading(130)
    turtle.forward(60)
    turtle.setheading(63)
    turtle.forward(70)
    turtle.end_fill()
    
    '''left wing'''
    turtle.penup()
    turtle.goto(-103,-52)
    turtle.setheading(210)
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.forward(90)
    turtle.setheading(-85)
    turtle.forward(200)
    turtle.setheading(0)
    turtle.forward(40)
    turtle.setheading(86)
    turtle.forward(140)
    turtle.setheading(45)
    turtle.forward(60)
    turtle.setheading(118)
    turtle.forward(71)
    turtle.end_fill()
    
    turtle.hideturtle()
    turtle.done()

draw_rocket()