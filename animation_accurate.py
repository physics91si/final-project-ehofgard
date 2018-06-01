from __future__ import division, print_function
import body
import sun
import solarsystem
import turtle 
import numpy as np
# Now just need to fix the scaling/relative sizes! yay
# Should scale everything in terms of the Earth's mass, radius, and distance to the sun
# Otherwise this won't work
solar_system = solarsystem.SolarSystem(20,20)
sun = sun.Sun('sun', 5000,10,'yellow')
solar_system.addSun(sun)
# for the initial velocities, I am saying that the planet starts at a position of x = position from the sun and y=0
earth = body.Body('Earth', 47.5,5000, 0.3, 0,1.8,.5, 'green')
solar_system.addPlanet(earth)

mercury = body.Body('Mercury', 9.09, 276.5, 0.1161,0,2.862,0.2,'gray')
solar_system.addPlanet(mercury)

mars = body.Body('Mars', 12.63, 535, 0.456, 0, 1.4544,0.25, 'red')
solar_system.addPlanet(mars)

jupiter = body.Body('Jupiter', 266.24, 1589000, 0.3*5.2, 0, 1.8*0.439,0.8, 'orange')
solar_system.addPlanet(jupiter)

venus = body.Body('Venus', 22.539, 4075, 0.2169,0, 2.124,.45, 'brown')
solar_system.addPlanet(venus)

saturn = body.Body('Saturn', 224.4375, 476000, 2.874, 0, .585,.7, 'yellow')
solar_system.addPlanet(saturn)

uranus = body.Body('Uranus', 97.375, 72500, 5.76,0,0.4104,0.6,'blue')
solar_system.addPlanet(uranus)

neptune = body.Body('Neptune', 92.15,85500,9.015,0,.3276,0.55,'purple')
solar_system.addPlanet(neptune)
#solar_system.start()

while True:
    solar_system.movePlanet()

#solar_system.freeze()

