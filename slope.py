# -*- coding: cp1252 -*-
from visual import *
from math import *


def showaxes(length):
    axiswidth = 0.1
    axis_x = arrow(pos = (0,0,0), axis = (length,0,0), shaftwidth = axiswidth, color = color.red)
    axis_y = arrow(pos = (0,0,0), axis = (0,length,0), shaftwidth = axiswidth, color = color.blue)
    axis_z = arrow(pos = (0,0,0), axis = (0,0,length), shaftwidth = axiswidth, color = color.green)

# Scene setup
scene.title = 'Skråt fald'
scene.height = scene.width = 800

# First things first: The x-, y- and z-axis
showaxes(20)

# Initial setup
angle = radians(-45)
direction = vector(cos(angle), sin(angle), 0)
perp_direction = vector(direction.y, direction.x, 0)

resistance_factor = 0

# The slope
slope_length = 30
slope_width = 5
slope_thickness = 0.5

slope_pos = vector(-slope_length * sin(pi - angle) / 2,
                   -slope_length * sin(angle) / 2,
                   5)

slope = box(pos = slope_pos,
            length = slope_length,
            height = slope_thickness,
            width = slope_width,
            axis = direction)


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
