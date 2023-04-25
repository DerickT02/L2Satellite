import turtle

class Sun(turtle.Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.color = color
        self.position = position
        self.setposition(self.position)
        self.penup()
        self.hideturtle()
        #turtle.goto(self.position)
        #turtle.pendown()
        self.dot(100, self.color)
        #turtle.penup()


