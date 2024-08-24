from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.all_snakes = []  # This list stores all the segments of the snake
        self.create_snake()
        self.head = self.all_snakes[0]  # The head of the snake is the first segment

    def create_snake(self):
        for position in self.segments_positions:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.all_snakes.append(snake_segment)

    def extend(self):
        # Add a new segment to the snake at the position of the last segment
        self.add_segment(self.all_snakes[-1].position())

    def move(self):
        # Move the snake from the last segment to the first
        for segment_num in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[segment_num - 1].xcor()
            new_y = self.all_snakes[segment_num - 1].ycor()
            self.all_snakes[segment_num].goto(new_x, new_y)
        # Move the head of the snake forward
        self.all_snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for snake in self.all_snakes:
            snake.goto(1000, 1000)
        self.all_snakes.clear()
        self.create_snake()
        self.head = self.all_snakes[0]
