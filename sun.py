from __future__ import division, print_function
import turtle

class Sun:
    def __init__(self, name, radius, mass, color):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.color = color
        self.x = 0
        self.y = 0
        
        self.sturtle = turtle.Turtle()
        self.sturtle.up()
        self.sturtle.color(self.color)
        self.sturtle.shape("circle")
        self.sturtle.turtlesize(stretch_wid=1,stretch_len=1)
        self.sturtle.goto(0,0)

    def get_mass(self):
        return self.mass

    def get_radius(self):
        return self.radius

    def get_xpos(self):
        return 0

    def get_ypos(self):
        return 0
