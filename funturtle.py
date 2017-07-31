import turtle

turtle.shape('turtle')
square = turtle.clone()
square.shape('square')
square.goto(0, 100)
square.goto(100, 100)
square.goto(100, 0)
square.goto(0, 0)

triangle = turtle.clone()
triangle.shape("triangle")
triangle.penup()
triangle.goto(120, 100)
triangle.pendown()
triangle.goto(200, 50)
triangle.goto(120, 0)
triangle.goto(120, 100)

square.penup()
square.goto(50, 200)
square.stamp()
triangle.penup()
turtle.penup()
turtle.goto(-20, 200)
triangle.goto(120, 200)

