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

# The falling box
falling_size = 2
falling_halfdiag = sqrt(falling_size * falling_size / 2)

falling_pos = vector(falling_halfdiag,
                     -slope_length * sin(angle),
                     5)

falling_thing = box(pos = falling_pos,
                    length = falling_size,
                    height = falling_size,
                    width = falling_size,
                    axis = direction)

# Gravity
g = -9.8

# The gravity split up along our slope-vectors
d_x = g * cos(angle + pi)
d_y = g * sin(angle + pi)

dt = 0.001
slowness = 0.001

# TODO: Calculate the complete opposite of the direction vector
resistance = vector(0,0,0) * resistance_factor

accel = vector(d_x, d_y, 0) * slowness - resistance

speed = accel * dt

while falling_thing.pos.y - falling_halfdiag > 0:
    rate(1/dt)
    falling_thing.pos = falling_thing.pos + speed
    speed = speed + accel*dt
