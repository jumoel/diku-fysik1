from visual import *

slope = box(pos = (0,0,0), length = 20, height = 0.5, width = 5, axis = (1,-1,0))
falling_thing = box(pos = (-5,8,0), length = 2, height = 2, width = 2, axis = (1,-1,0))

g = 9.8

# TODO: Calculate speed vector based on angle and g
speed = vector(0.1, -0.1, 0)

# TODO: Calculate the proper length to fall
while falling_thing.pos.y > (slope.pos.y - slope.length):
    rate(100)
    falling_thing.pos = falling_thing.pos + speed
