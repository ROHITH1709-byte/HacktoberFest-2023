from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Move the ball by its current x and y movement values."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse the y direction of the ball."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse the x direction of the ball."""
        self.x_move *= -1

    def reset_position(self):
        """Reset the ball to the center of the screen and reverse its x direction."""
        self.goto(0, 0)
        self.bounce_x()  # Ensure the ball moves in the opposite direction after reset

    
