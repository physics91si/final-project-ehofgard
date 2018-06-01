from __future__ import division, print_function
# This will define a planet class to use to model the solar system
# A planet has a mass, a name, it's own radius, and the radius from the sun
# It moves in a circular orbit around the sun and thus also has angular velocity
# Can animate the planets using turtle
# I would also like the user to be able to change the size of the central mass to see how the planets can change
# Or should I use Kepler's Laws???
# need to compute position from the orbital elements!
# need to calculate time in the main file
import numpy as np 
# for some reason, the visual import didn't work?
import turtle
# mass of the earth
mass_earth = 5.97e24
G = 6.67384e-11
mass_sun = 1.989e30
# initial velocity of the earth, used to calculate initial momentum
velocity_earth = 30e3
# distance of the earth from the sum
distance_earth = 149.6e9
# I'm basing everything off of measurement's of the earth's radius/velocity
# Using data from NASA
class Body:
    def __init__(self, name, radius, mass, distance, vx, vy,rel_size,  color):
        self.name = name
        self.radius = radius
        self.color = color
        self.distance = distance 
        self.x = distance
        self.y = 0
        self.mass = mass
        self.vx = vx
        #vy = np.sqrt((G*mass_sun)/self.distance)
        self.vy = vy
        self.rel_size = rel_size
        self.pturtle = turtle.Turtle()
        self.pturtle.up()
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.pturtle.turtlesize(stretch_wid=self.rel_size,stretch_len=self.rel_size)
        self.pturtle.goto(distance,0)
        self.pturtle.down()
        if self.name != 'Earth' and self.name != 'Mercury' and self.name != 'Venus':
            self.pturtle.write(self.name,align='center',font=("Arial", 12, "normal"))
#        if self.name == 'Saturn':
#            s = Shape('compound')
#            s.addcomponent('circle,' stretch_wid = self.rel_size, stretch_len = self.rel_size, self.color)
#            s.addcomponent('circle', stretch_wid = self.rel_size*1.5, stretch_len = self.rel_size/1.5,self.color)
    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_vx(self):
        return self.vx

    def get_vy(self):
        return self.vy

    def get_xpos(self):
        return self.x

    def get_ypos(self):
        return self.y

    # need to be able to move the planets/set new x and y velocities
    def move_planet(self,new_x,new_y):
        self.x = new_x
        self.y = new_y
        self.pturtle.goto(new_x,new_y)

    def set_vx(self,new_vx):
        self.vx = new_vx

    def set_vy(self,new_vy):
        self.vy = new_vy

    def get_force(self):
        # Returns the force on an orbiting planet given by Newton's law of gravitation
        force = (G*M*self.m)/(sun_radius + self.radius_from_central + self.radius)**2
        return force

    def get__angular_velocity(self):
        # Assumes perfectly circular orbit, uses centripetal force = gravitation force to compute the velocity
        angular_velocity = np.sqrt((G*M)/(sun_radius + self.radius_from_central + self.radius)**3)
        return angular_velocity

    def get_linear_velocity(self):
        linear_velocity = self.get_angular_velocity()*(sun_radius + self.radius_from_central + self.radius)
        return linear_velocity
