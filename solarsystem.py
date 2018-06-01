
from __future__ import division, print_function
import turtle
import numpy as np

G = .1
dt = .001

# Maybe try to create multiple solar systems to make a galaxy?
class SolarSystem:
    def __init__(self, width, height):
        self.sun = None
        # Make a list of planets
        self.planets = []
        # Make a turtle for the solar system to be able to set the screen height and width
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        x_pos = np.random.uniform(-width, width, 200)
        y_pos = np.random.uniform(-height, height, 200)
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width/2.0, -height/2.0, width/2.0, height/2.0)
        self.ssscreen.tracer(50)
        self.ssscreen.bgcolor('black')
        self.ssscreen.title('Welcome to our solar system!')
        for i in range(200):
            self.star_turtle = turtle.Turtle()
            self.star_turtle.shape('circle')
            self.star_turtle.up()
            self.star_turtle.color('white')
            self.star_turtle.turtlesize(stretch_wid = .1, stretch_len = .1)
            self.star_turtle.goto(x_pos[i],y_pos[i])
        # Not sure if this is right, do I need to be in some mode for turtles?
    def addSun(self, sun):
        self.sun = sun

    def addPlanet(self, planet):
        self.planets.append(planet)

    def start(self):
        self.ssscreen.onscreenclick(turtle.goto(0,0))
# Trying to get it to start on a click, also want to display planetary data/maybe have moons
    def freeze(self):
        self.ssscreen.exitonclick()

    def movePlanet(self):
        for planet in self.planets:
            x_move = planet.get_xpos() + dt * planet.get_vx()
            y_move = planet.get_ypos() + dt * planet.get_vy()
            planet.move_planet(x_move,y_move)
            x_vector = 0 - planet.get_xpos()
            y_vector = 0 - planet.get_ypos()
            r_vector = np.sqrt(x_vector**2 + y_vector**2)
            # Using F = ma
            a_x = (G * self.sun.get_mass() * x_vector) / (r_vector)**3
            a_y = (G * self.sun.get_mass() * y_vector) / (r_vector)**3

            new_vx = planet.get_vx() + a_x*dt
            new_vy = planet.get_vy() + a_y*dt
            planet.set_vx(new_vx)
            planet.set_vy(new_vy)



