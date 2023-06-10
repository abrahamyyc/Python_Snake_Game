from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.segments_list = []
        self.create_snake()
        self.head = self.segments_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.segments_list.append(snake_body)

    def reset(self):
        for seg in self.segments_list:
            seg.goto(1000, 1000)
        self.segments_list.clear()
        self.create_snake()
        self.head = self.segments_list[0]

    def extend(self):
        self.add_segment(self.segments_list[-1].position())

    def move(self):
        for segment_index in range(len(self.segments_list) - 1, 0, -1):
            new_x = self.segments_list[segment_index - 1].xcor()
            new_y = self.segments_list[segment_index - 1].ycor()
            self.segments_list[segment_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)