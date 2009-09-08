from visual import *
from math import *

angle = radians(-45)
angle_x = cos(angle)
angle_y = sin(angle)

resistance_factor = 0

direction = vector(angle_x, angle_y, 0)
perp_direction = vector(direction.y, direction.x, 0)

# TODO: Calculate position of box relative to slope
slope = box(pos = (0,0,0), length = 100, height = 0.5, width = 5, axis = direction)
falling_thing = box(pos = (-5,8,0), length = 2, height = 2, width = 2, axis = direction)

g = -9.8

d_x = g * cos(angle + pi)
d_y = g * sin(angle + pi)

dt = 0.001
slowness = 0.001

# TODO: Calculate the complete opposite of the direction vector
resistance = vector(0,0,0) * resistance_factor

accel = vector(d_x, d_y, 0) * slowness - resistance

speed = accel * dt

# TODO: Calculate the proper length to fall
while falling_thing.pos.y > (slope.pos.y - slope.length):
    rate(1/dt)
    falling_thing.pos = falling_thing.pos + speed
    speed = speed + accel*dt
