# -*- coding: cp1252 -*-
from visual import *
from math import *

def showaxes(length):
    axiswidth = length * 0.1
    axis_x = arrow(pos = (0,0,0), axis = (length,0,0), shaftwidth = axiswidth, color = color.red)
    axis_y = arrow(pos = (0,0,0), axis = (0,length,0), shaftwidth = axiswidth, color = color.blue)
    axis_z = arrow(pos = (0,0,0), axis = (0,0,length), shaftwidth = axiswidth, color = color.green)

scene.title = "Projektilaffyring"

angle = radians(85) # degrees
v0 = 10 # m/s-ish
g = 9.8 # m/s^2

v_0x = v0 * cos(angle)
v_0y = v0 * sin(angle)
t_max = 2*v_0y / g

y_max = v_0y * (t_max / 2) - (g / 2) * pow(t_max / 2, 2)
x_max = v_0x * t_max

scene.height = 700
scene.width = 700
largest_edge = x_max if x_max > y_max else y_max

scene.center = (largest_edge * 0.5 , largest_edge * 0.5, 0)
scene.range = (largest_edge * 0.5 * 1.1, largest_edge * 0.5 * 1.1, 1.0)
scene.autoscale = False

showaxes(x_max / 10)

ball = sphere(pos=(0,0,0), radius=x_max / 100)

dt = 0.001
t = 0
while (ball.pos.y > 0 or ball.pos.x == 0):
    rate(1/dt)
    ball.pos.y = v_0y * t - 0.5 * g * t * t
    ball.pos.x = v_0x * t

    if (ball.pos.y < 0):
        ball.pos.y = 0
    
    t = t + dt
